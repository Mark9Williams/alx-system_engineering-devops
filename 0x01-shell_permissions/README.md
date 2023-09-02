su betty: Create a script that switches the current user to the user betty.
whoami:Write a script that prints the effective username of the current user.

groups:Write a script that prints all the groups the current user is part of.
chown betty hello: Write a script that changes the owner of the file hello to the user betty.
touch hello: Write a script that creates an empty file called hello.
chmod u+x hello: Write a script that adds execute permission to the owner of the file, 'hello' which is in the working directory

chmod u+x,g+x,o+r: Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello which is in the working directory
chmod +x: Write a script that adds execution permission to the owner, the group owner and the other users, to the file hello in the working directory wwithout using commas
chown -R vincent:staff: Write a script that changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.

chown -h vincent:staff _hello:  Write a script that changes the owner and the group owner of _hello to vincent and staff respectively.
The file _hello is in the working directory
The file _hello is a symbolic link

chown --fro=guillaume betty hello: Write a script that changes the owner of the file hello to betty only if it is owned by the user guillaume.

The file hello will be in the working directory
