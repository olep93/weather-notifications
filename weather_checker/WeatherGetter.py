from twilio.rest import TwilioRestClient
from bs4 import BeautifulSoup
import requests
import time
import re

__author__ = "Ole Petter Kristiansen"
__copyright__ = "Copyright (C) 2004 Ole Petter Kristiansen"
__license__ = "http://www.wtfpl.net/about/"
__version__ = "1.0"

class Weather:
    
    # uses beautifulsoup to scrape the necessary attribute, in this case temperature
    # felt temperature and what time it's for. 
    @staticmethod
    def get_degrees():
        browser = requests.get("http://www.yr.no/sted/Norge/Buskerud/Hurum/S%C3%B8ndre_Storsand/")
        degrees = browser.text #get string from HTML above
        soup = BeautifulSoup(degrees)
        current_weather = soup('td', {'class' : 'temperature'})[0]['title']
        #scrape to necessary attributes
        return current_weather

    
    # uses beautifulsoup to scrape to location in the HTML, then returns that string
    # regex and decoding was necessary due to norwegian letters and HTML formatting
    @staticmethod
    def get_location():
        browser = requests.get("http://www.yr.no/sted/Norge/Buskerud/Hurum/S%C3%B8ndre_Storsand/")
        degrees = browser.text #get string from HTML above
        soup = BeautifulSoup(degrees)
        current_weather = soup('td', {'class' : 'temperature'})[0]['title']

        location = soup.find('div', class_="yr-content-title clearfix")
        loca = soup.find_all("h1")
        location_string = re.sub('<[^>]*>', '', str(loca))

        return location_string.decode('utf-8')

class Message(Weather):
    """A text messaging service using its parent class to fetch weather reports
       in an area specified"""
    
    def __init__(self, mobile_number):
        self.number = mobile_number

    # the method that will use the constructed argument number and twilio to send
    # a text containing weather, location and time.
    def send_text(self):
        current_time = time.strftime("%H:%M:%S")
        current_date = time.strftime("%d/%m/%Y")

        account_sid = "Your Twilio sid here"
        auth_token  = "Your Twilio auth token here"
        client = TwilioRestClient(account_sid, auth_token)
        message = client.messages.create(
            body = self.get_location() + "\nTid og Dato: " + current_time + ", " + current_date + "\n" + self.get_degrees() + "\n\n\nMvh Ole Petter!",
            to = self.number,
            from_= "Twilio phone number here")
        try:
            message.sid #send msg
            print("Message sent to {}.".format(self.number))

        except twilio.TwilioRestException as e:
            print e
        
            
            
