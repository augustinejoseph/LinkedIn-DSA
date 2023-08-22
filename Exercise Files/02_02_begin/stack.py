class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return not self.items
    
    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def __str__(self):
        return str(self.items)
    
    
if __name__ == "__main__":
    stack = Stack()
    print(stack)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack)
    print(stack.peek())
    stack.pop()
    print(stack)
    print(stack.peek())
    stack.pop()
    print(stack)
    print(stack.peek())
    stack.pop()
    print(stack)
    print(stack.is_empty())
 