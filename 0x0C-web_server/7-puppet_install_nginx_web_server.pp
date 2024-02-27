package { 'nginx':
  ensure => installed,
}

# Ensure index file is present and contains 'Hello World!'
file { 'Website index file':
  ensure  => present,
  path    => '/var/www/html/index.nginx-debian.html',
  content => 'Hello World!',
  require => Package['nginx'],
}

# Ensure 404 file is present and contains 'Ceci n'est pas une page'
file { 'Website 404 file':
  ensure  => present,
  path    => '/var/www/html/404.html',
  content => "Ceci n'est pas une page",
}

# Ensure nginx is running
service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}
