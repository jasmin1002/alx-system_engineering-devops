# Nginx configuration: header customization

exec {'Customize response header':
  command  => 'sudo apt update;
  sudo apt -y install nginx;
  sed -i "16 a \\\tadd_header X-Served-By \$hostname;" /etc/nginx/nginx.conf;
  sudo service nginx restart',
  provider => 'shell',
}
