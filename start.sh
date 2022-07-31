#!/bin/sh
nohup python3 manage.py runserver 0.0.0.0:8001 >> run.log 2>&1 &
