# Notes

# An Array is a collection of items stored at contiguous memory locations.
# In the array the elements belong to indexes. (Arra[0]<--- index)
# Insertion and deletion can be done at any index in the array.
# Array has a fixed size.

##### ##### ##### ##### #####
# A # # B # # C # # D # # E #
##### ##### ##### ##### #####
# 0     1     2     3     4  <-------- Array index
# Array size = 5
# Firts index = 0
# Last index = 4


arr = [1, 2, 3, 4, 5]
# Iterate a array
for i in range(0, 5):
    print("\n Iteration")
    print(arr[i])

# Get arr element by index
print("\n Get index")
print(arr[2])
print('\n')

# Insert item, you need pass the index and de value

print("Insert item in the array \n")

# the magic of python :v is weird but I now that you got it ;).
arr.insert(0, 'new item')
print(arr)
print('\n')
