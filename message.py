# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

account_sid = 'AC0f0d0cc655f0a7d78a5985be18f9012f'
auth_token = '3b6e880590703522d73e638081a24b0f'
client = Client(account_sid, auth_token)

def send(message, number):
    if number[0]!= "1":
        number = "1" + number
    number = "+" + number
    message = client.messages.create(
        body = message,
        from_='+12028040779',
        to = number
    )
    return message.sid
