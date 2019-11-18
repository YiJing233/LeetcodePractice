class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.head, self.tail = -1, -1
        self.vec = [None for _ in range(k)]

        
    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull(): return False
        self.head -= 1
        if self.head < 0:
            self.head = len(self.vec)-1
        self.vec[self.head] = value
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.tail += 1
        if self.tail == len(self.vec):
            self.tail = 0
        self.vec[self.tail] = value
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.vec[self.head] = None
        self.head += 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty(): return False
        self.vec[self.tail] = None
        self.tail -= 1
        return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        print(self.head, len(self.vec))
        return self.vec[self.head]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.vec[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        for x in self.vec:
            if x != None:
                return False
        return True

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        for x in self.vec:
            if x == None:
                return False
        return True


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()



'''
一个并不复杂的双端队列题目
用双端队列来存储元素
判断队列是否为空、是否已满，只要分别判断数组的长度是否为0、等于k即可
添加、删除元素时要分别判断队列是否已满、为空
'''
