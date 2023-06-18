class Stack:
    """
    Stack is a data structure that follows the LIFO (Last In First Out) principle.
    It has the following methods:
    - isEmpty: checks if the stack is empty
    - push: adds an item to the top of the stack
    - pop: removes and returns the item at the top of the stack
    - peek: returns the item at the top of the stack without removing it
    - size: returns the number of items in the stack
    """
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)



# a driver program for class Stack
if __name__ == '__main__':
    
    data_in = ['hello', 'how', 'are', 'you']
    s = Stack()
    for i in data_in:
        s.push(i)
           
    assert s.size() == len(data_in)
    assert s.peek() == data_in[-1]
    data_out = []
    while not s.isEmpty():
        data_out.append(s.pop())
    assert data_out == data_in[::-1]
    assert s.size() == 0
    assert s.peek() == None