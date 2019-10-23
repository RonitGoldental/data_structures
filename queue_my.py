
class Queue_my:

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        value = self.peek()
        del self.queue[0]
        return value

    def peek(self):
        return self.queue[0]

    def sizeStack(self):
        return len(self.queue)

queue = Queue_my()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print("the size of the queue is", queue.sizeStack())
print("popped value is", queue.dequeue())
print("popped value is", queue.dequeue())
print("peek ", queue.peek())
print("the size of the queue is", queue.sizeStack())
