# -------------------------------
# [0] Libs
# -------------------------------
import pandas as pd
from sodapy import Socrata
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt

# -------------------------------
# [1] Main
# -------------------------------
def main():
    # [1] Get data
    # Unauthenticated client only works with public data sets. Note 'None'
    # in place of application token, and no username or password:
    client = Socrata('www.datos.gov.co', None)

    # Example authenticated client (needed for non-public datasets):
    # client = Socrata(www.datos.gov.co,
    #                  MyAppToken,
    #                  userame='user@example.com',
    #                  password='AFakePassword')

    # [2] Results
    # Results returned as JSON from API / converted to Python list of
    # dictionaries by sodapy.
    results = client.get_all('gt2j-8ykr')
    # results = client.get('gt2j-8ykr', limit=2000)

    # [3] Convert
    # Convert to pandas DataFrame
    data = pd.DataFrame.from_records(results)

    # [*] Format columns
    # TODO: Format appropiate for other values (wait until consistency in gov's data)
    # print(data.columns)
    # ['id_de_caso', 'fecha_de_notificaci_n', 'codigo_divipola',
    #   'ciudad_de_ubicaci_n', 'departamento', 'atenci_n', 'edad', 'sexo',
    #   'tipo', 'estado', 'pa_s_de_procedencia', 'fis', 'fecha_de_muerte',
    #   'fecha_diagnostico', 'fecha_recuperado', 'fecha_reporte_web']

    # [4] Reset columns
    data.columns = ['CASE', 'NOTIFICATION_DATE', 'COD_DIVIPOLA', 'CITY', 'DEPARTAMENT', 'STATUS',
                    'AGE', 'GENDER', 'KIND', 'LEVEL', 'ORIGIN', 'SYMPTOMS_BEGINNING_DATE',
                    'DEATH_DATE', 'DIAGNOSIS_DATE', 'RECOVERED_DATE', 'REPORT_DATE']

    # [*] Format - Date
    # TODO: Format appropiate for other date values (wait until consistency in gov's data) - POSIXct
    # dates = ['NOTIFICATION_DATE', 'SYMPTOMS_BEGINNING_DATE', 'DEATH_DATE', 'DIAGNOSIS_DATE', 'RECOVERED_DATE', 'REPORT_DATE']
    # data[dates] = data[dates].replace('-   -', pd.NaT)
    # data[dates] = data[dates].apply(pd.to_datetime, infer_datetime_format = True)

    # [5] Format - Uppercase
    strings = ['GENDER', 'STATUS', 'KIND', 'LEVEL', 'ORIGIN', 'SYMPTOMS_BEGINNING_DATE']
    data[strings] = data[strings].apply(lambda x: x.astype(str).str.upper())

    # [6] Export!
    records(data)
    statistics(data)
    timeline(data)

# -------------------------------
# [2] List of CASES
# -------------------------------
# Full list of CASES with all its RECORDS
# @arg  {pd.dataFrame} data     -- The dataFrame
def records(data):
    # [1] Export!
    export(data, 'records');

# -------------------------------
# [3] Statistics
# -------------------------------
# Get CASES per CITY and DEPARTAMENT with COORDINATES
# @arg  {pd.dataFrame} data     -- The dataFrame
def statistics(data):
    # [1] Get CASES per CITY and DEPARTAMENT
    statistics = data.groupby(['CITY', 'DEPARTAMENT']).size().reset_index()

    # [2] Reset columns
    statistics.columns = ['CITY', 'DEPARTAMENT', 'CASES']

    # [3] Config geolocator
    geolocator = Nominatim(user_agent = 'col-covid-19', timeout = None)

    # [4] Query
    statistics['COORDS'] = statistics['CITY'] + ', ' + statistics['DEPARTAMENT'] + ', ' + 'Colombia'

    # [5] Get COORDINATES - 1st try (by CITY + DEPARTAMENT)
    statistics['COORDS'] = statistics['COORDS'].apply(
        lambda coord : geolocator.geocode(coord, country_codes = 'CO')
    )

    # [6] Get COORDINATES - 2nd try (by CITY)
    statistics['COORDS'] = statistics.apply(
        lambda row: geolocator.geocode(row['CITY'], country_codes = 'CO') if pd.isnull(row['COORDS']) else row['COORDS'],
        axis = 1
    )

    # [7] Drop Not found (e.g., misspelled words) and reset index
    statistics = statistics.dropna()
    statistics = statistics.reset_index(drop = True)

    # [8] Get POINT
    statistics['LAT'] = statistics['COORDS'].apply(lambda coord : coord.latitude if coord else None)
    statistics['LNG'] = statistics['COORDS'].apply(lambda coord : coord.longitude if coord else None)

    # [9] Drop
    statistics = statistics.drop(columns = ['COORDS'])

    # [10] Export!
    export(statistics, 'statistics')
    export_JS(statistics, 'statistics')

