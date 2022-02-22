# Notes singly linked list:
# A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations.
# The elements in a linked list are linked using pointers
# A linked list consists of nodes where each node contains a data field and a reference to the next node in the list.


# Head
# |
# |
# v
##### #####       ##### #####       ##### #####
# A # #   # ----> # B # #   # ----> # C # #   #  ----> NULL
##### #####       ##### #####       ##### #####


class SLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "Object: data={}".format(self.data)

    def get_data(self):
        """Return the atribute"""

        return self.data

    def set_data(self, new_data):
        """Replace the existing value on data with the value of new_data"""

        self.data = new_data

    def get_next(self):
        """Return the atribute"""

        return self.next

    def set_next(self, new_next):
        """Replace the existing value on next with the value of new_next"""

        self.next = new_next


class SLL:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return "Object: head={}".format(self.head)

    def is_empty(self):

        #True if self.head == None else False

        if self.head == None:

            return True
        else:
            return False

    def add_front(self, new_data):
        """Add a node whose data is the new_data to the front of the linked list"""

        temp_node = SLLNode(new_data)
        temp_node.set_next(self.head)
        self.head = temp_node

    def size(self):
        """Traverses the linked list and return the number of nodez in the linked list
           Time complexity: O(N)
        """

        size = 0
        if self.head == None:
            return 0
        else:
            current = self.head
            while current is not None:
                size += 1
                current = current.get_next

            return size

    def search(self, data):
        """Traverse the linked list and find the data if the data appears in the node return true

        Time complexity: O(N)
        """

        if self.head is None:
            return 'No nodes to search in the linked list'

        current = self.head
        while current is not None:
            if current.get_data == data:

                return True
            else:
                current = current.get_next()

        return False

    def remove(self, data):
        """Removes the firts occurence of a node that constains the data argument
        as its data variable. Return nothing.

        Time complexity: O(N)
        """

        if self.head == None:
            return 'Linked list is empty'

        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() == None:
                    return 'A node with data value is not present '
                else:
                    previous = current
                    current = current.get_next()

        if previous is None:
            self.head = current.get_next()

        else:
            previous.set_data(current.get_next())
