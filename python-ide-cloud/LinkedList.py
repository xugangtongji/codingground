# -*- coding: utf-8 -*-
# 节点 链表结构 初始化，插入及其遍历

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:             #具有表头（只有下一个节点的地址没有当前数据）的链表
    def __init__(self):
        self.head = None       #指向地址

    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head   #当前第一个数据
        self.head = NewNode        #指向新数据

    def AtEnd(self,data_in):
        NewNode=Node(data_in)
        p=self.head
        while(p.next):
            p=p.next
        p.next=NewNode
# Function to remove node 类似List的remove功能, 删除固定位置的元素 del a[1] a.pop(0)
    def RemoveNode(self,removekey):
        
        headval=self.head
        
        if headval is None:
            print "This is a kong list"
            return
        
        if headval.data==removekey:
            self.head=headval.next
            return
        
        prev=self.head
        nowhead=self.head
        flag=0
        
        while nowhead is not None:
            if nowhead.data==removekey:
                flag=1
                prev.next=nowhead.next
                break
            prev=nowhead
            nowhead=nowhead.next
        
        if flag==0:
            print "There is no this element!"
            return

    def LenList(self):
        headval=self.head
        lenth=0
        while headval is not None:
            headval=headval.next
            lenth+=1
        return lenth
            
    def InsertNode(self,key,num):         #插入下标从0，1，2...num开始
         headval=self.head
         
         if num>self.LenList():
             print "error insert num!"
             return
         elif num == self.LenList():
             self.AtEnd(key)
             return
         elif num==0:
             self.Atbegining(key)
             return
         
         InNode=Node(key)
         prev=headval
         nowhead=headval

         for i in range (num):         #num 指的是循环次数
             prev=nowhead
             nowhead=nowhead.next
        
         InNode.next=prev.next
         prev.next=InNode
            
        
            
    def LListprint(self):
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next
    

            

llist = SLinkedList()
llist.Atbegining("xugang")
llist.Atbegining("Tue")
llist.Atbegining("Wed")
llist.Atbegining("hell")
llist.RemoveNode("hell")
llist.InsertNode("si",2)
llist.LListprint()
print llist.LenList()