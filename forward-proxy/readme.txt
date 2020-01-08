Apache HTTPD approach
	Straight forward
NGINX approach
   	Relies on reiz/nginx_proxy:latest


docker pull reiz/nginx_proxy:latest
docker run -d -p 3001:8888  --name $p $p1
docker cp whitelist.conf $p:/usr/local/nginx/conf/nginx.conf

