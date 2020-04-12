import datetime
from playsound import playsound #pip install playsound
import random
hrtime=0
crrampm="am"
if datetime.datetime.now().hour>12:
    hrtime=datetime.datetime.now().hour-12
    crrampm="pm"
print("__Welcome to Alarm Clock__")
print("\nCurrent time is",hrtime,":",datetime.datetime.now().minute,crrampm)
print("\nDo you want to set an alarm ?")
print("1. Yes")
print("2. No, repeat my default alarm") #sets the alarm to the default time
loudsounds=["HouseFireAlarm.wav","LoudAlarm.wav","SchoolBellAlarm.wav"]
lightsounds=["AnalogWatchAlarm.wav","SmokeAlarm.wav"]
run=True
choice=int(input())
alarmHour=0
alarmMinute=0
ring=0
if choice==1:
    print("Please enter in 12 hour format")
    alarmHour=int(input("At what HOUR(H) do you want to wake up ?"))
    alarmMinute=int(input("At what MINUTE(MM) do you want to wake up ?"))
    ampm=str(input("AM or PM?"))
    ring=int(input("Press 1 for a light and peaceful alarm tone and 2 for a loud alarm tone.\n"))
elif choice==2:
    alarmHour=7
    alarmMinute="00"
    ampm="am"
else:
    run=False
    print("Invalid input1")
print("Alarm set for",alarmHour,":",alarmMinute,ampm.lower())
if ampm.lower()=="pm" and alarmHour in {1,2,3,4,5,6,7,8,9,10,11}:
    alarmHour=alarmHour+12
while(run):
    if(alarmHour==datetime.datetime.now().hour and alarmMinute==datetime.datetime.now().minute):
        print("===============================")
        print("Wake Up! Your alarm is ringing!")
        print("===============================")
        if ring==1:
            playsound(random.choice(lightsounds))
        elif ring==2:
            playsound(random.choice(loudsounds))    
        break
print("\n__Exited__")

