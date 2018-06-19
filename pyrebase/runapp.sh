#!/bin/bash
cd /app
tar xvzf server.src.tar.gz
cd src
python manage.py runserver 0.0.0.0:8000

