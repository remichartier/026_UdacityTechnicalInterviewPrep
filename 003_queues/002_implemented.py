"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    def __init__(self, head=None):
        self.storage = [head]
        self.head_idx = None
        self.tail_idx = None
        if head != None :
            self.head_idx = 0
            self.tail_idx = 0
        else:
            self.head_idx = None
            self.tail_idx = None
        # print self.storage

    def print_queue(self):
        #print self.storage
        pass

    def enqueue(self, new_element):
        self.storage.append(new_element)
        if self.head_idx != None :
            self.tail_idx += 1
        else:
            self.head_idx = 0
            self.tail_idx = 0
        self.print_queue()

    def peek(self):
        if self.head_idx!= None :
            return self.storage[self.head_idx]

    def dequeue(self):
        if self.head_idx != None :
            value = self.storage[self.head_idx]
            self.storage.pop(self.head_idx)
            self.tail_idx -= 1
            self.print_queue()
            if self.tail_idx == -1:
                self.head_idx = None
                self.tail_idx = None 
            return value
    
# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print q.peek()

# Test dequeue
# Should be 1
print q.dequeue()

# Test enqueue
q.enqueue(4)
# Should be 2
print q.dequeue()
# Should be 3
print q.dequeue()
# Should be 4
print q.dequeue()
q.enqueue(5)
# Should be 5
print q.peek()