#!/bin/bash

# run local server
ip="$(ifconfig | grep -A 1 'eth0' | tail -1 | cut -d ':' -f 2 | cut -d ' ' -f 1)"

if [ "$#" = "0" ]
then
	python manage.py runserver $ip:8025
else
	python manage.py runserver $ip:$1
fi
