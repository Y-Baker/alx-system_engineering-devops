# set up your client SSH configuration file

file_line {'Remove authentication password':
  ensure => 'present',
  line   => 'PasswordAuthentication no',
  path   => '/etc/ssh/ssh_config'
}

file_line {'use private key in file':
  ensure => 'present',
  line   => 'IdentityFile ~/.ssh/school',
  path   => '/etc/ssh/ssh_config'
}
