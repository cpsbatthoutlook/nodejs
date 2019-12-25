
## 
docker run -it -p4000:80 --name $ng1 -v /git/nodejs/nodejs-mysql-crud/nginx/volume:/etc/nginx/conf.d  $ng
## Volume contains default.conf,  server.key, pem.key


=== SSL Configuration ===

#https://www.humankode.com/ssl/create-a-selfsigned-certificate-for-nginx-in-5-minutes
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/conf.d/private.key -out /etc/nginx/conf.d/public.pem -config localhost.conf

==== localhost.conf =====
[req]
default_bits       = 2048
default_keyfile    = localhost.key
distinguished_name = req_distinguished_name
req_extensions     = req_ext
x509_extensions    = v3_ca

[req_distinguished_name]
countryName                 = Country Name (2 letter code)
countryName_default         = US
stateOrProvinceName         = State or Province Name (full name)
stateOrProvinceName_default = New York
localityName                = Locality Name (eg, city)
localityName_default        = Rochester
organizationName            = Organization Name (eg, company)
organizationName_default    = localhost
organizationalUnitName      = organizationalunit
organizationalUnitName_default = Development
commonName                  = Common Name (e.g. server FQDN or YOUR name)
commonName_default          = localhost
commonName_max              = 64

[req_ext]
subjectAltName = @alt_names

[v3_ca]
subjectAltName = @alt_names

[alt_names]
DNS.1   = localhost
DNS.2   = 127.0.0.1