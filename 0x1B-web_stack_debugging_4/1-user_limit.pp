# Puppet script that makes it possible to login with the holberton user

# Holberton User Resource
  ensure => present,
  home   => '/',
  shell  => '/bin/bash',
}

# Grant holberton user sudo privilage
exec { 'grant_sudo_privilege':
  command => 'echo "holberton ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/holberton',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'test ! -e /etc/sudoers.d/holberton',
}
