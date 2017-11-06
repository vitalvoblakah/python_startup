#!/bin/bash

cd app

# python manage.py startapp home

echo "Deleting old migrations..."
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

python manage.py showmigrations

until python manage.py makemigrations
do
    echo "Waiting for postgres ready..."
    sleep 2
done

python manage.py migrate --fake-initial

python manage.py loaddata fixtures.json

python manage.py runserver 0.0.0.0:8000