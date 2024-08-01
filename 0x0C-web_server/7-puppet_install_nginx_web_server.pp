# Nginx installation and configuration using Puppet

# Ensure Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

# Configure Nginx to listen on port 80 and serve "Hello World!" at root
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/nginx_site.erb'),
  notify  => Service['nginx'],
}

# Create the "Hello World!" index page
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  require => Package['nginx'],
}

# Ensure the document root directory exists
file { '/var/www/html':
  ensure => directory,
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0755',
}

# Template for Nginx site configuration
file { '/etc/puppetlabs/code/environments/production/modules/nginx/templates/nginx_site.erb':
  ensure  => file,
  content => '
server {
    listen 80;
    root /var/www/html;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }

    # Redirect /redirect_me to another page with a 301 status
    location /redirect_me {
        return 301 http://example.com;  # Replace with actual redirect target
    }
}
',
}
