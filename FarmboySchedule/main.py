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

    def __str__(self):
        return f"{self.name}      {self.break1}     {self.lunch}     {self.break2}"

Employees =['Maricel W','Prabh k','Abigail D',
            'Emer L','Troy M','Marissa B',
            'Salma H','Bessan A','Nour B',
            'Salma Z','Ewen J','Jeannice D',
            'Jopeph P','Annalyn F','Mariceli C',
            'Dragan K-K','Annabelle B','Lauren G',
            'Paul M']

Employees2 = ["{}. {}".format(x+1,Employees[x]) for x in range(len(Employees))]
WorkingToday = []
WorkingToday2 = []


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
    print(breakLength)
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
    if Worker.start.time() <= datetime.time(12,0) and Worker.break1 == True and Worker.break2 == None:
        Worker.break1 = None
        Worker.break2 = True


time_format = "%H:%M%p"
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

for x in WorkingToday2:
    print(x)