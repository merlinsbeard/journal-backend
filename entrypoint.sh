#!/bin/sh
python manage.py migrate
python manage.py collectstatic --noinput
echo Starting Gunicorn.
exec gunicorn journal.wsgi:application \
    --bind 0.0.0.0:8000 \
    --name journal \
    --workers $GUNICORN_WORKERS \
    --log-level=info \
    --access-logfile - \
    --error-logfile - \
"$@"
echo woot
