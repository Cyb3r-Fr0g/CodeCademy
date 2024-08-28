#Files -- Hacking The Fender -- Cyb3r_Fr0g -- 8/28/24

import csv

compromised_users = []

#Obtains compromised users from the password leak
with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for row in password_csv:
    compromised_users.append(row['Username'])

#creates a file of the compromised users
with open('compromised_users.txt', 'w') as compromised_user_file:
  for user in compromised_users:
    compromised_user_file.write(user)

#writes a json file to be sent as a message to the boss
import json
with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
  json.dump(boss_message_dict, boss_message)

#Creates the new password file
with open('new_passwords.csv', 'w') as new_passwords_obj:
  slash_null_sig = '''

 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/

'''
  new_passwords_obj.write(slash_null_sig)
  
#replaces the leaked password file with our new password file
import os
os.replace('new_passwords.csv', 'passwords.csv')
