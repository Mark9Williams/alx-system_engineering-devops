#!/usr/bin/env bash                                                             
# making changes to our config file using puppet                                
file {'etc/ssh/ssh_config',
        ensure => 'present',
}

file_line {'No Password Aunthentication':
        path    => 'etc/ssh/ssh_config',
        line    => 'PasswordAuthentication no',
        match   => 'PasswordAuthentication yes',
        replace => 'true',
}

file_line{'private_key ~/.ssh/school':
        ensure => 'present',
        path   => 'etc/ssh/ssh_config',
        line   => 'IdentityFile ~/.ssh/school',
        match  => '^IdentityFile',
}
