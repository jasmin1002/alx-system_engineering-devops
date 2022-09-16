# Resource type: exec
# kills a process named killmenow

exec {  'killmenow':
  command => 'pkill -F killmenow',
  path    => 'usr/bin/',
}
