# Creating a tuple
my_tuple = (10, 20, 30, 40, 50)
print("Original Tuple:", my_tuple)
# 1. Accessing Elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# 2. Slicing a Tuple
print( my_tuple[1:4])

# 3. Finding Length of Tuple
print(len(my_tuple))

# 4. Counting Occurrences of an Element
print( my_tuple.count(20))

# 5. Finding Index of an Element
print( my_tuple.index(30))

# 6. Tuple Concatenation
new_tuple = my_tuple + (60, 70)
print( new_tuple)

# 9. Iterating Over Tuple
print("Tuple Elements:")
for item in my_tuple:
    print(item)
