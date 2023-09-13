FROM python:3.10-slim

ENV PYTHONBUFFERED=1

ADD ./requirements.txt /app/requirements.txt

ADD . /app 
WORKDIR /app

RUN apt update -y

RUN pip install --upgrade pip
RUN pip install django
RUN pip install djangorestframework
RUN pip install gunicorn

# RUN pip install -r /app/requirements.txt
RUN python /app/manage.py makemigrations && python /app/manage.py migrate
RUN python /app/manage.py collectstatic


EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--timeout", "600", "--workers", "1", "drf.wsgi:application"]