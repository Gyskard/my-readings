# my-readings

First small discovery project with the Django framework to satisfy a simple personal need: having a list of books, knowing if the book has been read or not, search for an author or a book. 

Deployed on heroku [here](https://my-readings-django.herokuapp.com/).

## Description

* Django project with an application named `library`.
* The model contains an **author** class and a **book** class. 
* **Books** and **authors** are added via the administration interface.
* **SQLite** is used in local and **PostgreSQL** is used in production. 
* There is 4 settings file :
  * base.py (common ground)
  * development.py
  * production.py (for heroku)
  * secrets.py (must be created in local to contain the secret key)

## Getting started

Local installation tested with a virtualized Ubuntu (18.04.4 LTS).

### Prerequisites

* python 3.6 (developed with version 3.6.9)
* pip
* git
* libpq-dev
* python3-dev
* virtualenv (optional)
* python3-virtualenv (optional)

### Installing

#### 1. Creation and use of a virtual environment (optional).

```
python3 -m venv ~/.virtualenvs/venv
source ~/.virtualenvs/venv/bin/activate
```

#### 2. Clone of the repository

```
git clone https://github.com/Gyskard/my-readings
```

#### 3. Installation of the packages

```
cd ./my-readings
pip install -r requirements.txt
```

#### 4. Add the secret key

There is no secret key in the repository, you have to add one manually in a `secrets.py` file. You can generate one via [this site web ](https://djecrety.ir/).

You can add it using this command :

```
echo -e "SECRET_KEY = 'my_key'\n" > ./MyReadings/settings/secrets.py
```

Or by adding it directly to the `./MyReadings/settings/secrets.py` :

```
SECRET_KEY = 'my_key'
```
#### 5. Launch

```
python3 manage.py migrate --settings=MyReadings.settings.development
python3 manage.py runserver --settings=MyReadings.settings.development
```

## Deployement

The project is configured to work with [heroku](https://djecrety.ir/). There are three **Config Vars** :
- DATABASE_URL = postgres://... *(automatic)*
- DJANGO_SETTINGS_MODULe = MyReadings.settings.production
- SECRET_KEY = my_key *(You can generate one via [this site web](https://heroku.com/))*

## Built With

* [Django](https://www.djangoproject.com/) - high-level Python Web framework.
  * [water.css](https://kognise.github.io/water.css/) - just-add-css collection of styles.
  * [flake8](https://flake8.pycqa.org/en/latest/) - python library which verifies pep8.
  * [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) - set of panels that display various debug information.
  * [SQLite](https://www.sqlite.org/index.html) - C-language library that implements a SQL database engine. 
* [Heroku](https://www.heroku.com/) - cloud application platform.
  * [PostgreSQL](https://www.postgresql.org/) - open source relational database.

## Authors

* **Thomas Margueritat** - *Initial work* - [Gyskard](https://github.com/Gyskard)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details