# -------------------------------
# [4] Per DATE and STATUS
# -------------------------------
# Get CASES per DATE and STATUS
# @arg  {pd.dataFrame} data     -- The dataFrame
def timeline(data):
    # [*] Format - Date
    # TODO: Format appropiate for other date values (wait until consistency in gov's data) - POSIXct
    # dates = ['DEATH_DATE', 'RECOVERED_DATE', 'REPORT_DATE']
    dates = ['REPORT_DATE']
    # data[dates] = data[dates].replace('-   -', pd.NaT)
    data[dates] = data[dates].apply(pd.to_datetime, infer_datetime_format = True)

    # TODO: Wait until consistency in gov's data
    cases = data.groupby(by = 'REPORT_DATE').size().reset_index()
    recovered = data[data['STATUS'] == 'RECUPERADO'].groupby(by = 'REPORT_DATE').size().reset_index()
    deaths = data[data['STATUS'] == 'FALLECIDO'].groupby(by = 'REPORT_DATE').size().reset_index()

    # [1] Get per DATE and STATUS
    # cases = data.groupby(by = 'REPORT_DATE').size().reset_index()
    # recovered = data.groupby(by = 'RECOVERED_DATE').size().reset_index()
    # deaths = data.groupby(by = 'DEATH_DATE').size().reset_index()

    # [2] Reset columns
    cases.columns = ['DATE', 'CASES']
    recovered.columns = ['DATE', 'RECOVERED']
    deaths.columns = ['DATE', 'DEATHS'];

    # [3] Merge
    timeline = pd.merge(cases, recovered, how = 'left', on = 'DATE')
    timeline = pd.merge(timeline, deaths, how = 'left', on = 'DATE')

    # [4] Fill 'NaN' values
    timeline.fillna(0, inplace = True)

    # [5] Format
    # Due to Panda's merge issue (https://github.com/pandas-dev/pandas/issues/8596)
    timeline['RECOVERED'] = timeline['RECOVERED'].astype('int64')
    timeline['DEATHS'] = timeline['DEATHS'].astype('int64')

    # [6] Sort index
    timeline.sort_index()

    # [7] Cumulative sum
    timeline['SUM_CASES'] = timeline['CASES'].cumsum()
    timeline['SUM_RECOVERED'] = timeline['RECOVERED'].cumsum()
    timeline['SUM_DEATHS'] = timeline['DEATHS'].cumsum()

    # [8] Export!
    export(timeline, 'timeline')

    # [9]
    summary(data, timeline);

    # [10] Plot
    # Dataset [1]
    dataset = timeline[['DATE', 'CASES']]
    dataset.set_index('DATE', inplace = True)

    # Axis
    axis = dataset['CASES'].plot()

    # Plot properties
    plt.suptitle('Línea de Tiempo / Timeline')
    plt.title('Casos reportados diariamente / Cases reported dairy', fontsize = 10)
    plt.xlabel('Fechas / Dates')
    plt.ylabel('No. de Casos / No. of Cases')

    # Save plot
    plt.savefig('imgs/cases.png')

    # Close plot
    plt.close()

    # Dataset [2]
    dataset = timeline[['DATE', 'SUM_CASES']]
    dataset.set_index('DATE', inplace = True)

    # Axis
    axis = dataset['SUM_CASES'].plot()

    # Plot properties
    plt.suptitle('Línea de Tiempo / Timeline')
    plt.title('Histórico de casos en el tiempo / History of cases over time', fontsize = 10)
    plt.xlabel('Fechas / Dates')
    plt.ylabel('No. de Casos / No. of Cases')

    # Save plot
    plt.savefig('imgs/timeline.png')

    # Close plot
    plt.close()

# -------------------------------
# [5] Summary
# -------------------------------
# Get important DATA
# @arg  {pd.dataFrame} data     -- The dataFrame
#       {pd.dataFrame} timeline -- The timeline dataFrame
def summary(data, timeline):
    # [1] CASES per GENDER, STATUS, KIND, LEVEL, ORIGIN
    per_gender = data['GENDER'].value_counts().reset_index()
    per_status = data['STATUS'].value_counts().reset_index()
    per_kind = data['KIND'].value_counts().reset_index()
    per_level = data['LEVEL'].value_counts().reset_index()
    per_origin = data['ORIGIN'].value_counts().reset_index()

    # [2] Reset columns
    per_gender.columns = ['GENDER', 'TOTAL']
    per_status.columns = ['STATUS', 'TOTAL']
    per_kind.columns = ['KIND', 'TOTAL']
    per_level.columns = ['LEVEL', 'TOTAL']
    per_origin.columns = ['ORIGIN', 'TOTAL']

    # [3] SUMMARY of CASES per STATUS
    summary = []
    summary.append(['CASOS', timeline['CASES'].sum()])
    summary.append(['RECUPERADOS', timeline['RECOVERED'].sum()])
    summary.append(['FALLECIDOS', timeline['DEATHS'].sum()])
    summary = pd.DataFrame(data = summary, columns = ['VALUE', 'TOTAL'])
    # TODO: difference

    # [4] Export!
    export(per_gender, 'cases_per_gender')
    export(per_status, 'cases_per_status')
    export(per_kind, 'cases_per_kind')
    export(per_level, 'cases_per_level')
    export(per_origin, 'cases_per_origin')
    export(summary, 'summary')
    export_JS(summary, 'summary')

# -------------------------------
# [6] Export
# -------------------------------
# @arg  {pd.dataFrame} data     -- The dataFrame
#       {string} filename       -- The name of the file
def export(data, filename):
    # Print
    print(f'\n[EXPORTED] {filename} \n{data}')

    # [1] To CSV
    data.to_csv(f'csv/{filename}.csv', index = False)

    # [2] To JSON
    data.to_json(f'json/{filename}.json', orient = 'index', indent = data.shape[1])

# -------------------------------
# [7] Export to JS
# -------------------------------
# @arg  {pd.dataFrame} data     -- The dataFrame
#       {string} filename       -- The name of the file
def export_JS(data, filename):
    # [3] TO JS
    # Could be used as javascript window (static) variable
    js = open(f'js/{filename}.js', 'w+')
    json = data.to_json(orient = 'index', indent = data.shape[1])
    js.write(f'window.{filename} = {json}')
    js.close()

# -------------------------------
# [8] Main
# -------------------------------
if __name__ == '__main__':
    main()
