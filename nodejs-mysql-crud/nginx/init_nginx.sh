#!/bin/bash
apt-get -y update && apt-get -y install openssl  apache2-utils

# cd /etc/nginx && sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/private.key -out /etc/nginx/public.pem -config /tmp/localhost.conf
