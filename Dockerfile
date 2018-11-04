FROM python:3.7-slim
LABEL maintainer="benpaat@dailywarrior.ph"

WORKDIR /journal
COPY ./requirements.txt .

RUN pip install -r requirements.txt

ENV DJANGO_SETTINGS_MODULE='journal.settings'
ENV CONFIG_FILE='/journal/config/prod.env'

COPY . /journal

RUN python manage.py collectstatic --no-input
CMD python manage.py runserver 0.0.0.0:8000
