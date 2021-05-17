# Dictionary:
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered, changeable and does not allow duplicates.

"Key"        "Value"
#####        ######
# 9 # -----> # 22 #
#####        ######
#####        ######
# 1 # -----> # HI #
#####        ######
#####        ######
# 3 # -----> # 11 #
#####        ######
#####        ######
# 5 # -----> # A2 #
#####        ######

# Simple dictionary
animals = {
    'animal': 'dog',
    'Name': 'Flufly',
    'age': 5
}

print("Animals: {}".format(animals))

# Nested Dictionary
person = {
    1: {'name': 'Bob', 'age': 20, 'sex': 'M'},
    2: {'name': 'Ana', 'age': 24, 'sex': 'F'},
    3: {'name': 'Liz', 'age': 27, 'sex': 'F'},
}

print("Persons: {}".format(person))

# Access to elements
print("{}".format(person[1]['name']))
print("{}".format(person[1]['age']))
print("{}".format(person[1]['sex']))


# Add elements or changed

animals = {
    'animal': 'dog',
    'Name': 'Flufly',
    'age': 5
}

animals['animal'] = 'cat'

print("Animals: {}".format(animals))


# Delete elements

animals = {
    'animal': 'dog',
    'Name': 'Flufly',
    'age': 5
}

del animals['animal']

print("Animals: {}".format(animals))

# Iterate a dictionary

person = {
    1: {'name': 'Bob', 'age': 20, 'sex': 'M'},
    2: {'name': 'Ana', 'age': 24, 'sex': 'F'},
    3: {'name': 'Liz', 'age': 27, 'sex': 'F'},
}

for item in person.items():
    print(item)
