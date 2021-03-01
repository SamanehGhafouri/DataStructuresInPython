# Queue is FIFO: First in First out
# Enqueue(append()): Add an item to the end of the line
# Dequeue(popleft()): Remove an item from the front of the line
# How to implement: Using built in Deque


from collections import deque
my_queue = deque()
my_queue.append(5)
my_queue.append(10)
print(my_queue)
print(my_queue.popleft())


# *************************** Fun Exercise

class Queue():

    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        else:
            return None

    def __str__(self):
        return str(self.queue)


my_queue1 = Queue()
my_queue1.enqueue(2)
my_queue1.enqueue(4)
my_queue1.enqueue(90)
print("this is ", str(my_queue1))
print(my_queue1.dequeue())
print(my_queue1.dequeue())
print(my_queue1.dequeue())
print(my_queue1.dequeue())




