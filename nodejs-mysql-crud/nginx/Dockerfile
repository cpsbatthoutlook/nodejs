FROM nginx:latest
COPY nginx.conf /etc/nginx/nginx.conf
COPY default_http.conf /etc/nginx/conf.d/default.conf
COPY localhost.conf /tmp/localhost.conf
#For SSL, Create CRT and copy over
#COPY default_https.conf /etc/nginx/conf.d/default.conf
ADD init_nginx.sh /tmp/init_nginx.sh
RUN bash /tmp/init_nginx.sh



#!/bin/bash
apt-get -y update && apt-get -y install openssl && \
cd /etc/nginx && sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/private.key -out /etc/nginx/public.pem -config /tmp/localhost.conf

