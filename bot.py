import os
from twilio.rest import Client

account_sid = 'AC7448aa8145deabde7571936157a8d064'
auth_token = '87fc686a09a0ee371b1526ee62d6704f'
client = Client(account_sid, auth_token)

def send(msg, to_):
    message = client.messages.create(
        from_ = 'whatsapp:+14155238886',
        to = f'whatsapp:{to_}',
        body = msg
    )
    print(message.sid)

to_ = input("Enter Receiver Number: ")
msg = input("Enter Message: ")

if __name__ == '__main__':
    send(msg,to_)