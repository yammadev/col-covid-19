# ----------------------------------
# [0] Libs
# ----------------------------------
import pandas as pd
from sodapy import Socrata
from geopy.geocoders import Nominatim

import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (9, 5)

# ----------------------------------
# [1] Main
# ----------------------------------
def main():
    # [1] Get data
    # Unauthenticated client only works with public data sets. Note 'None'
    # in place of application token, and no username or password:
    client = Socrata('www.datos.gov.co', None)

    # [2] Results
    # Results returned as JSON from API / converted to Python list of
    # dictionaries by sodapy.
    records, samples = client.get_all('gt2j-8ykr'), client.get_all('8835-5baf')
    # records, samples = client.get('gt2j-8ykr', limit = 2000), client.get('8835-5baf', limit = 2000)

    # [3] Convert
    # Convert to pandas DataFrame
    records, samples = pd.DataFrame.from_records(records), pd.DataFrame.from_records(samples)

    # [*] Columns
    # print(records.columns)
    # ['id_de_caso', 'fecha_de_notificaci_n', 'c_digo_divipola',
    #   'ciudad_de_ubicaci_n', 'departamento', 'atenci_n', 'edad', 'sexo',
    #   'tipo', 'estado', 'pa_s_de_procedencia', 'fis', 'fecha_diagnostico',
    #   'fecha_recuperado', 'fecha_reporte_web', 'tipo_recuperaci_n',
    #   'codigo_departamento', 'codigo_pais', 'pertenencia_etnica',
    #   'fecha_de_muerte']

    # print(samples.columns)
    # ['fecha', 'acumuladas', 'amazonas', 'antioquia', 'arauca', 'atlantico',
    #   'bogota', 'bolivar', 'boyaca', 'caldas', 'caqueta', 'casanare', 'cauca',
    #   'cesar', 'choco', 'cordoba', 'cundinamarca', 'guainia', 'guajira',
    #   'guaviare', 'huila', 'magdalena', 'meta', 'narino',
    #   'norte_de_santander', 'putumayo', 'quindio', 'risaralda', 'san_andres',
    #   'santander', 'sucre', 'tolima', 'valle_del_cauca', 'vaupes', 'vichada',
    #   'procedencia_desconocida', 'positivas_acumuladas',
    #   'negativas_acumuladas', 'positividad_acumulada', 'indeterminadas',
    #   'barranquilla', 'cartagena', 'santa_marta']

    # [4] Get desired columns
    samples = samples[['fecha', 'acumuladas']]

    # [5] Reset columns
    records.columns = ['CASE', 'NOTIFICATION_DATE', 'COD_DIVIPOLA', 'CITY', 'DEPARTAMENT', 'STATUS',
                    'AGE', 'GENDER', 'KIND', 'LEVEL', 'ORIGIN', 'SYMPTOMS_BEGINNING_DATE', 'DIAGNOSIS_DATE',
                    'RECOVERED_DATE', 'REPORT_DATE', 'KIND_OF_RECOVERY', 'DEPARTAMENT_CODE', 'COUNTRY_CODE',
                    'ETHNICITY', 'DEATH_DATE']
    samples.columns = ['DATE', 'ACCUMULATED']

    # [6] Export!
    list(records)
    processed(samples)
    statistics(records)
    timeline(records)

    # [7] Plot!
    plot()

# ----------------------------------
# [2] List of CASES
# ----------------------------------
# Full list of CASES with all its RECORDS
# @arg  {pd.dataFrame} data     -- The dataFrames
def list(data):
    # [*] Format - Date
    # TODO: Format appropiate for other date values (wait until consistency in gov's data) - POSIXct
    # dates = ['NOTIFICATION_DATE', 'SYMPTOMS_BEGINNING_DATE', 'DEATH_DATE', 'DIAGNOSIS_DATE', 'RECOVERED_DATE', 'REPORT_DATE']
    # records[dates] = records[dates].apply(pd.to_datetime, errors = 'coerce', infer_datetime_format = True)

    # [1] Format - Uppercase
    strings = ['GENDER', 'STATUS', 'KIND', 'LEVEL', 'ORIGIN', 'SYMPTOMS_BEGINNING_DATE']
    data[strings] = data[strings].apply(lambda x: x.astype(str).str.upper())

    # [2] Export!
    export(data, 'records')

