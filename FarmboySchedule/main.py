# Code Written by Paul Madut and is not to be used by any other entity

import datetime
from twilio.rest import Client
import sqlite3
import Constants

# Twilio Api
# Fill in auth_token with you actual auth token
account_sid = 'AC48f54b1fc2e0f214851b67e491c1be88'
auth_token = '[Redacted]'
client = Client(account_sid, auth_token)

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
        if self.break1 == None:
            self.break1 = ""
        if self.break2 == None:
            self.break2 = ""
        if self.lunch == None:
            self.lunch = ""

        text = "{} |{:<16}|{:^16}|{:>16}"
        return text.format(self.name,self.break1,self.lunch,self.break2)

    def MakePretty(self)-> None:
        time_format = "%H:%M%p"

        if self.break1 != None:
            break1End = self.break1 + datetime.timedelta(minutes = Constants.BREAKLENGTH)
            self.break1 = datetime.datetime.strftime(self.break1, time_format)
            break1End = datetime.datetime.strftime(break1End, time_format)
            break1End = amPm(break1End)
            break1End= amPm2(break1End)
            self.break1 = amPm(self.break1)
            self.break1 = amPm2(self.break1)

            self.break1 = str(self.break1) + "|" + str(break1End)

        if self.break2 != None:
            break2End = self.break2 + datetime.timedelta(minutes = Constants.BREAKLENGTH)
            self.break2 = datetime.datetime.strftime(self.break2, time_format)
            break2End = datetime.datetime.strftime(break2End, time_format)
            break2End = amPm(break2End)
            break2End = amPm2(break2End)
            self.break2 = amPm(self.break2)
            self.break2 = amPm2(self.break2)

            self.break2 = str(self.break2) + "|" + str(break2End)

        if self.lunch != None:
            lunchEnd = self.lunch + datetime.timedelta(minutes = Constants.LUNCHLENGTH)
            self.lunch = datetime.datetime.strftime(self.lunch, time_format)
            lunchEnd = datetime.datetime.strftime(lunchEnd, time_format)
            lunchEnd = amPm(lunchEnd)
            lunchEnd = amPm2(lunchEnd)
            self.lunch = amPm(self.lunch)
            self.lunch = amPm2(self.lunch)

            self.lunch = str(self.lunch) + "|" + str(lunchEnd)



WorkingToday = []
WorkingToday2 = []
breakConflicts = []

# database things
connection = sqlite3.connect("employees.db")

cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Employees(
number INTEGER,
name TEXT
)
""")
"""
cursor.execute("""
#INSERT INTO Employees VALUES
""" +
               employeeInfo

)
"""
cursor.execute("""
SELECT * FROM Employees
""")
rows = cursor.fetchall()

Employees2 = ["{}. {}".format(rows[x][0],rows[x][1]) for x in range(len(rows))]
Employees = [x for x in Employees2]

connection.commit()
connection.close()

def BreakLength(shiftLength:int)-> int:
    if shiftLength <= 5:
        return Constants.BREAKLENGTH
    elif shiftLength <=6.5:
        return Constants.LUNCHLENGTH
    elif shiftLength <= 8:
        return 45
    elif shiftLength > 8:
        return 60

def ShiftLength(startTime:datetime, endTime:datetime)-> int:
    delta  = (endTime - startTime).total_seconds()
    delta /= 60*60
    return delta

def MakeBreaks(currWorker:Worker,breakLength:int)->None:
    if breakLength == 0:
        return

    elif breakLength >= 60:
        currWorker.break1 = True
        MakeBreaks(currWorker, breakLength - Constants.BREAKLENGTH)

    elif breakLength >= 30:
        if currWorker.break1 == None:
            currWorker.lunch = True
        else:
            currWorker.lunch = True
        MakeBreaks(currWorker, breakLength - Constants.LUNCHLENGTH)

    elif breakLength <= 15:

        if currWorker.break1 == None:
            currWorker.break1 = True
        else:
            currWorker.break2 = True
        MakeBreaks(currWorker,breakLength-Constants.BREAKLENGTH)

def BreakOrder(worker:Worker)-> None:
    if worker.start.time() >= datetime.time(12,0) and worker.break1 == True and worker.break2 == None:
        worker.break1 = None
        worker.break2 = True


def amPm(formattedTime:str)-> datetime:
    time_format = "%H:%M%p"
    time = datetime.datetime.strptime(formattedTime, time_format)
    if "pm" in formattedTime and time.hour != 12:
        time += datetime.timedelta(hours=12)
    return time

def amPm2(unformattedTime:datetime)-> str:
    time_format = "%H:%M%p"
    time = datetime.datetime.strftime(unformattedTime, time_format)
    if unformattedTime.hour > 12:
        unformattedTime += datetime.timedelta(hours=12)
        time = datetime.datetime.strftime(unformattedTime, time_format)
        time= time.replace("AM","PM")
    return time

def breakTimes(worker:Worker)-> None:
    # Break 1
        if type(worker.break1) == bool and worker.break1 and worker.lastBreak + datetime.timedelta(hours=2) not in breakConflicts:
            worker.break1 = worker.lastBreak + datetime.timedelta(hours=2)
            worker.lastBreak = worker.break1
            for x in range(15):
                breakConflicts.append(worker.break1 + datetime.timedelta(minutes = x))
        elif type(worker.break1) == bool and worker.break1 and worker.lastBreak + datetime.timedelta(hours=2) in breakConflicts:
            worker.break1 =worker.lastBreak + datetime.timedelta(hours=2) + datetime.timedelta(minutes=Constants.BREAKLENGTH)
            worker.lastBreak = worker.break1
            for x in range(15):
                breakConflicts.append(worker.break1 + datetime.timedelta(minutes=x))

        # Break 2
        if type(worker.break2) == bool and worker.break2 and worker.lastBreak + datetime.timedelta(hours=2) not in breakConflicts:
            worker.break2 = worker.lastBreak + datetime.timedelta(hours=2)
            worker.lastBreak = worker.break2
            for x in range(15):
                breakConflicts.append(worker.break2 + datetime.timedelta(minutes = x))
        elif type(worker.break2) == bool and worker.break2 and worker.lastBreak + datetime.timedelta(hours=2) in breakConflicts:
            worker.break2 =worker.lastBreak + datetime.timedelta(hours=2) + datetime.timedelta(minutes=Constants.BREAKLENGTH)
            worker.lastBreak = worker.break2
            for x in range(15):
                breakConflicts.append(worker.break2 + datetime.timedelta(minutes=x))

        # Lunch
        if type(worker.lunch) == bool and worker.lunch and worker.lastBreak + datetime.timedelta(hours=2) not in breakConflicts:
            worker.lunch = worker.lastBreak + datetime.timedelta(hours=2)
            worker.lastBreak = worker.lunch
            for x in range(30):
                breakConflicts.append(worker.lunch + datetime.timedelta(minutes = x))
        elif type(worker.lunch) == bool and worker.lunch and worker.lastBreak + datetime.timedelta(hours=2) in breakConflicts:
            worker.lunch = worker.lastBreak + datetime.timedelta(hours=2) + datetime.timedelta(minutes=Constants.LUNCHLENGTH)
            worker.lastBreak = worker.lunch
            for x in range(30):
                breakConflicts.append(worker.lunch + datetime.timedelta(minutes=x))
        return



flag = True
print("Welcome to the Schedule Maker 2000! \n To exit the program type -1")
counter = 0

while(flag):
    for x in Employees2:
        print(x)
    try:
        worker = int(input("Who is working today? "))
    except Exception:
        print("Please enter a valid employee")
        continue


    if worker == -1:
        break
    else:
        try:
            WorkingToday.append(Employees2[worker-1])
            del Employees2[worker - 1]
        except IndexError:
            print("Enter a valid employee")
            continue

    try:
        startTime  = str(input("What time do they start? (hh:mm): "))
        startTime = amPm(startTime)
    except Exception:
        print("Please enter a start valid time")
        continue

    try:
        endTime  = str(input("What time do they end? (hh:mm): "))
        endTime = amPm(endTime)
    except Exception:
        print("Please enter a endTime valid time")
        continue

    WorkingToday2.append(Worker(Employees[worker-1],startTime,endTime))
    MakeBreaks(WorkingToday2[counter],BreakLength(ShiftLength(startTime,endTime)))
    BreakOrder(WorkingToday2[counter])
    breakTimes(WorkingToday2[counter])
    counter+=1

for x in WorkingToday2:
    x.MakePretty()
    print(x)
    """
    message = client.messages.create(
        messaging_service_sid='MG835442ee15df88dd2018d4a8c1c04b29',
        body=x,
        to='+16139814476'
    )
    """
