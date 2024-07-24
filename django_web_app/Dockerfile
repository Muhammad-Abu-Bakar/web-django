FROM python:3.10

WORKDIR /app

COPY web-django/django_web_app/requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD python /app/manage.py runserver 0.0.0.0:8000
