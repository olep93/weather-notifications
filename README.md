weather-notifications
=====================

A program written in Python to send text messages every x hours notifying you about the weather in your chosen area. First python project I made on my own. 

Through BeautifulSoup, Twilio, requests, time and regex, the program will text what location it's reporting the weather for, what time and date it is, degrees, the felt degrees + what time it counts for. It uses the site "www.yr.no", a very precise and concise Norwegian weather site.

Construct a Messages class. Messages class takes one argument, self.number. The class is fully automated, all it requires is the usage of the class method send_text().

It's also controlled by time, so if time is < 9 AM or > 23:30, it wont run.


Enjoy
