#!/bin/sh

set -e

if [ "$DJANGO_MIGRATE" = "on" ]; then
    echo "Run migration"
    python manage.py migrate
fi

if [ "$DJANGO_COLLECTSTATIC" = "on" ]; then
    echo "Run Collectstatic"
    python manage.py collectstatic --noinput
fi

if [ "$IS_PROD" = "true" ]
then
    echo Starting Production mode
    exec gunicorn journal.wsgi:application \
        --bind 0.0.0.0:8000 \
        --name journal \
        --workers $GUNICORN_WORKERS \
        --log-level=info \
        --access-logfile - \
        --error-logfile -
else
    echo Development Mode
    exec gunicorn journal.wsgi:application \
        --bind 0.0.0.0:8000 \
        --name journal \
        --workers $GUNICORN_WORKERS \
        --log-level=info \
        --access-logfile - \
        --error-logfile - \
        --reload
fi


"$@"