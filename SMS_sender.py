#SMS program to send messages

import colorama
from colorama import Fore, Back, Style
colorama.init()

import requests
from requests import get



def user_page():

 
 user_input =  int(input(Fore.GREEN + """What would you like to do?
    1. Send SMS
    2. Check Balance
    3. Exit program\n
    Select option: """))
 return user_input
                       
def user_options(user_input):
    if user_input == 1:
        send_sms()
    elif user_input == 2:
        pass
    elif user_input == 3:
        print(Fore.RED + "Exiting program...")
        pass
    else:
        print(Fore.RED + "Invalid option!")
    
    user_input = user_page()
    user_options(user_input)
    
    
def send_sms():
    print(Fore.LIGHTYELLOW_EX + "Send SMS")
    sms_body = input(Fore.CYAN + "Enter your message: ")
    sms_recipient = input(Fore.BLUE+ "Enter recipient number: ")
    sender_id = input(Fore.BLUE + "Enter sender ID: ")
    
    msg_feedback = send_info(sms_body,sms_recipient,sender_id)

def send_info(num,msg, sender_id):
    msg_feedback = get(f'http://sms.smsnotifygh.com/smsapi?key=xxxxxxxxxx&to={num}&msg={msg}1x&sender_id={sender_id}')
    return msg_feedback.text
    
    
    
user_input = user_page()
user_options(user_input)
    