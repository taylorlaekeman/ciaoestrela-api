install:
	pip install --upgrade pip==19.1.1
	pip install -r requirements.txt

build:
	python manage.py makemigrations
	python manage.py migrate

run:
	python manage.py runserver 0.0.0.0:8080

test:
	python -m pytest

lint:
	python -m pylint ciaoestrela_api
