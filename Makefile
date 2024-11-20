mig:
	python3 manage.py makemigrations
	python3 manage.py migrate
user:
	python3 manage.py createsuperuser --username m --email test@gmail.com
sort:
	black .
	isort .
