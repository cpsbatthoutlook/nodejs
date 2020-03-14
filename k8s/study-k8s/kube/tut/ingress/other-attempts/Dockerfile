FROM nginx:alpine
COPY hello1.conf /etc/nginx/conf.d/default.conf
COPY hello1.html /usr/share/nginx/html/index.html
EXPOSE 80
STOPSIGNAL SIGTERM
CMD ["nginx", "-g", "daemon off;"]