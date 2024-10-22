# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

def send_sms(body, to):
    account_sid = "" # Your Twilio account SID
    auth_token = "" # Your Twilio authentication token
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=body,
        from_="", # Your Twilio phone number (the number assigned to your account)
        to=to,
    )

    print(message.body)