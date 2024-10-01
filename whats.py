import pywhatkit
import time


msg = input("Enter Message: ")
wait = int(input("Enter Wait Time: "))
close = 5
    
def send_msg(msg):
    number = input("Enter Whatsapp Number: ")
    time_ = input("Enter Time to Send: ")
    hr = int(time_.split(":")[0])
    mins = int(time_.split(":")[1])
    pywhatkit.sendwhatmsg(number,msg,hr,mins,wait,True,close)

def send_msg_instant(msg):
    number = input("Enter Whatsapp Number: ")
    pywhatkit.sendwhatmsg_instantly(number,msg,wait,True,close)

def send_msg_group():
    group_ = input("Enter Group Name: ")
    time_ = input("Enter Time to Send: ")
    hr = int(time_.split(":")[0])
    mins = int(time_.split(":")[1])
    pywhatkit.sendwhatmsg_to_group(group_,msg,hr,mins,wait,True,close)

try:
    send_msg_group()
    time.sleep(30)
    print("Message Sucessfully Sent")
except Exception as E:
    print("Message Not Sent!\n Error: ", E)

