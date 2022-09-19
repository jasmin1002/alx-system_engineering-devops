# Client configuration file with puppet
#
$path_to_file = '/root/.ssh/config'

file {'Turn off passwd auth':
  ensure  => 'present',
  path    => '${path_to_file}',
  mode    => '0600',
  content => 'PasswordAuthentication no'
}

file {'Declare identity file':
  ensure  => 'present',
  path    => '${path_to_file}',
  content => 'IdentityFile ~/.ssh/school'
}
