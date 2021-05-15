# Doubly linked list:
# A Doubly Linked List contains an extra pointer, typically called previous pointer,
# together with next pointer and data which are there in singly linked list.

# Head
# |
# |
# v
##### ##### #####         ##### ##### #####        ##### ##### #####
#   # # A # #   #  -----> #   # # B # #   # -----> #   # # C # #   # -----> NULL
#   # #   # #   #  <----- #   # #   # #   # <----- #   # #   # #   #
##### ##### #####         ##### ##### #####        ##### ##### #####
# ^
# |
# |
# Null

class DLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

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

    def get_previous(self):
        """Return the atribute"""

        return self.previous

    def set_previous(self, new_previous):
        """Replace the existing value on previous with the value of new_previous"""

        self.previous = new_previous


class DLL:

    def __init__(self):

        self.head = None

    def __repr__(self):
        return 'Object: head={}'.format(self.head)

    def is_empty(self):

        return self.head is None

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

    def add_front(self, new_data):
        """Add a node whose data is the new_data to the front of the linked list"""

        temp_node = DLLNode(new_data)
        temp_node.set_next(self.head)

        if self.head is not None:
            self.head.set_previous(temp_node)

        self.head = temp_node

    def remove(self, data):
        """Removes the firts occurence of a node that constains the data argument
        as its data variable. Return nothing.

        Time complexity: O(N)
        """

        if self.head is None:
            return 'Linked list is empty'

        current = self.head
        found = False

        while not found:
            if current.get_data() == data:
                found = True

            else:
                if current.get_next() is None:
                    return 'No nodes with this value'
                else:
                    current = current.get_next()
        if current.previous is None:
            self.head = current.get_next()
        else:
            current.previous.set_next(current.get_next())

            current.next.set_previous(current.get_previous())
