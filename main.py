import time as t 
import datetime as dt
import os
import csv

def countdown(interval, type):
    while interval:
        mins, secs = divmod(interval, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        t.sleep(1)
        interval -= 1
        print(type, timer, end='\r')


