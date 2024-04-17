# Puppet script to inpcrease nginx

$nginx_ulimit = 'ULIMIT="-n 65535"'

package { 'nginx':
}

file { '/etc/default/nginx':
  ensure  => present,
  content => $nginx_ulimit,
  notify  => Service['nginx']
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
}
