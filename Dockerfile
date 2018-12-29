FROM python:3.7-alpine
LABEL maintainer="benpaat@dailywarrior.ph"

RUN apk update && \
    apk --no-cache add  \
      git \
      build-base \
      postgresql-dev \
      jpeg-dev \
      zlib-dev

WORKDIR /journal
COPY ./requirements.txt .
COPY ./entrypoint.sh /journal/

RUN ["pip" ,"install", "-r", "requirements.txt"]

ENV DJANGO_SETTINGS_MODULE="journal.settings"
ENV DJANGO_MIGRATE="off"
ENV DJANGO_COLLECTSTATIC="off"
ENV CONFIG_FILE="/journal/config/prod.env"
ENV GUNICORN_WORKERS="4"
ENV GOOGLE_APPLICATION_CREDENTIALS="/secrets/secret.json"

COPY . /journal

EXPOSE 8000
RUN ["chmod", "+x", "/journal/entrypoint.sh"]
ENTRYPOINT ["/journal/entrypoint.sh"]
