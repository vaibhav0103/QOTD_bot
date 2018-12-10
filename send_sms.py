from twilio.rest import Client
from credentials import *
from get_quote import get_quote
from datetime import datetime


time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

client = Client(account_sid, auth_token)

#Get quote of the Day by calling function
msg = get_quote()

message = client.messages \
    .create(
         body=msg,
         from_= my_twilio,
         to=my_phone
     )
s_id = message.sid

#Change File Path to store detail of message in log.txt
filepath = "/Complete path to store log/log.txt"

file = open(filepath, "a+")
file.write("Time: " + time + "\n")
file.write("Message: " + msg + "\n")
file.write("S.Id: " + s_id)
file.write("\n --------------------------------------------------------------------------------------")
file.close()
