![BANNER](resources/imgs/banner.png)

## 1. Acerca / About
###### Seguimiento (Mapa y Estadísticas) del **COVID-19** en **Colombia** / Tracking (Map & Statistics) **COVID-19** in **Colombia**.
Este proyecto muestra el estado (mapas y estadísticas) casi en tiempo real basado en datos del [Ministerio de Salud y Protección Social](https://www.minsalud.gov.co/Paginas/default.aspx) de Colombia, diseñado para brindar información sobre la evolución del [COVID-19](https://es.wikipedia.org/wiki/COVID-19) en el país y en sus ciudades / This project shows the state (maps and statistics) almost in real time based on data from the [Ministry of Health and Social Protection](https://www.minsalud.gov.co/Paginas/default.aspx) of Colombia, designed to provide information on the evolution of [COVID-19](https://en.wikipedia.org/wiki/Coronavirus_disease_2019) in the country and its cities.

### Actualizaciones / Updates
- **Twitter** [@ColCovid19](https://twitter.com/ColCovid19)
- **Github** [col-covid-19](https://github.com/yammadev/col-covid-19.git)

### Autor / Author
Yefferson Marí­n - ([@yammadev](https://github.com/yammadev))

### Licencia / Licence
[GNU General Public License v3.0](LICENSE)

## 2. ¿Cómo contribuír? / How to contribute?
Cualquier ayuda es bien recibida. Este repositorio está diseñado para ser fácil de replicar para cualquier otro país. / Any help will be good received. This repository is designed to be easy to replicate for any other country.

### Lista de pendientes / To do list
- Instrucciones para replicar en otro país / Instructions to replicate in other country.
- Integrar dominio propio (?) / Integrate own domain (?).
- Automatizar más tareas usando `APIs` / Automate more tasks using `APIs`.

## 3. Instrucciones / Instructions
### Herramientas y Requerimientos / Tools & Requirements
- [Git](https://git-scm.com/)
- [NPM](https://www.npmjs.com/)
- [Grunt](https://gruntjs.com/)
- [Sass](https://sass-lang.com/)

### Construir / Build
```sh
  # Instalar dependencias / Install dependencies
  $ npm install

  # Construir y exportar archivos / Build and export files
  $ grunt build

  # Reconstruir / Rebuild
  $ npm run clean-build
  $ grunt build
```

### Desarrollar / Develop
```bash
  # Esperar a hacer cambios y reconstruir / Watch for changes and rebuild
  $ grunt

  # O / Or
  # $ grunt default
  # $ grunt watch
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
