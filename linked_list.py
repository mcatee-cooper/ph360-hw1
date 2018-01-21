# padraic mcatee
# hw1 - ph360

class node:
    def __init__(self,initialData):
        self.data = initialData
        self.point = None

    def getData(self):
        return self.data

    def getPoint(self):
        return self.point

    def setData(self,newData):
        self.data = newData

    def setPoint(self,newPoint):
        self.point = newPoint

class linkedList:
    def __init__(self):
        self.head = None
    def add2Head(self,item):
        tmpNode = node(item)
        tmpNode.setPoint(self.head)
        self.head = tmpNode
    def add2Tail(self,item):
        tmpNode = node(item)
        traverse = self.head
        # brings us to tail
        if traverse == None:
            self.add2Head(item)
        else:
            while traverse.getPoint() != None:
                traverse = traverse.getPoint()
            traverse.setPoint(tmpNode)
            tmpNode.setPoint(None)
    def printList(self):
        if self.head == None:
            print('empty list')
        else:
            traverse = self.head
            counter = 0
            while traverse != None:
                print(traverse.getData())
                traverse = traverse.getPoint()
    def addByKey(self,item,key):
        # adds item after specified element
        traverse = self.head
        while traverse != None:
            if traverse.getData() == key:
                tmpNode = node(item)
                tmpNode.setPoint(traverse.getPoint())
                traverse.setPoint(tmpNode)
                break
            else:
                traverse = traverse.getPoint()
    def delByKey(self,key):
        # removes specified element
        traverse = self.head
        while traverse != None:
            if traverse.getData() == key:
                try:
                    priorNode.setPoint(traverse.getPoint())
                except:
                    self.head = self.head.getPoint()
            priorNode = traverse
            traverse = traverse.getPoint()
    def copy(self):
        # returns copy of list
        buffer = linkedList()
        traverse = self.head
        while traverse != None:
            buffer.add2Tail(traverse.getData())
            traverse = traverse.getPoint()
        return buffer
    def reverse(self):
        # returns reversed copy of list
        buffer = linkedList()
        traverse = self.head
        while traverse != None:
            buffer.add2Head(traverse.getData())
            traverse = traverse.getPoint()
        return buffer