# ----------------------------------
# [3] List of SAMPLES
# ----------------------------------
# Full list of SAMPLES
# @arg  {pd.dataFrame} data     -- The dataFrame
def processed(data):
    # [1] Drop NaN (e.g., misspelled dates)
    data.dropna(inplace = True)

    # [2] Format - Date
    data['DATE'] = data['DATE'].apply(pd.to_datetime, errors = 'coerce', infer_datetime_format = True)

    # [3] Format - Dtype
    data['ACCUMULATED'] = data['ACCUMULATED'].astype('int64')

    # [4] Count
    data['PROCESSED'] = data['ACCUMULATED'].diff().fillna(data['ACCUMULATED'])

    # [5] Format - Dtype
    data['PROCESSED'] = data['PROCESSED'].astype('int64')

    # [6] Reset index
    data = data.reset_index(drop = True)

    # [7] Reorganize
    data = data[['DATE', 'PROCESSED', 'ACCUMULATED']]

    # [8] Export!
    export(data, 'samples')

# ----------------------------------
# [4] Statistics
# ----------------------------------
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

# ----------------------------------
# [5] Timeline per DATE and STATUS
# ----------------------------------
# Get CASES per DATE and STATUS
# @arg  {pd.dataFrame} data     -- The dataFrame
def timeline(data):
    # [1] Format - Date
    dates = ['REPORT_DATE', 'RECOVERED_DATE', 'DEATH_DATE']
    data[dates] = data[dates].apply(pd.to_datetime, errors = 'coerce', infer_datetime_format = True)

    # [2] Get per DATE and STATUS
    cases = data.groupby(by = 'REPORT_DATE').size().reset_index()
    recovered = data[data['STATUS'] == 'RECUPERADO'].groupby(by = 'RECOVERED_DATE').size().reset_index()
    deaths = data[data['STATUS'] == 'FALLECIDO'].groupby(by = 'DEATH_DATE').size().reset_index()

    # [3] Reset columns
    cases.columns = ['DATE', 'CASES']
    recovered.columns = ['DATE', 'RECOVERED']
    deaths.columns = ['DATE', 'DEATHS']

    # [4] Merge
    timeline = pd.merge(cases, recovered, how = 'left', on = 'DATE')
    timeline = pd.merge(timeline, deaths, how = 'left', on = 'DATE')

    # [5] Fill 'NaN' values
    timeline.fillna(0, inplace = True)

    # [6] Format - Dtype
    # Due to Panda's merge issue (https://github.com/pandas-dev/pandas/issues/8596)
    timeline['RECOVERED'] = timeline['RECOVERED'].astype('int64')
    timeline['DEATHS'] = timeline['DEATHS'].astype('int64')

    # [7] Sort index
    timeline.sort_index()

    # [8] Cumulative sum
    timeline['SUM_CASES'] = timeline['CASES'].cumsum()
    timeline['SUM_RECOVERED'] = timeline['RECOVERED'].cumsum()
    timeline['SUM_DEATHS'] = timeline['DEATHS'].cumsum()

    # [9] Export!
    export(timeline, 'timeline')

    # [10] Summary
    summary(data, timeline)

