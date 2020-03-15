# Contacto / Contact
Yefferson Marí­n - *yefferson.marin@gmail.com*

# Herramientas y Requerimientos / Tools and Requirements
1. [Git](https://git-scm.com/)
2. [PHP >= 7.2](http://www.php.net/)
3. [Composer](https://getcomposer.org/)
5. [XAMPP](https://www.apachefriends.org/index.html) - [MySql](https://www.mysql.com/)

# Instrucciones / Instructions
## Preparar / Prepare
```sh
  # Clonar / Clone
  $ git clone https://github.com/yammadev/col-covid-19

  $ cd col-covid-19

  # Instalar dependencias / Install dependencies
  $ composer install

  # Configurar .env y generar llave / Configure .env and generate key
  $ cp .env.example .env
  $ php artisan key:generate
```

## Ejecutar / Run
```sh
  $ php artisan serve

  # Ir a / Go to -> 127.0.0.1:8000
```

# Registro de Cambios / [EN] Changelog
Todos los cambios notables a este proyecto están documentados en esta parte del archivo. El formato está basado en [Keep a Changelog](http://keepachangelog.com/) / All notable changes to this project are documented in this part of the file. The format is based on [Keep a Changelog](http://keepachangelog.com/).

#### [x.y.z] - AAAA-MM-DD / [EN] YYYY-MM-DD
- **x** para versiones principales relacionadas con adiciones o cambios importantes / for major release related to major additions or changes.
- **y** para versiones menores relacionadas con adiciones o cambios menores en la versión principal actual / for minor release related to minor additions or changes in current major release.
- **z** para versiones menores relacionadas con adiciones o cambios menores en la versión menor actual / for minor release related to minor additions or changes in current minor release.

### [0.2.0] - 2020-03-15
- Aplicación mínima de `Laravel` / `Laravel` minimal app.

### [0.1.0] - 2020-03-15
- `Commit` inicial / Initial `commit`.
