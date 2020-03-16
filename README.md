## 1. Acerca / About Col-Covid-19 ![CO](docs/assets/CO.png)
Seguimiento (Mapa y Estadísticas) del **COVID-19** en **Colombia** / Tracking (Map & Statistics) **COVID-19** in **Colombia**

### Autor / Author
Yefferson Marí­n ([yammadev](https://github.com/yammadev)) - yefferson.marin@gmail.com

### Licencia / Licence
[GNU General Public License v3.0](LICENSE)

## 2. Instrucciones / Instructions
### Herramientas y Requerimientos / Tools & Requirements
- [Git](https://git-scm.com/)
- [NPM](https://www.npmjs.com/)
- [Grunt](https://gruntjs.com/)
- [Sass](https://sass-lang.com/)
- [Babel](https://babeljs.io/)

### Construir / Build
```sh
  # Clonar / Clone
  $ git clone https://github.com/yammadev/col-covid-19
  $ cd col-covid-19

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

## 3. ¿Cómo contribuír? / How to contribute?
Cualquier ayuda es bien recibida / Any help will be good received.

### Lista de pendientes / To do list
- Integrar dominio propio (?) / Integrate own domain (?).
- Automatizar más tareas usando `APIs` / Automate more tasks using `APIs`.

### Colaboradores / Contributors
La lista completa de colaboradores del proyecto saldrá aquí / Full list of project contributors will appear here.

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
- Reestructurado para una más simple y rápida solución / Restructuring for a simpler and faster solution.
- `Readme` editado / `Readme` edited.

#### Removido / Removed
- Framework `Laravel` / `Laravel` Framework.

### [0.2.0] - 2020-03-15
#### Agregado / Added
- Aplicación mínima de `Laravel` / `Laravel` minimal app.

### [0.1.0] - 2020-03-15
#### Agregado / Added
- `Commit` inicial / Initial `commit`.
