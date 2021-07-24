import datetime
import time

import requests
from twilio.rest import Client

account_sid = ''  # Enter Account SID from Twilio
auth_token = ''   # Enter Account Authentication Token from Twilio
client = Client(account_sid, auth_token)

xxx = datetime.datetime.now()
print("Activating Program")
start_message = client.messages.create(
    messaging_service_sid='',   # Enter your Messaging Service ID from Twilio
    body='Program has successfully Activated',
    to=''   # Receiver Mobile number with Country Code
)
print(start_message.sid)
while True:
    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=302&date='
    url = url + str(xxx.day) + '-' + str(xxx.month) + '-' + str(xxx.year)
    response = requests.get(url)
    try:
        locations = response.json()['centers']
    except:
        continue

    for i in locations:
        x = i['sessions']
        for xx in x:
            if xx['available_capacity_dose1'] > 0:
                message = client.messages.create(
                    messaging_service_sid='MG2d51afac03d6c38d303ecebf76d089e9',
                    body='Available Slot in Malappuram',
                    to=''   # Receiver Mobile number with Country Code
                )
                print(message.sid)
                time.sleep(2 * 60)
