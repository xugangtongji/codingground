# -*- coding: utf-8 -*-
#list实现 队列的出队和入队 FIFO

class Queue:

  def __init__(self):
      self.queue = list()
  def size(self):
      return len(self.queue)
      
  def add(self,dataval):
# Insert method to add element
      if dataval not in self.queue:
          self.queue.insert(0,dataval)
          return True
      return False
# Pop method to remove element
  def remove(self):
      if len(self.queue)>0:
          return self.queue.pop()
      return ("No elements in Queue!")

TheQueue = Queue()
TheQueue.addtoq("Mon")
TheQueue.addtoq("Tue")
TheQueue.addtoq("Wed")
print(TheQueue.size())