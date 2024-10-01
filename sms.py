import nexmo

key = ""
secret = ""

client = nexmo.Sms(key = key,secret = secret)

number = input("Enter Phone Number: ")
msg = input("Enter the Message: ")

response = client.send_message({'from': '2348141501566','to': number,'text': msg })

response = response['messages'][0]

if response['status'] == '0':
    print('Send Message' , response['message-id'])
else:
    print('Error:', response['error-text'])