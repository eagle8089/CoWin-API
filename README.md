# CoWin-API

Hi, I have created automated system to detect the availability of COVID-19 vaccine shots and send an SMS Alert to your Phone.

This code is utilizing 2 APIs and external accounts:

 1. Co-WIN Public API (https://apisetu.gov.in/public/marketplace/api/cowin)
 2. Twilio API and Account (https://www.twilio.com/)
 3. Heroku Cloud Hosting (https://www.heroku.com/home)

## How to run

 - Before starting, We need a code editor. While a notepad works fine, I suggest you go for a dedicated code editor like Visual Studio Code (https://code.visualstudio.com/download) or PyCharm (https://www.jetbrains.com/pycharm/download/).
 - Next create a free account over at Twilio (https://www.twilio.com/try-twilio) for sending the SMS. (Free accounts can only send SMS to verified phone numbers, So verify your number in the Twilio portal).
 - Its now time to edit the code and add your credentials into it. The locations are marked in the code. (Twilio credentials are available from its dashboard).
 - At line 20, The URL is " https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=302&date= " here district_id is set to filter by Districts, set this ID to your district ID. See the end of this page to know how to find your district ID.
 - AAt line 32, *available_capacity_dose1* can we changed to *available_capacity_dose2* depending on your requirement.
 - Save your code, Its time to RUN it!!!

**At this point you can run this code in your system and everything will work fine**

Now, We can't keep  our PC running 24x7 for this right?
So, Follow these steps:

 - We can host this code on a free cloud provider like Heroku. For this first create a free account in Heroku (https://signup.heroku.com/).
 - Once ready, create a new app in the Heroku Dashboard. Give a nice name and we are ready...
 - Heroku gives excellent explanation on how to deploy your files onto it, So I am going to skip it.
 - Noticed the Procfile? The file with no extension? It is to let the Heroku server know of what to do with you code. Once your code is deployed, Go to your resources tab in Heroku Dashboard. Here you will see a worker under the free Dynos. Activate it.

**Vola! Your Program is now up and running **

## Finding your District ID using API calls
You have to send a few simple API calls using your browser to find you district ID.

 - Run this API call to get your State ID first : https://cdn-api.co-vin.in/api/v2/admin/location/states . You will get the state ID like this "{"state_id":17,"state_name":"Kerala"}". Keep this ID
 - un this API call to get your District ID : https://cdn-api.co-vin.in/api/v2/admin/location/districts/< State ID > **Replace the < State ID > with your ID like this : https://cdn-api.co-vin.in/api/v2/admin/location/districts/17 .**
 - You will get all the District IDs, get your District ID from here...
