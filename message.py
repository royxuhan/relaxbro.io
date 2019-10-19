# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


account_sid = 'AC18eb94a83fab149001173c9dc7be24c5'
auth_token = '04b5f576ee5c8b2190d49a21bcfa9074'
client = Client(account_sid, auth_token)

def send(message):
    message = client.messages.create(
                                  body='chill bro',
                                  from_='+14155019697',
                                  to='+19092879363'
                              )
    return message.sid
