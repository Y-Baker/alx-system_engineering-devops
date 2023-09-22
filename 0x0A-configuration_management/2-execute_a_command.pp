# create a manifest that kills a process named killmenow

exec { 'killmenow' :
  path    => '/bin/usr/',
  command => 'pkill killmenow',
    }
