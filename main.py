import time as t 
import datetime as dt
import os
import csv


def countdown(interval, type): # this is a simple countdown that displays minutes and seconds
    while interval:
        mins, secs = divmod(interval, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        t.sleep(1)
        interval -= 1
        print(type, timer, end='\r') # takes the type of interval (pasue/work) and the time


def pause():
    pass

def work():
    pass

def savetoCSV():
    pass

def start():
    pass

def notifier(title, text):
        os.system("""
                osascript -e 'display notification "{}" with title "{}" sound name "Glass"'
                """.format(text, title))
    

