from config import *
from twilio.rest import Client


try:
    client = Client(account_sid, auth_token)
    message = client.messages.create(body="This is a test message", from_=twilio_phone, to=customer_no)
    print(message.sid)
    print('Success!')
except Exception as e:
    print(f"Twilio API error : {str(e)}")