# ----------------------------------
# [6] Summary
# ----------------------------------
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
    summary.append(['ULTIMO REPORTE', timeline['CASES'].iloc[-1]])
    summary.append(['ANTERIOR REPORTE', timeline['CASES'].iloc[-2]])
    summary = pd.DataFrame(data = summary, columns = ['VALUE', 'TOTAL'])

    # [4] Export!
    export(per_gender, 'cases_per_gender')
    export(per_status, 'cases_per_status')
    export(per_kind, 'cases_per_kind')
    export(per_level, 'cases_per_level')
    export(per_origin, 'cases_per_origin')
    export(summary, 'summary')
    export_JS(summary, 'summary')

# ----------------------------------
# [7] Plot selected Dataframes
# ----------------------------------
# Plot and export to PNG
def plot():
    # [1] Read
    timeline = pd.read_csv('csv/timeline.csv')
    samples = pd.read_csv('csv/samples.csv')

    # [2] Plot CASES
    dataset = timeline[['DATE', 'CASES']]
    dataset.set_index('DATE', inplace = True)

    # Plot
    dataset.plot()

    # Plot properties
    plt.suptitle('Línea de Tiempo / Timeline')
    plt.title('Casos reportados diariamente / Cases reported dairy', fontsize = 10)
    plt.xlabel('Fechas / Dates')
    plt.ylabel('No. de Casos / No. of Cases')
    plt.legend(['Confirmados / Confirmed'])

    # Save plot
    plt.savefig('imgs/cases.png')

    # Close plot
    plt.close()

    # [3] Plot TIMELINE
    dataset = timeline[['DATE', 'SUM_CASES', 'SUM_RECOVERED', 'SUM_DEATHS']]
    dataset.set_index('DATE', inplace = True)

    # Plot
    dataset.plot()

    # Plot properties
    plt.suptitle('Línea de Tiempo / Timeline')
    plt.title('Histórico de casos en el tiempo / History of cases over time', fontsize = 10)
    plt.xlabel('Fechas / Dates')
    plt.ylabel('No. de Casos / No. of Cases')
    plt.legend(['Confirmados / Confirmed', 'Recuperados / Recovered', 'Fallecidos / Deaths'])

    # Save plot
    plt.savefig('imgs/timeline.png')

    # Close plot
    plt.close()

    # [4] Plot CASES vs. SAMPLES
    dataset = samples[['DATE', 'PROCESSED']]
    dataset_2 = timeline[['DATE', 'CASES']]
    dataset.set_index('DATE', inplace = True)
    dataset_2.set_index('DATE', inplace = True)

    axis = dataset.plot()
    dataset_2.plot(ax = axis)

    # Plot properties
    plt.suptitle('Línea de Tiempo de Muestras Procesadas y Casos / Timeline of Processed Samples and Cases')
    plt.title('Histórico de muestras procesadas y casos en el tiempo / History of processed samples and cases over time', fontsize = 10)
    plt.xlabel('Fechas / Dates')
    plt.ylabel('No. de Muestras y Casos / No. of Samples and Cases')
    plt.legend(['Muestras Procesadas / Processed samples', 'Confirmados / Confirmed'])

    # Save plot
    plt.savefig('imgs/samples.png')

    # Close plot
    plt.close()

# ----------------------------------
# [8] Export to CSV
# ----------------------------------
# @arg  {pd.dataFrame} data     -- The dataFrame
#       {string} filename       -- The name of the file
def export(data, filename):
    # Print
    print(f'\n[EXPORTED] {filename} \n{data}')

    # [1] To CSV
    data.to_csv(f'csv/{filename}.csv', index = False)

# ----------------------------------
# [9] Export to JS
# ----------------------------------
# @arg  {pd.dataFrame} data     -- The dataFrame
#       {string} filename       -- The name of the file
def export_JS(data, filename):
    # This could be used as javascript window (static) variable
    js = open(f'../resources/data/{filename}.js', 'w+')
    json = data.to_json(orient = 'index', indent = data.shape[1])
    js.write(f'window.{filename} = {json}')
    js.close()

# ----------------------------------
# [10] Main
# ----------------------------------
if __name__ == '__main__':
    main()
