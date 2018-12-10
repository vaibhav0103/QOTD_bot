# QOTD_bot

A Python script to send a **_Quote Of The Day_** message/sms to your phone using Twilio

## Getting Started

1. Create a twilio accounct by visiting [Twilio](https://www.twilio.com/try-twilio)

> With a Free/Trial account youn only get to send sms/message to verified number

2. Follow instructions and get verified number

3. Select python as your language

## Further Instructions

4. Get Credentials and Your Phone Numbers

- [x] GO to [Twilio Console](https://www.twilio.com/console/)
- [x] Get Account Sid and Auth Token
- [x] Get your twilio number and verified number

#Cloning

5. Clone this repository to your desktop

6. Subsitute your credentials in credentials.py

7. Install Twilio 
` pip install twilio `

## Finally
8. Run `send_sms.py` 

> **You'll get an sms on your verified number**

# Additional 
> **Automate message Using CRON**
* Go to terminal 
Type `sudo crontab -e`
> Add `00 10 * * * python3 fullpathto/send_sms.py` to the cron list
* Save
* Exit

## And We are Done!!
