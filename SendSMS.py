import sys
from twilio.rest import TwilioRestClient

account = "ACfd03a9b8c45fb66bab8b834a21ec578c"
token = "aff6d0726a21c044cc3797d9037e9b15"
client = TwilioRestClient(account, token)

message = client.messages.create(to="+918056903214", from_="(347) 380-7554",
                             body="Hello There!")


#print(message)