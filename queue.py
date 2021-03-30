# Notes

# A Queue is a linear structure that follows a particular order in
# which the operations are performed.
# The order is FIFO.(First In First Out)
# The difference between stacks and queues is in removing.
# Stack remove remove from the top and the queue remove the itemmore recent.

               # Rear                # Front
               #|                    #|
               #|                    #|
               #v       # Queue      #v
#Enqueue        ##### ##### ##### #####
# ------>       # 0 # # 1 # # 2 # # 3 #  ------> Dequeue
                ##### ##### ##### #####


queue = []

# Append items to the queue
queue.append("Item 1")
queue.append("Item 2")
queue.append("Item 3")

print("\n Initial queue")
print(queue)

# Unqueue items froms the queue
queue.pop(0)

print("\n Queue after pop")
print(queue)
