# Creating a manifest that kills a process named killmenow

exec { 'killmenow':
command => 'pkill killmenow',
path    => '/bin',
returns => [0, 1],
}
