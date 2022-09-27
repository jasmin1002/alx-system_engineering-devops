# Nginx configuration: header customization

file_line {'Customize response header':
  ensure => 'present',
  path   => '/etc/nginx/nginx.conf',
  line   => 'add_header X-Served-By $hostname',
}
