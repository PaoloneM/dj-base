# Django basic project

## How this is created

Create and use virtual environment with django installed:

```shell
python -m venv  ~/Development/virtualenvs/<my-env>
. ~/Development/virtualenvs/<my_env>/bin/activate
pip install Django
```

Create the django project with:

```shell
django-admin startproject dj_base
python dj_base/manage.py runserver
```

and test the server is running.

## Use PostgreSQL

