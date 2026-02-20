#!/bin/bash

APP_DIR=student-notes-api

pkill gunicorn || true

cd $APP_DIR

source venv/bin/activate

pip install -r requirements.txt

nohup gunicorn -w 2 -b 0.0.0.0:5000 wsgi:app &