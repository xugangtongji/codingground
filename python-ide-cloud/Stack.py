# -*- coding: utf-8 -*-

#使用list实现堆栈 push pop lenth peektop
class Stack:

    def __init__(self):
        self.stack = []
    
    def lenth(self):
        return len(self.stack)
    
    
    def push(self, dataval):
# Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
# Use list pop method to remove element
    def pop(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()
# Use peek to look at the bottom of the stack

    def peekBottom(self):     
	    return self.stack[0]
    def peekTop(self):     
	    return self.stack[self.lenth()-1]

AStack = Stack()
AStack.push("Mon")
AStack.push("Tue")
AStack.push("Wed")
AStack.push("Thu")
print AStack.pop()
print (AStack.peekTop())