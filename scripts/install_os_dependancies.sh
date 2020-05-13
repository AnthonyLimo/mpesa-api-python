#!/bin/bash
apt-get update -y
apt-get upgrade -y
apt-get install apache2 postgresql postgresql-contrib python3-psycopg2 libpq-dev
apt-get install g++
apt-get install build-essential
