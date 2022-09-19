# Client configuration file with puppet
#
$path_to_file = '/etc/ssh/ssh_config'

file {'Turn off passwd auth':
  ensure  => 'present',
  path    => '${path_to_file}',
  line    => 'PasswordAuthentication no'
}
file {'Declare identity file':
  ensure  => 'present',
  path    => '${path_to_file}',
  line    => 'IdentityFile ~/.ssh/school'
}
