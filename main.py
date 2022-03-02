import re
import string
import os
import threading
import random
import time
from queue import Queue



print(f'''
 ██▓ ███▄    █   █████▒██▓ ███▄    █  ██▓▄▄▄█████▓▓██   ██▓
▓██▒ ██ ▀█   █ ▓██   ▒▓██▒ ██ ▀█   █ ▓██▒▓  ██▒ ▓▒ ▒██  ██▒
▒██▒▓██  ▀█ ██▒▒████ ░▒██▒▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░  ▒██ ██░
░██░▓██▒  ▐▌██▒░▓█▒  ░░██░▓██▒  ▐▌██▒░██░░ ▓██▓ ░   ░ ▐██▓░
░██░▒██░   ▓██░░▒█░   ░██░▒██░   ▓██░░██░  ▒██▒ ░   ░ ██▒▓░
░▓  ░ ▒░   ▒ ▒  ▒ ░   ░▓  ░ ▒░   ▒ ▒ ░▓    ▒ ░░      ██▒▒▒ 
 ▒ ░░ ░░   ░ ▒░ ░      ▒ ░░ ░░   ░ ▒░ ▒ ░    ░     ▓██ ░▒░ 
 ▒ ░   ░   ░ ░  ░ ░    ▒ ░   ░   ░ ░  ▒ ░  ░       ▒ ▒ ░░  
 ░           ░         ░           ░  ░            ░ ░     
                                                   ░ ░         
[!] https://discord.gg/U3Vj2rahNa | zdvrer#8413                     
''')

print(f"""    [!] OPTIONS:    
\n          [01] Cookie generator
\n          [02] Cookie checker""")
    input(f"""Choice: """)
  
if input == '1' or input == '01':
        print(f"[!] Note: cookies will be in cookies.txt")
        main(
outputfile = open("cookies.txt", "a")

x = 0
cookies = []
intro = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_"
n = 0
print('[RECOMMENDED: Pick a high amount for better odds of generating valid cookies]')
c = int(input("[!] How many cookies do you want to generate? \n"))
print('[!] Generating random cookies... please be patient! \n')
print('Note: This doesnt check is the cookies are valid, for that please use a special script. \n')
letters = 'ABCDEF'

while x < c:


    cookies =  intro +  ''.join(random.choices(letters + string.digits, k=732))

    x = x + 1
    
    f = open('Cookies.txt', "a+")
    f.write(f'{cookies}\n')
    f.close()
    

if __name__ == '__main__':

    number_of_threads = 900
    print_lock = threading.Lock()
    cookie_queue = Queue()
    url = 'https://accountinformation.roblox.com/v1/birthdate'

        
    cookie_queue.join()

outputfile.close()

t1 = time.time()
print('[!] Done! Successfully generated all the desired cookies in cookies.txt.')
input("Press enter to exit."))
