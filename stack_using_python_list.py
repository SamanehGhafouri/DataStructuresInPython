# Stack using Python List
# Stack is a LIFO data structure -- last in, first out.
# Use append() to push an item onto the stack.
# Use pop() to remove an item.

my_stack = list()
my_stack.append(4)
my_stack.append(7)
my_stack.append(12)
my_stack.append(19)
print(my_stack)
print(my_stack.pop())
print(my_stack.pop())
print(my_stack)

# *********************************** Stack using List with a Wrapper Class


class Stack():
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None

    def __str__(self):
        return str(self.stack)


# Test code for the class
my_stack1 = Stack()
my_stack1.push(1)
my_stack1.push(3)
print('my stack', my_stack1)
print(my_stack1.pop())
print(my_stack1.peek())
print(my_stack1.pop())
print(my_stack1.pop())

