python /app/manage.py collectstatic --no-input

gunicorn drf.wsgi:application --bind 0.0.0.0:"$PORT"