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


def pause(p_length): # takes the length of the pause as parameter
    print(f'Let\'s take a {p_length} break!')
    input('')
    if p_length == 'short':
        countdown(pause_interval_s)
    else: 
        countdown(pause_interval_l)
    

def work():
    input('')
    global interval_count
    interval_count += 1
    countdown(work_interval, 'Work')

    if (interval_count % 4) == 0:
        p_length = 'long'
    else:
        p_length = 'short'

    notifier('Pause!', f'Take a {p_length} break')
    pause(p_length)


def savetoCSV(): # this functions saves some data to a csv file
    fulldt = dt.datetime.now()
    date = f"{fulldt.day}.{fulldt.month}.{fulldt.year}" # date
    time = "{:02d}:{:02d}".format(fulldt.hour, fulldt.minute) #  current time
    outputFile = open('log.csv', 'a', newline='')
    outputWriter = csv.writer(outputFile, delimiter='\t')
    outputWriter.writerow([date, time, task, timeFormat, interval_count, flow_scale]) # task, how many intervals and the flow experienced

def start():
    print('This is a timer for flow&productivity!)
    task = input('Enter task:\n>')
    print("To start the next interval hit ENTER")


    


def notifier(title, text):
        os.system("""
                osascript -e 'display notification "{}" with title "{}" sound name "Glass"'
                """.format(text, title))
    



work_interval = 5 # seconds times minutes
pause_interval_s = 2 # short pause
pause_interval_l = 3 # long pause (after 4 intervals)
interval_count = 0
startTime = t.time() # the time we started working


start()

try:
    work()
except KeyboardInterrupt:
    endTime = t.time() # here we capture the time when the user ends the program with ctrl-C
    totalTime = int(endTime - startTime) # this calculates the time between start and end
    mins, secs = divmod(totalTime, 60)   # this makes the time human readable
    timeFormat = "{:02d}:{:02d}".format(mins, secs)  # this makes the time human readable
    print(f"\nWell Done!\nTotal Time: {timeFormat} Intervals: {interval_count}") # this could be a notification in the future
    flow = input("Flow experienced: ")
    savetoCSV()
