#!/bin/bash
cd /home/ubuntu/www/mpesa/
source /home/ubuntu/www/mpesa/venv/bin/activate
service postgresql start

./manage.py makemigrations
./manage.py migrate
