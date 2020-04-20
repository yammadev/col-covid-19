# -------------------------------
# [0] Libs
# -------------------------------
import pandas as pd
from sodapy import Socrata
from geopy.geocoders import Nominatim

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

    # [4] Reset columns
    data.columns = ['CASE', 'DATE', 'COD_DIV', 'CITY', 'DEPARTAMENT', 'STATUS', 'AGE', 'GENDER',
                    'KIND', 'LEVEL', 'ORIGIN', 'SYMPTOMS_BEGINNING_DATE', 'DIAGNOSIS_DATE', 'RECOVERED_DATE',
                    'REPORT_DATE', 'DEATH_DATE']

    # [*] Format
    # TODO: Format appropiate for other date values (wait until consistency in gov's data) - POSIXct
    data['DATE'] = data['DATE'].apply(lambda date : date.split('T')[0])
    #data['SYMPTOMS_BEGINNING_DATE'] = data['SYMPTOMS_BEGINNING_DATE'].apply(lambda date : date.split('T')[0])
    #data['DIAGNOSIS_DATE'] = data['DIAGNOSIS_DATE'].apply(lambda date : date.split('T')[0])
    #data['RECOVERED_DATE'] = data['RECOVERED_DATE'].apply(lambda date : date.split('T')[0])
    #data['REPORT_DATE'] = data['REPORT_DATE'].apply(lambda date : date.split('T')[0])
    #data['DEATH_DATE'] = data['DEATH_DATE'].apply(lambda date : date.split('T')[0])

    # Uppercase
    data['GENDER'] = data['GENDER'].str.upper()
    data['STATUS'] = data['STATUS'].str.upper()

    # [] Export!
    records(data)
    statistics(data)
    timeline(data)

# -------------------------------
# [] List of CASES
# -------------------------------
# Full list of CASES with all its RECORDS
# @arg  {pd.dataFrame} data     -- The dataFrame
def records(data):
    # [1] Export!
    export(data, 'records');

# -------------------------------
# [] Statistics
# -------------------------------
# Get CASES per CITY and DEPARTAMENT with COORDINATES
# @arg  {pd.dataFrame} data     -- The dataFrame
def statistics(data):
    # [1] Get CASES per CITY and DEPARTAMENT
    statistics = data.groupby(['CITY', 'DEPARTAMENT']).size().reset_index()
    statistics.columns = ['CITY', 'DEPARTAMENT', 'CASES']

    # [2] Config geolocator
    geolocator = Nominatim(user_agent = 'col-covid-19', timeout = None)

    # [3] Query
    statistics['COORDS'] = statistics['CITY'] + ', ' + statistics['DEPARTAMENT'] + ', ' + 'Colombia'

    # [4] Get COORDINATES - 1st try (by CITY + DEPARTAMENT)
    statistics['COORDS'] = statistics['COORDS'].apply(
        lambda coord : geolocator.geocode(coord, country_codes = 'CO')
    )

    # [5] Get COORDINATES - 2nd try (by CITY)
    statistics['COORDS'] = statistics.apply(
        lambda row: geolocator.geocode(row['CITY'], country_codes = 'CO') if pd.isnull(row['COORDS']) else row['COORDS'],
        axis = 1
    )

    # [6] Drop Not found (e.g., misspelled words) and reset index
    statistics = statistics.dropna()
    statistics = statistics.reset_index(drop = True)

    # [7] Get POINT
    statistics['LAT'] = statistics['COORDS'].apply(lambda coord : coord.latitude if coord else None)
    statistics['LNG'] = statistics['COORDS'].apply(lambda coord : coord.longitude if coord else None)

    # [8] Drop
    statistics = statistics.drop(columns = ['COORDS'])

    # [9] Export!
    export(statistics, 'statistics')
    export_JS(statistics, 'statistics')

# -------------------------------
# [] Per DATE and STATUS
# -------------------------------
# Get CASES per DATE and STATUS
# @arg  {pd.dataFrame} data     -- The dataFrame
def timeline(data):
    # [1] Get per DATE and STATUS
    cases = data.groupby(by = 'DATE', sort = False).size().reset_index()
    recovered = data[(data['STATUS'] == 'RECUPERADO') | (data['STATUS'] == 'RECUPERADO (HOSPITAL)')].groupby(by = 'DATE', sort = False).size().reset_index()
    deaths = data[data['STATUS'] == 'FALLECIDO'].groupby(by = 'DATE', sort = False).size().reset_index()

    cases.columns = ['DATE', 'CASES']
    recovered.columns = ['DATE', 'RECOVERED']
    deaths.columns = ['DATE', 'DEATHS'];

    # TODO: Update with appropiate date group (wait until consistency in gov's data)
    # reported = data.groupby(by = 'REPORT_DATE', sort = False).size().reset_index()
    # recovered = data.groupby(by = 'RECOVERED_DATE', sort = False).size().reset_index()
    # deaths = data.groupby(by = 'DEATH_DATE', sort = False).size().reset_index()

    # [2] Merge
    timeline = pd.merge(cases, recovered, how = 'left', on = 'DATE')
    timeline = pd.merge(timeline, deaths, how = 'left', on = 'DATE')

    # [3] Fill 'NaN' values
    timeline.fillna(0, inplace = True)

    # [*] Format
    # Due to Panda's merge issue (https://github.com/pandas-dev/pandas/issues/8596)
    timeline['RECOVERED'] = timeline['RECOVERED'].astype('int64')
    timeline['DEATHS'] = timeline['DEATHS'].astype('int64')

    # [4] Sort index
    timeline.sort_index(ascending = True)

    # [4] Cumulative sum
    timeline['SUM_CASES'] = timeline['CASES'].cumsum()
    timeline['SUM_RECOVERED'] = timeline['RECOVERED'].cumsum()
    timeline['SUM_DEATHS'] = timeline['DEATHS'].cumsum()

    # [5] Export!
    export(timeline, 'timeline')

    # [6]
    summary(data, timeline);

# -------------------------------
# [] Summary
# -------------------------------
# Get important DATA
# @arg  {pd.dataFrame} data     -- The dataFrame
#       {pd.dataFrame} timeline -- The timeline dataFrame
def summary(data, timeline):
    # [1] CASES per STATUS
    per_status = data['STATUS'].value_counts().reset_index()
    per_status.columns = ['STATUS', 'TOTAL']

    # [2] CASES per GENDER
    per_gender = data['GENDER'].value_counts().reset_index()
    per_gender.columns = ['GENDER', 'TOTAL']

    # [3] SUMMARY of CASES per STATUS
    summary = []
    summary.append(['CASOS', timeline['CASES'].sum()])
    summary.append(['RECUPERADOS', timeline['RECOVERED'].sum()])
    summary.append(['FALLECIDOS', timeline['DEATHS'].sum()])
    summary = pd.DataFrame(data = summary, columns = ['VALUE', 'TOTAL'])
    # TODO: difference

    # [4] Export!
    export(per_status, 'cases_per_status')
    export(per_gender, 'cases_per_gender')
    export(summary, 'summary')
    export_JS(summary, 'summary')

# -------------------------------
# [] Export
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
# [] Export to JS
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
# [] Main
# -------------------------------
if __name__ == '__main__':
    main()
