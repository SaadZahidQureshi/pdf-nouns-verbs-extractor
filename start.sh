#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn pdf_extractor.wsgi --bind 0.0.0.0:$PORT
