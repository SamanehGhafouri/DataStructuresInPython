# Linked List in python
# Node class
# Node class has a constructor that sets the data passed in, and optionally
# and prev_node
# It also has a str method to give a string representation for printing.
# Note that prev_node is only used for Doubly Linked Lists.
# Operations: Add, Find, Remove, Print_list


class Node:

    def __init__(self, d, n=None, p=None):

        self.data = d
        self.next_node = n
        self.prev_node = p

    def __str__(self):
        return '(' + str(self.data) + ')'


class LinkedList:

    def __init__(self, r=None):

        self.root = r
        self.size = 0

    def add(self, d):

        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def find(self, d):

        this_node = self.root

        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
        return None

    def remove(self, d):

        this_node = self.root
        prev_node = None

        while this_node is not None:

            if this_node.data == d:

                if prev_node is not None:
                    prev_node.next_node = this_node.next_node

                else:
                    self.root = this_node.next_node
                self.size -= 1
                return True

            else:

                prev_node = this_node
                this_node = this_node.next_node

        return False

    def print_list(self):

        this_node = self.root
        while this_node is not None:
            print(this_node, end='->')
            this_node = this_node.next_node
        print('None')


my_list = LinkedList()
my_list.add(5)
my_list.add(8)
my_list.add(12)
my_list.print_list()

print("size="+str(my_list.size))
my_list.remove(8)
print("size="+str(my_list.size))
print(my_list.find(5))
print(my_list.root)



