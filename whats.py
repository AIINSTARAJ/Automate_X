import pywhatkit
import time

wait = int(input("Enter Wait Time: "))
close = 5
    
def send_msg():
    msg = input("Enter Message: ")
    number = input("Enter Whatsapp Number: ")
    time_ = input("Enter Time to Send: ")
    hr = int(time_.split(":")[0])
    mins = int(time_.split(":")[1])
    pywhatkit.sendwhatmsg(number,msg,hr,mins,wait,True,close)

def send_msg_instant():
    msg = input("Enter Message: ")
    number = input("Enter Whatsapp Number: ")
    pywhatkit.sendwhatmsg_instantly(number,msg,wait,True,close)

def send_img():
    number = input("Enter Whatsapp Number: ")
    image = input("Enter Image Path: ")
    time_ = input("Enter Time to Send: ")
    msg = input("Enter Caption: ")
    pywhatkit.sendwhats_image(number,image,msg,wait,True,close)


def send_msg_group():
    msg = input("Enter Message: ")
    group_ = input("Enter Group Name: ")
    time_ = input("Enter Time to Send: ")
    hr = int(time_.split(":")[0])
    mins = int(time_.split(":")[1])
    pywhatkit.sendwhatmsg_to_group(group_,msg,hr,mins,wait,True,close)


def send_msg_group_instant():
    msg = input("Enter Message: ")
    group_ = input("Enter Group Name: ")
    pywhatkit.sendwhatmsg_to_group_instantly(group_,msg,wait,True,close)

try:
    send_img()
    time.sleep(30)
    print("Message Sucessfully Sent")
except Exception as E:
    print("Message Not Sent!\n Error: ", E)

