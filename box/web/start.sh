#!/bin/bash

sudo pkill gunicorn
cd /home/box/web
sudo gunicorn -c etc/hello.py hello:application &
cd /home/box/web/ask
sudo gunicorn --bind 0.0.0.0:8000 ask.wsgi &
sudo /etc/init.d/nginx restart &
