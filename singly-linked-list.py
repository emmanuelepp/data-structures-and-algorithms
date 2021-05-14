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


class Node:

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
