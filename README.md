# Django basic project

## How this is created

If Python 3.7 is not installed, get it with

```shell
pyenv install 3.7.9
```

Create and use virtual environment with django installed:

```shell
pyenv virtualenv 3.7.9 dj_base_env
pyenv activate dj_base_env
pip install Django
pip install psycopg2
```

Create the django project with:

```shell
django-admin startproject dj_base
python dj_base/manage.py runserver
```

and test the server is running.

## Use PostgreSQL

Launch PostgreSQL with Docker:

```
docker-compose up -d
```

Then login to [adminer](http://127.0.0.1:8080/) and create a db called `dj_base_db`

In `settings.py` use this db config:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dj_base_db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

Start server again and check it works, then you can stop it and run migrations with

```
python manage.py migrate
```
