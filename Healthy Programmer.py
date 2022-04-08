# Healthy Programmer
"""
A Programmer sits on laptop for long hours.
This program take care of 3 basic health related things:
1. Water
2. Eyes
3. Physical health

This program reminds him for:
1. Drinking water every 35 mins
2. Doing eye exercise every 25 mins
3. Doing some physical exercise every 45 mins

It will work during office hours (9:00am to 5:00pm)
"""


from datetime import datetime
from datetime import timedelta
from pygame import mixer

def drink_water():
    for dt in datetime_range(timedelta(hours=9, minutes=0), timedelta(hours=23, minutes=0), timedelta(minutes=35)):
        dt1 = str(dt)
        if now1 == dt1:
            mixer.music.load("water.mp3")
            print("Drink Water")
            mixer.music.play(-1)
            input("Enter 'Drank' when your finished\n")
            f1 = open("Healthy_log.txt", "a")
            f1.write('Drank Water at: ' + '[' + str(getdate()) + ']\n')
            mixer.music.stop()
            f1.close()
            break

def eyes_exr():
    # Eye Exercise Remainder
    for et in datetime_range(timedelta(hours=9, minutes=0), timedelta(hours=23, minutes=0), timedelta(minutes=25)):
        et1 = str(et)
        if now1 == et1:
            mixer.music.load("eyes.mp3")
            print("Rest your eyes")
            mixer.music.play(-1)
            input("Enter 'Eydone' when your finished\n")
            f2 = open("Healthy_log.txt", "a")
            f2.write('Did Eye Exercise at: ' + '[' + str(getdate()) + ']\n')
            mixer.music.stop()
            f2.close()
            break

def physical_ex():
    # Physical Exercise Remainder
    for pt in datetime_range(timedelta(hours=9, minutes=0), timedelta(hours=23, minutes=0), timedelta(minutes=45)):
        pt1 = str(pt)
        if now1 == pt1:
            mixer.music.load("physical.mp3")
            print("Do Physical Exercise")
            mixer.music.play(-1)
            input("Enter 'Exdone' when your finished\n")
            f3 = open("Healthy_log.txt", "a")
            f3.write('Did Physical Exercise at: ' + '[' + str(getdate()) + ']\n')
            mixer.music.stop()
            f3.close()
            break

def datetime_range(start, end, delta):
    current = start
    while current < end:
        yield current
        current += delta
def getdate():
    import datetime
    return datetime.datetime.now()

if __name__ == "__main__":
    now = datetime.now()
    mixer.init()

    while(now.hour>=9 and now.hour<=23):
        now = datetime.now()
        now1 = now.strftime("%H:%M:%S")
        drink_water()
        eyes_exr()
        physical_ex()