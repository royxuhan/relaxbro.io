# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

account_sid = 'xxx'
auth_token = 'xxx'
client = Client(account_sid, auth_token)


def send(message):
    message = client.messages.create(
        body='chill bro',
        from_='+12028040779',
        to='+17819852066'
    )
    return message.sid
