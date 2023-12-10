#!/bin/bash

sudo /etc/init.d/mysql start
sudo mysql -uroot -e "create database if not exists WEB"
sudo pkill gunicorn
cd /home/box/web
sudo gunicorn -c etc/hello.py hello:application &
cd /home/box/web/ask
sudo gunicorn --bind 0.0.0.0:8000 ask.wsgi &
sudo /etc/init.d/nginx restart &

# sudo python /home/box/web/ask/manage.py
# sudo python /home/box/web/ask/manage.py makemigrations
