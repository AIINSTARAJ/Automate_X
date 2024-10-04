from flask import *
from twilio.twiml.messaging_response import MessagingResponse
import time
from termcolor import *

app = Flask(__name__)

user_message_counts = {}
time_range = 3600

max_msg = 5

def respond(message):
    response = MessagingResponse()
    response.message(message)
    return str(response)

@app.route('/', methods=['POST'])
def reply():
    print(colored("Automated Whatsapp Test By A.I Instaraj",'green','on_blue',['bold', 'blink']))
    message = request.form.get('Body','')
    sender_id = request.form.get('From','')[9:]
    user = request.form.get('ProfileName', '')
    current_time = time.time()
    print(colored(f"Message: {message}", 'green'))
    
    if message:
        if sender_id not in user_message_counts or (current_time - user_message_counts[sender_id]['timestamp'] > time_range):
            user_message_counts[sender_id] = {'counts': 0 ,"timestamp" : current_time}
        if user_message_counts[sender_id]['counts'] >= max_msg:
            time_passed = current_time - user_message_counts[sender_id]['timestamp']
            rem_time = time_range - time_passed
            mins = int(rem_time//60)
            print(f'Remaining Time: {mins}')
            return respond(f'Dear {user}, you have reached your maximum hourly message limit. Try again in the next {mins} minutes')
        else:
            user_message_counts[sender_id]['counts'] += 1
            return respond(f'Thank you for your message! This is a practice for Whatsapp Automation by A.I Instaraj')

if __name__ == '__main__':
    app.run(debug=True)