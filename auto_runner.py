from main import selftest
import datetime
from datetime import date
from time import sleep

print("--------autorunner start--------")

while 1:
    dt = datetime.datetime.now()
    if (dt.hour == 6 and dt.minute == 00 and dt.second == 00):
        print(dt.hour, dt.minute, dt.second)
        selftest()
        print("자가진단성공")
        print("=======================")
        sleep(20)