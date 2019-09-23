import time
import random
import queue

class Printer():
  def __init__(self,pagePerMin):
    self.busy = False
    self.task = None
    self.pagePerMin = pagePerMin
    self.simTimePerPage = 60 / pagePerMin
    self.completedTask = []

  def getCurrentTask(self):
    # Retruns current task that printer is working on
    return self.task

  def assignNewTask(self, task, simTime):
    #assigns new task to printer for printing and does resultant assignments
    self.task = task
    self.busy = True
    self.task.startTask(simTime)

  def endCurrentTask(self, simTime):
    # ends current task assigned to printer and does resultant assignments
    self.task.endTask(simTime)
    self.completedTask.append(self.task)
    self.task = None
    self.busy = False
    
  def addToCompletedTask(self, task):
    # saves completed task in a list for future analytics calculations
    self.completedTask.append(task)

class Task():
  def __init__(self, simTime):
    self.createTime = simTime
    self.startTime = None
    self.endTime = None
    self.pages = random.randrange(1,21)

  def endTask(self, simTime):
    self.endTime = simTime

  def startTask(self, simTime):
    self.startTime = simTime

  def waitTime(self):
    # returns time it took for task from creation to execution
    return self.startTime - self.createTime

def createTask():
  x = random.randrange(1,181) == 50
  return x

printQ = queue.Queue()
printer = Printer(pagePerMin=5)
for simTime in range(3600):
  if createTask():
    t = Task(simTime)
    printQ.put(t)

    if printer.busy:
      ct = printer.getCurrentTask()
      if simTime > ct.startTime + ct.pages * printer.simTimePerPage:
        printer.endCurrentTask(simTime)

    if not printer.busy:
      printer.assignNewTask(printQ.get(), simTime)