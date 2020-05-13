#!/bin/bash
chown ubuntu:ubuntu /home/ubuntu/www
apt-get install python3-pip libapache2-mod-wsgi-py3
pip3 install virtualenv
virtualenv /home/ubuntu/www/mpesa/venv
chown ubuntu:ubuntu /home/ubuntu/www/mpesa/venv
chown ubuntu:ubuntu /home/ubuntu/www/mpesa/venv/*
source /home/ubuntu/www/mpesa/venv/bin/activate
pip3 install -r /home/ubuntu/www/mpesa/requirements.txt
