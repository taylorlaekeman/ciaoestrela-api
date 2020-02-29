install:
	pip install --upgrade pip==19.1.1
	pip install -r requirements.txt

run:
	python manage.py makemigrations orders
	python manage.py migrate
	gunicorn --bind 0.0.0.0:8080 ciaoestrela_api.wsgi

test:
	python -m pytest tests/

lint:
	python -m pylint orders
