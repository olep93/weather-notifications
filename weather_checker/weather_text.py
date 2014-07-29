import WeatherGetter
import time
import datetime

text_YourName = WeatherGetter.Message("Number to text here") #initialize a message object, with my own number as it's argument


# an infinite loop, containing an if expression checking what time it is,
# if time is past 23:30 or pre 9 am, it won't run.

# time initializers were put inside the loop so it continually checks it
# this lets the program run seamless (could be used as a daemon on a server)
while True:
    now = datetime.datetime.now()
    now_time = now.time()
    if datetime.time(9,00) <= now_time <= datetime.time(23,30):
        text_YourName.send_text()
        time.sleep(2*60*60)
    else:        
        print "Time is either before 9 or after 23.30. Texts will not be sent at this hour."
        time.sleep(2*60*60)    
