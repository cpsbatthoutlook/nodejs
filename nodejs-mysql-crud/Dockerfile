# https://nodejs.org/de/docs/guides/nodejs-docker-webapp/  Dockerize NodeJs
FROM node:8.16-alpine
WORKDIR /app
ADD src ./
ADD package.json ./
RUN  npm install
EXPOSE 3000
CMD [ "node", "index.js" ]

## Need Mysql DB @ 172.22.0.2 : 3306
# docker build -t nodejsmysql:latest .
# docker run  -p 3000:3000  --name nodejsmysql nodejsmysql
#Another example
# https://www.digitalocean.com/community/tutorials/how-to-build-a-node-js-application-with-docker

