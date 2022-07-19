release: python3 manage.py makemigrations
release: python3 manage.py migrate
web: gunicorn Markit.wsgi:application --log-file -
