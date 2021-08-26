#!/usr/bin/env bash
sudo apt -y update
sudo apt -y install nginx

sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo "simple test message" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown ubuntu:ubuntu /data/


mkdir -p /var/www/holberton
rm -f /var/www/holberton/*
echo "Holberton School" > /var/www/holberton/index.html
echo "Ceci n'est pas une page" > /var/www/holberton/error404.html

sudo rm /etc/nginx/sites-enabled/*
printf "server {
	   listen 80;
	   listen [::]:80;

	   server_name bestfound.tech;

	   root /var/www/holberton;
	   index index.html;

	   location / {
			   try_files \$uri \$uri/ =404;
			   add_header X-Served-By \"\$HOSTNAME\";
	   }
	   location /redirect_me {
			   rewrite ^/redirect_me$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
	   }
	   location /hbnb_static {
	        alias /data/web_static/current/;
			index index.html;
       }
	   error_page 404 /error404.html;
}
" | tee /etc/nginx/sites-available/airbnb_server
sudo ln -s /etc/nginx/sites-available/airbnb_server /etc/nginx/sites-enabled/airbnb_server

sudo service nginx restart
