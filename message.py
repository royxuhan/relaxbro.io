# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

account_sid = 'AC0f0d0cc655f0a7d78a5985be18f9012f'
auth_token = '3b6e880590703522d73e638081a24b0f'
client = Client(account_sid, auth_token)

def send(message):
    message = client.messages.create(
        body=message,
        from_='+12028040779',
        to='+17819852066'
    )
    return message.sid
