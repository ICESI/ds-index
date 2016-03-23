#!/usr/bin/expect -f
spawn /usr/bin/mysql_secure_installation
expect ":" # Enter current password for root (enter for none):
send -- "\r" 
expect "n]" # Set root password? 
send -- "y\r"
expect ":" # New password:
send -- "distribuidos\r"
expect ":" # Re-enter new password:
send -- "distribuidos\r"
expect "n]" # Remove anonymous users? 
send -- "n\r"
expect "n]" # Disallow root login remotely?
send -- "n\r"
expect "n]" # Remove test database? 
send -- "n\r"
expect "n]" # Reload privilege tables now?
send -- "y\r"
expect eof
