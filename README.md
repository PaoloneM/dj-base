# Django basic project

This is a sample Django project that uses default rest framework auth, exposes user info and implements some simple api.

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
        'HOST': 'db',
        'PORT': '5432',
    }
}
```

Start server again and check it works, then you can stop it and run migrations with

```
python manage.py migrate
```

## Admin

The admin interface is enabled by default, but you have to create an admin user before being able to access it:
```
python manage.py createsuperuser
```

## Setting up full containerized deploy

Once created, the project has been containerized. Current `docker-compose` file includes a service to run the Django project as a container. The following steps helps you in getting things running from scratch with Docker only.

After creating the `dj_base_db` via Adminer, run the following commands

```
docker-compose restart django
docker-compose run django python manage.py migrate
docker-compose run django python manage.py createsuperuser
docker-compose run django python manage.py loaddata /fixtures/products.json
```

## Sample api calls

Get paginated list of products
```
http://127.0.0.1:8000/api/products?format=json&page=5&page_size=10
```