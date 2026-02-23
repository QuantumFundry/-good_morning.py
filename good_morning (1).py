#Good morning sir
from datetime import datetime
hour = datetime.now().hour
wishing_time = hour

if wishing_time < 12:
    print("Good 😊 Morning Sir!")

elif 12  <= wishing_time > 16:
    print("Good 😊 Afternoon sir")
else:
    print("Good Evening🌆 Sir")
