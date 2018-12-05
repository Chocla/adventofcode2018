import datetime
from collections import defaultdict

f = open('input.txt','r')
entries = f.read().splitlines()
entries.sort()

guards = defaultdict(float)
for e in entries:
    if e[19] == "G":
        #print e
        guard = e.split("#")[1].split(" ")[0]
        i = 0
        continue
    if i % 2 == 0:
        sleepTime =  datetime.datetime.strptime(e[1:17], "%Y-%m-%d %H:%M")
        #print sleepTime.hour
    else:
        wakeTime = datetime.datetime.strptime(e[1:17], "%Y-%m-%d %H:%M")
        guards[guard] +=  (wakeTime - sleepTime).total_seconds() / 60
        
        #print datetime.timedelta(sleepTime, wakeTime)
    i += 1
#print guards
maxTime = 0.0
for g in guards:
    #print guards[g] > 0.0
    if guards[g] > maxTime:
        maxTime = guards[g]
        maxGuard = g
#Check only the correct guard's times for minutes
minutes = defaultdict(int)
for e in entries:
    if e[19] == "G":
        if e.split("#")[1].split(" ")[0] == maxGuard:
            correctGuard = True
        else:
            correctGuard = False
        i = 0
        continue
    if correctGuard and i % 2 == 0:
        start = datetime.datetime.strptime(e[1:17], "%Y-%m-%d %H:%M")
    if correctGuard and i % 2 != 0:
        end = datetime.datetime.strptime(e[1:17], "%Y-%m-%d %H:%M")
        delta = int((end - start).total_seconds() / 60)
        startMinute = start.minute
        endMinute = end.minute
        #print start, end
        for i in range(delta-1):
            minutes[(startMinute+i)%60] += 1
        #for each minute between start and end
            # increment that minute's counter 
        #print startMinute, range(delta+1)
    i += 1
maxCount = 0

for m in minutes:
    if minutes[m] > maxCount:
        maxMinute = m
        maxCount = minutes[m]
print int(maxGuard),maxMinute#,minutes
#87789 too low
#92291 too low