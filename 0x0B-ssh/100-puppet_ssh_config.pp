# practice using Puppet to make changes to our configuration file.

file_line { 'Declare Identity File':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
}

file_line { 'Turn off password auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
}
