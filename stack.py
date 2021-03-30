#Notes

# A Stack is a linear data structure in which elements can be inserted and
# deleted only from one side of the list, called the top.
# A stack follows the LIFO. (Last In First Out)
# Stack has a dynamic and fixed size.
# Stack remove remove from the top.

# STACK

#####
# 0 #    <------- TOP
#####
# 1 #
#####
# 2 #
#####
# 3 #
#####


stack = []

# Append items to the stack
stack.append("Item 1")
stack.append("Item 2")
stack.append("Item 3")

print("\n Initial stack")
print(stack)

# Poped items froms the stack
stack.pop(0)

print("\n Stack after pop")
print(stack)

# Insert items by index to the stack
stack.insert(0, "Item 4")

print("\n Stack insert by index")
print(stack)
