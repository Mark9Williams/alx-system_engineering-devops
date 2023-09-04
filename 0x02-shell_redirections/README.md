echo "Hello,World": Write a script that prints “Hello, World”, followed by a new line to the standard output.
echo "(Ôo)":Write a script that displays a confused smiley "(Ôo)'

cat /etc/passwd: Write a sript that display the content of the /etc/passwd file

echo /etc/passwd /etc/hosts: Script that displays the content of /etc/passwd and /etc/hosts

tail -n 10 /etc/passwd: Script that displays the last 10 lines of /etc/passwd

tail -n 10 /etc/passwd: Script that displays the first 10 lines of /etc/passwd

awk "NR==3":Script that displays the third line of the file iacta.

echo "Best School" > "\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)": Write a shell script that creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line

ls -la > ls_cwd_content: Write a script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.

tail -n 1 iacta >> iacta: Write a script that duplicates the last line of the file iacta. The file iacta will be in the working directory

find . -type f -name "*js" -delete: Write a script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders

find . -type d -not path '.' | wc -l: Write a script that counts the number of directories and sub-directories in the current directory.
The current and parent directories should not be taken into account
Hidden directories should be counted

ls -t1 | head:Create a script that displays the 10 newest files in the current directory.
One file per line
Sorted from the newest to the oldest

sort | uniq -u: Create a script that takes a list of words as input and prints only words that appear exactly once.
Input format: One line, one word
Output format: One line, one word
Words should be sorted

grep "root" /etc/passpwd: Display lines containing the pattern “root” from the file /etc/passwd

grep -c "bin" /etc/passwd: Display the number of lines that contain the pattern “bin” in the file /etc/passwd

grep -A 3 "root" /etc/passwd: Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.
