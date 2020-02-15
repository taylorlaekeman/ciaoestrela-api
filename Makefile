install:
	pip install --upgrade pip==19.1.1
	pip install -r requirements.txt

run:
	python manage.py makemigrations orders
	python manage.py migrate
	python manage.py runserver 0.0.0.0:8080

test:
	python -m pytest tests/

lint:
	python -m pylint orders
