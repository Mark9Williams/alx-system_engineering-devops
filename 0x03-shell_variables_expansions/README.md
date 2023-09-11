alias ls='rm *': Create a script that creates an alias.
Name: ls
Value: rm *

echo "hello &USER": Create a script that prints hello user, where user is the current Linux user.

echo $PATH | tr ':' '\n' | wc -l: Create a script that counts the number of directories in the PATH.

printenv: Create a script that lists environment variables.

set: A script that lists all local variables and environment variables, and functions.

BEST="School": a script that creates a new local variable.

export BEST ="School": a script that creates a new global variable.

echo $((128 + $TRUEKNOWLEDGE): a script that prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line.

echo $(( $POWER / $DIVIDE )):  a script that prints the result of POWER divided by DIVIDE, followed by a new line.
POWER and DIVIDE are environment variables

echo $(( $BREATH ** $ LOVE )): Write a script that displays the result of BREATH to the power LOVE
BREATH and LOVE are environment variables

echo $((2#BINARY)): Write a script that converts a number from base 2 to base 10.
The number in base 2 is stored in the environment variable BINARY

echo {a..z}{a..z}|tr ' ' '\n'|grep -v 'oo': a script that prints all possible combinations of two letters, except oo.

printf "%.2f" $NUM:  a shell script that prints a number with two decimal places, followed by a new line.
The number will be stored in the environment variable NUM.
It should be one line of code

printf "%.2f\n" "$NUM": Write a script that converts a number from base 10 to base 16.
The number in base 10 is stored in the environment variable DECIMAL
