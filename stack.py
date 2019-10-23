
class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self,value):
        self.stack.append(value)

    def pop(self):
        value = self.peek()
        del self.stack[-1]
        return value

    def peek(self):
        return self.stack[-1]

    def sizeStack(self):
        return len(self.stack)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.sizeStack())
print("poped value is",stack.pop())
print("poped value is",stack.pop())
print("peek ",stack.peek())
print("the size of the stack is",stack.sizeStack())
