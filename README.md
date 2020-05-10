![SCREENSHOT](resources/imgs/screenshot.png)

## 1. Acerca / About
#### Seguimiento (Mapa y Estadísticas) del **COVID-19** en **Colombia** / Tracking (Map & Statistics) **COVID-19** in **Colombia**.
Este proyecto muestra el estado (mapas y estadísticas) casi en tiempo real basado en datos del [Ministerio de salud y protección social](https://www.minsalud.gov.co/Paginas/default.aspx) de Colombia, diseñado para brindar información sobre la evolución del [COVID-19](https://es.wikipedia.org/wiki/COVID-19) en el país y sus ciudades / This project shows the state (maps and statistics) almost in real time based on data from the [Ministry of health and social protection](https://www.minsalud.gov.co/Paginas/default.aspx) of Colombia, designed to provide information on the evolution of the [COVID -19](https://en.wikipedia.org/wiki/Coronavirus_disease_2019) in the country and its cities.

### Actualizaciones / Updates
- **Twitter** [@ColCovid19](https://twitter.com/ColCovid19)
- **Github** [col-covid-19](https://github.com/yammadev/col-covid-19.git)

### Autor / Author
Yefferson Marí­n - ([@yammadev](https://github.com/yammadev))

### Licencia / Licence
[GNU General Public License v3.0](LICENSE)

## 2. Datos / Data
Los datos utilizados son cargados (una vez se realiza una actualización) desde los [Datos Abiertos](https://www.datos.gov.co/Salud-y-Protecci-n-Social/Casos-positivos-de-COVID-19-en-Colombia/gt2j-8ykr) del Gobierno Nacional, publicados por el [Ministerio de salud y protección social](https://www.minsalud.gov.co/Paginas/default.aspx) de Colombia / The data used is loaded (once an update is made) from the [Open Data](https://www.datos.gov.co/Salud-y-Protecci-n-Social/Casos-positivos-de-COVID-19-en-Colombia/gt2j-8ykr) of the National Government, published by the [Ministry of health and social protection](https://www.minsalud.gov.co/Paginas/default.aspx) of Colombia.

Los datos formateados se encuentran disponibles en la carpeta [data/](data) para su estudio y uso en formatos `.csv` y `.json` / Formatted data is available in the [data/](data) folder for study and use in `.csv` and` .json` formats:

| Archivo / File | Referencia / Reference |
| :-----: | ---------- |
| `records` | Lista completa de CASOS con todos sus REGISTROS / Full list of CASES with all its RECORDS
| `statistics` | Casos por CIUDADES y DEPARTAMENTOS con COORDENADAS / CASES per CITY and DEPARTMENTS with COORDINATES
| `timeline` | CASOS por FECHAS y ESTADOS / CASES per DATE and STATUS
| `summary` | Resúmen de CASOS por ESTADO / Summary of CASES per STATUS
| `cases_per_gender` | CASOS por GÉNERO / CASES per GENDER
| `cases_per_status` | CASOS por FECHAS y ESTADOS / CASES per STATUS
| `cases_per_kind` | CASOS por TIPO / CASES per KIND
| `cases_per_level` | CASOS por NIVEL / CASES per LEVEL
| `cases_per_origin` | CASOS por ORIGEN / CASES per ORIGIN

Adicionalmente, las gráficas de las estadísticas en formatos `.img` / Additionally, the graphs of the statistics in `.img` formats.

| Archivo / File | Referencia / Reference |
| :-----: | ---------- |
| `cases` | CASOS reportados diariamente / CASES reported dairy
| `timeline` | Histórico de CASOS en el tiempo / History of CASES over time

Para mayor información sobre cómo usar los datos, consulte [data/generate.py](data/generate.py) / For more information on how to use the data, see [data/generate.py](data/generate.py)

![CASES](data/imgs/cases.png)

![TIMELINE](data/imgs/timeline.png)

## 3. Notas de desarrollo / Development notes
### Herramientas y Requerimientos / Tools & Requirements
- [Python](https://www.python.org/)
- [NPM](https://www.npmjs.com/)

### Construir / Build
```sh
  # Instalar dependencias / Install dependencies
  npm install

  # Construir exportar archivos / Build and export files
  npm run build

  # Después de solicitar revisar los archivos generados, será subido
  # automáticamente. De otro modo, se debe reconstruir y subir manualmente /
  # After asking to check generated files, it will be pushed automatically.
  # Otherwise it should be rebuilt and pushed manually.

  # Reconstruir / Rebuild
  npm run rebuild

  # Subir como siempre / Push as usual
```

### Manualmente / Manually
```bash
  cd data

  # Ambiente virtual / Virtual environment
  py -m venv venv

  # Activar / Activate
  venv\scripts\activate

  # Instalar requerimientos / Install requirements
  (venv) pip install -r requirements.txt

  # Generar datos / Generate data
  (venv) py generate.py

  # Desactivar / Deactivate
  (venv) venv\scripts\deactivate

  cd ..

  # Construir exportar archivos / Build and export files
  npm run build

  # O esperar a hacer cambios y reconstruir / Or watch for changes and rebuild
  npm run watch
```

## 4. Registro de Cambios / Changelog
Todos los cambios notables a este proyecto están documentados en esta parte del archivo. El formato está basado en [Keep a Changelog](http://keepachangelog.com/) / All notable changes to this project are documented in this part of the file. The format is based on [Keep a Changelog](http://keepachangelog.com/).

#### [x.y.z] - AAAA-MM-DD / YYYY-MM-DD
- **x** para versiones principales relacionadas con adiciones o cambios importantes / for major release related to major additions or changes.
- **y** para versiones menores relacionadas con adiciones o cambios menores en la versión principal actual / for minor release related to minor additions or changes in current major release.
- **z** para versiones menores relacionadas con adiciones o cambios menores en la versión menor actual / for minor release related to minor additions or changes in current minor release.

#### Extras / Extras
- **Agregado** para nuevas funciones / **Added** for new features.
- **Modificado** por cambios en la funcionalidad existente / **Modified** for changes in existing functionality.
- **Obsoleto** para funciones que se eliminarán próximamente / **Deprecated** for soon-to-be removed features.
- **Removido** para funciones eliminadas / **Removed** for removed features.
- **Corregido** cualquier corrección de errores / **Fixed for** any bug fixes.
- **Seguridad** en caso de vulnerabilidades / **Security** in case of vulnerabilities.

### [2.6.1] - 2020-05-09
#### Modificado / Modified
- Cambios menores / Minor changes.
- Screenshot.

### [2.6.0] - 2020-05-01
#### Modificado / Modified
- Cambios menores / Minor changes.
- Screenshot.
- Readme.

### [2.5.1] - 2020-04-30
#### Modificado / Modified
- Cambios menores / Minor changes.

### [2.5.0] - 2020-04-30
#### Modificado / Modified
- Gráficas / Graphs.

### [2.4.4] - 2020-04-24
#### Modificado / Modified
- Información relacionada con las fechas (Esperar hasta que haya consistencia en los datos del Gobierno) / Info related with date (Wait until consistency in gov's data).

### [2.4.3] - 2020-04-23
#### Modificado / Modified
- Cambios menores / Minor changes.

### [2.4.2] - 2020-04-22
#### Modificado / Modified
- Información relacionada con las fechas (Esperar hasta que haya consistencia en los datos del Gobierno) / Info related with date (Wait until consistency in gov's data).
- Screenshot.

### [2.4.1] - 2020-04-21
#### Removido / Removed
- Banner.

### [2.4.0] - 2020-04-21
#### Agregado / Added
- Screenshot.

#### Modificado / Modified
- Información relacionada con las fechas (Esperar hasta que haya consistencia en los datos del Gobierno) / Info related with date (Wait until consistency in gov's data).

### [2.3.0] - 2020-04-21
#### Agregado / Added
- Más información y más estadísticas / More info and more statistics.
- Gráficas / Graphs.

#### Modificado / Modified
- Dataframe.
- Limpieza del código / Code cleanning.

### [2.2.0] - 2020-04-19
#### Modificado / Modified
- Dataframe.

### [2.1.0] - 2020-04-19
#### Modificado / Modified
- Script.
- Banner.
- Readme.

### [2.0.0] - 2020-04-19
#### Agregado / Added
- Datos automatizados / Automated data.
- Datos exportados para uso general en `csv` y `json` / Data exported to general purpose in `csv` and `json`.
- Más información y más estadísticas / More info and more statistics.

#### Modificado / Modified
- Mejoras en las vistas / Improvements in front-end.
- Mejor estructura para mantenener y actualizar con frecuencia / Better structure to maintain and update frequently.
- Limpieza del código / Code cleanning.

#### Removido / Removed
- Gráficos `Chart.js` / `Chart.js` charts.

### [1.3.7] - 2020-03-31
#### Agregado / Added
- Reporte (datos) actualizado / Report (data) updated.
- Mejoras en las vistas / Improvements in front-end.

### [1.3.6] - 2020-03-29
#### Agregado / Added
- Reporte (datos) actualizado / Report (data) updated.
- Mejoras en las vistas / Improvements in front-end.

### [1.3.5] - 2020-03-25
#### Agregado / Added
- Reporte (datos) actualizado / Report (data) updated.
- Mejoras en las vistas / Improvements in front-end.

### [1.3.4] - 2020-03-23
#### Agregado / Added
- Reporte (datos) actualizado / Report (data) updated.
- Mejoras en las vistas / Improvements in front-end.

### [1.3.3] - 2020-03-21
#### Agregado / Added
- Reporte (datos) actualizado / Report (data) updated.
- Mejoras en las vistas / Improvements in front-end.

### [1.3.2] - 2020-03-21
#### Agregado / Added
- Reporte (datos) actualizado / Report (data) updated.

### [1.3.1] - 2020-03-21
#### Agregado / Added
- Reporte (datos) actualizado / Report (data) updated.
- Mejoras en las vistas / Improvements in front-end.

### [1.3.0] - 2020-03-21
#### Agregado / Added
- Reporte (datos) actualizado / Report (data) updated.
- Estadísticas acerca de la edad y el género / New statistics about age and gender.
- Gráfico `Chart.js` agregado / `Chart.js` chart added.
- Limpieza del código / Code cleanning.
- Mejoras en las vistas / Improvements in front-end.

#### Modificado / Modified
- Modularización de los archivos `.js` / `.js` files were modularized.

### [1.2.8] - 2020-03-20
#### Removido / Removed
- `Open Graph` metadata.
- Social banner.

### [1.2.7] - 2020-03-20
#### Agregado / Added
- Reporte (datos) actualizado / Report (data) updated.

### [1.2.6] - 2020-03-20
#### Agregado / Added
- Social banner.

#### Modificado / Modified
- `Open Graph` metadata.

### [1.2.5] - 2020-03-20
#### Agregado / Added
- `Open Graph` metadata.
- Pequeños ajustes en las vistas / Few improvements in front-end.

### [1.2.4] - 2020-03-20
#### Agregado / Added
- Reporte (datos) actualizado / Report (data) updated.
- Ajuste de datos para hacerlo más acertado / Adjustment of data to make it more accurate.
- Pequeños ajustes en las vistas / Few improvements in front-end.

### [1.2.3] - 2020-03-20
#### Agregado / Added
- Reporte (datos) actualizado / Report (data) updated.
- Pequeños ajustes en las vistas / Few improvements in front-end.

### [1.2.2] - 2020-03-20
#### Agregado / Added
- Reporte (datos) actualizado / Report (data) updated.
- Pequeños ajustes en las vistas / Few improvements in front-end.

### [1.2.1] - 2020-03-19
#### Agregado / Added
- Pequeñas mejoras / Few improvements.

### [1.2.0] - 2020-03-19
#### Agregado / Added
- `Vue.js` integrado / `Vue.js` integrated.
- `package-lock.json`
- Lectura de datos / Data reading.
- Vistas mejoradas / Front-end improved.

#### Modificado / Modified
- Algunas archivos se reescribieron y se reestructuran para facilitar la reutilización del proyecto / Some files where rewritten and restructured to make reusability of the project easier.

### [1.1.1] - 2020-03-17
#### Removido / Removed
- `package-lock.json`

### [1.1.0] - 2020-03-17
#### Agregado / Added
- `Sourcemaps` en archivos generados / `Sourcemaps` in generated files.
- Vistas mejoradas / Front-end improved.
- Mapa `Leaflet` agregado / `Leaflet` map added.
- Librerías `js` y `css` agregadas / `js` and `css` libraries added.

#### Modificado / Modified
- `Readme` editado / `Readme` edited.

#### Removido / Removed
- `Babel` para usar `js` simple / `Babel` to use simple `js`.

### [1.0.0] - 2020-03-16
#### Agregado / Added
- Tareas `Grunt` / `Grunt` Tasks.
- Archivos base generados con `sass` y `babel` / Base files generated with `sass` & `babel`.
- Tareas automáticas que generan `css`, `js` y `html` / Automated tasks that generates `css`, `js` & `html`.
- Arquitectura desde `resources` que exporta a `docs` archivos compilados / Architecture from `resources` that exports to `docs` compiled files.  
- Comandos `npm` para limpieza de archivos y carpetas / `npm` commands for cleaning folders & files.
- Mejor estructura para mantenener y actualizar con frecuencia / Better structure to maintain and update frequently.

#### Modificado / Modified
- `Readme` editado / `Readme` edited.

### [0.3.0] - 2020-03-15
#### Modificado / Modified
- Reestructurado para una más simple y rápida solución / Restructured for a simpler and faster solution.
- `Readme` editado / `Readme` edited.

#### Removido / Removed
- Framework `Laravel` / `Laravel` Framework.

### [0.2.0] - 2020-03-15
#### Agregado / Added
- Aplicación mínima de `Laravel` / `Laravel` minimal app.

### [0.1.0] - 2020-03-15
#### Agregado / Added
- `Commit` inicial / Initial `commit`.
