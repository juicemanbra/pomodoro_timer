import time as t
import datetime as dt
import os
import csv



def notifier(title, text): # this function is used to send a notification to the user
    os.system("""
            osascript -e 'display notification "{}" with title "{}" sound name "Glass"'
            """.format(text, title))


def countdown(interval, type): # with this function we print out a live countdown of the current interval
    while interval:
        mins, secs = divmod(interval, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        t.sleep(1)
        interval -= 1
        print(type, timer, end='\r')# this makes the printout live and replaces the counter with the current 


def pause(length): # this counts down in a pause, either short or long depending on how many intervals
    if length == 'short': # we take here the parameter defined in the work_timer() function
        countdown(pause_interval_s, 'Pause: ') # pause still needs a skip functiom
        
    else:
        countdown(pause_interval_l, 'Pause: ')
    notifier('Break is over!', 'Get back to work!')
    work()


def work(): # this is counting down when working -- still needs a pause function!
    print('To start working, press ENTER.')
    input('')
    print('Press ENTER to pause.')
    global interval_count # have not found a cleaner way to use the variable within this function yet. 
    interval_count += 1
    countdown(work_interval, 'Work: ')
    if (interval_count % 4) == 0:
        p_length = 'long'
        notifier('Pause!','Take a long break!')
    else:
        p_length = 'short'
        notifier('Pause!','Take a short break!')
    pause(p_length)


def savetoCSV(): # this function saves some data to a csv file for future reference/analysis
    fulldt = dt.datetime.now()
    date = f"{fulldt.day}.{fulldt.month}.{fulldt.year}"
    time = "{:02d}:{:02d}".format(fulldt.hour, fulldt.minute)
    outputFile = open('timeLog_v2.csv', 'a', newline='')
    outputWriter = csv.writer(outputFile, delimiter='\t')
    outputWriter.writerow([date, time, task, timeFormat, interval_count, flow_scale])


task = input("Enter task\n") # here we let the user tell us what he's working on
print("To stop working, press Ctrl-C.")
print("To start next interval hit ENTER.")

work_interval = 25 * 60 # time spent working (minutes times seconds)
pause_interval_s = 5 * 60 # time for short pause
pause_interval_l = 20 * 60 # time for long pause
interval_count = 0 # start count of the total intervals
startTime = t.time() # this captures the time, when the user starts the clock

try: # this creates an infinite loop and lets the user end it with ctrl-C
    work()
except KeyboardInterrupt:
        endTime = t.time() # here we capture the time when the user ends the program with ctrl-C
        totalTime = int(endTime - startTime) # this calculates the time between start and end
        mins, secs = divmod(totalTime, 60)   # this makes the time human readable
        timeFormat = "{:02d}:{:02d}".format(mins, secs)  # this makes the time human readable
        print(f"\nWell Done!\nTotal Time: {timeFormat} Intervals: {interval_count}") # this could be a notification in the future
        print("Flow experienced:")
        flow_scale = input("") 
        savetoCSV() 
        


