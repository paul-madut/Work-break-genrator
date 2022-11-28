# Code Written by Paul Madut and is not to be used by any other entity

import datetime
class Worker:
    def __init__(self, name, startTime, endTime):
        self.name = name
        self.start = startTime
        self.end = endTime

        self.break1 = None
        self.break2 = None
        self.lunch = None

        self.lastBreak = startTime

    def __str__(self):
        return f"{self.name}      {self.break1}     {self.lunch}     {self.break2}"

Employees =['Bob A',
            'Paul M']

Employees2 = ["{}. {}".format(x+1,Employees[x]) for x in range(len(Employees))]
WorkingToday = []
WorkingToday2 = []
breakConflicts = []


def BreakLength(shiftLength):
    if shiftLength <= 5:
        return 15
    elif shiftLength <=6.5:
        return 30
    elif shiftLength <= 8:
        return 45
    elif shiftLength > 8:
        return 60

def ShiftLength(startTime, endTime):
    delta  = (endTime - startTime).total_seconds()
    delta /= 60*60
    return delta

def MakeBreaks(currWorker,breakLength):
    if breakLength == 0:
        return

    elif breakLength >= 60:
        currWorker.break1 = True
        MakeBreaks(currWorker, breakLength - 15)

    elif breakLength >= 30:
        if currWorker.break1 == None:
            currWorker.lunch = True
        else:
            currWorker.lunch = True
        MakeBreaks(currWorker, breakLength - 30)

    elif breakLength <= 15:

        if currWorker.break1 == None:
            currWorker.break1 = True
        else:
            currWorker.break2 = True
        MakeBreaks(currWorker,breakLength-15)

def BreakOrder(Worker):
    if Worker.start.time() >= datetime.time(12,0) and Worker.break1 == True and Worker.break2 == None:
        Worker.break1 = None
        Worker.break2 = True


def amPm(formattedTime):
    time_format = "%H:%M%p"
    time = datetime.datetime.strptime(formattedTime, time_format)
    if "pm" in formattedTime and time.hour != 12:
        time += datetime.timedelta(hours=12)
    return time

def breakTimes(Worker):
    # Break 1
        if type(Worker.break1) == bool and Worker.break1 and Worker.lastBreak + datetime.timedelta(hours=2) not in breakConflicts:
            Worker.break1 = Worker.lastBreak + datetime.timedelta(hours=2)
            Worker.lastBreak = Worker.break1
            for x in range(15):
                breakConflicts.append(Worker.break1 + datetime.timedelta(minutes = x))
        elif type(Worker.break1) == bool and Worker.break1 and Worker.lastBreak + datetime.timedelta(hours=2) in breakConflicts:
            Worker.break1 =Worker.lastBreak + datetime.timedelta(hours=2) + datetime.timedelta(minutes=15)
            Worker.lastBreak = Worker.break1
            for x in range(15):
                breakConflicts.append(Worker.break1 + datetime.timedelta(minutes=x))

        # Break 2
        if type(Worker.break2) == bool and Worker.break2 and Worker.lastBreak + datetime.timedelta(hours=2) not in breakConflicts:
            Worker.break2 = Worker.lastBreak + datetime.timedelta(hours=2)
            Worker.lastBreak = Worker.break2
            for x in range(15):
                breakConflicts.append(Worker.break2 + datetime.timedelta(minutes = x))
        elif type(Worker.break2) == bool and Worker.break2 and Worker.lastBreak + datetime.timedelta(hours=2) in breakConflicts:
            Worker.break2 =Worker.lastBreak + datetime.timedelta(hours=2) + datetime.timedelta(minutes=15)
            Worker.lastBreak = Worker.break2
            for x in range(15):
                breakConflicts.append(Worker.break2 + datetime.timedelta(minutes=x))

        # Lunch
        if type(Worker.lunch) == bool and Worker.lunch and Worker.lastBreak + datetime.timedelta(hours=2) not in breakConflicts:
            Worker.lunch = Worker.lastBreak + datetime.timedelta(hours=2)
            Worker.lastBreak = Worker.lunch
            for x in range(30):
                breakConflicts.append(Worker.lunch + datetime.timedelta(minutes = x))
        elif type(Worker.lunch) == bool and Worker.lunch and Worker.lastBreak + datetime.timedelta(hours=2) in breakConflicts:
            Worker.lunch =Worker.lastBreak + datetime.timedelta(hours=2) + datetime.timedelta(minutes=15)
            Worker.lastBreak = Worker.lunch
            for x in range(30):
                breakConflicts.append(Worker.lunch + datetime.timedelta(minutes=x))



        return


"""
flag = True
print("Welcome to the Schedule Maker 2000! \n To exit the program type -1")
counter = 0

while(flag):
    worker = int(input("Who is working today? "))
    if worker == -1:
        break
    else:
        WorkingToday.append(Employees[worker-1])
        del Employees2[worker-1]
    startTime  = input("What time do they start? (hh:mm): ")
    startTime = datetime.datetime.strptime(startTime, time_format)
    endTime  = input("What time do they end? (hh:mm): ")
    endTime = datetime.datetime.strptime(endTime, time_format)


    WorkingToday2.append(Worker(Employees[worker-1],startTime,endTime))



    MakeBreaks(WorkingToday2[counter],BreakLength(ShiftLength(startTime,endTime)))
    BreakOrder(WorkingToday2[counter])
    counter+=1
"""

startTime  = "2:00pm"
startTime = amPm(startTime)
endTime  = "4:30pm"
endTime = amPm(endTime)

WorkingToday2.append(Worker("bob a",startTime,endTime))
MakeBreaks(WorkingToday2[0],BreakLength(ShiftLength(startTime,endTime)))
BreakOrder(WorkingToday2[0])
breakTimes(WorkingToday2[0])

for x in breakConflicts:
    print(x)
print("----------------------------------")


startTime1  = "1:00pm"
startTime1 = amPm(startTime1)
endTime1  = "6:30pm"
endTime1 = amPm(endTime1)


WorkingToday2.append(Worker("pete c",startTime1,endTime1))
MakeBreaks(WorkingToday2[1],BreakLength(ShiftLength(startTime1,endTime1)))
BreakOrder(WorkingToday2[1])
breakTimes(WorkingToday2[1])

for x in breakConflicts:
    print(x)

for x in WorkingToday2:
     print(x)


