#!/usr/bin/env bash

if [ ${LOCAL} = true ]; then
    python3 -u src/app.py
else
    cd src
    exec gunicorn --bind :${PORT} --workers 1 --threads 2 --timeout 0 app:app
fi