# Enabling holberton user to login and open files without errors

# Increasing hard file limit for holberton user
exec { 'increase-hard-file-limit-for-holberton user':
  command => "sed -i '/^holberton hard/s/4/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}

# Increasing soft file limits for Holberton user
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/^holberton soft/s/5/50000/" /etc/security/limits.conf',
  path    => '/user/local/bin/:/bin/'
}
