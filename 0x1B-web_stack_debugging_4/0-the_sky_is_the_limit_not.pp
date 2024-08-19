# Increase the amount of traffic handled by Nginx server
# Increaing the ulimit of the default file
exec { 'fix--for-nginx':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  # specifying path for the sed command
  path    => '/usr/local/bin/:/bin/',
}

# Restarting nginx
exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  # specifying the path for the init.d script
  path    => '/etc/init.d/',
}
