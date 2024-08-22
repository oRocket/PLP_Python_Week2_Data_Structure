# Create an empty list called my_list
my_list = []

# Append the value 10 to the end of my_list
my_list.append(10)

# Append the value 20 to the end of my_list
my_list.append(20)

# Append the value 30 to the end of my_list
my_list.append(30)

# Append the value 40 to the end of my_list
my_list.append(40)

# Insert the value 15 at the second position (index 1) in my_list
my_list.insert(1, 15)

# Extend my_list by adding the elements from another list [50, 60, 70] to the end
my_list.extend([50, 60, 70])

# Remove the last element from my_list (in this case, 70)
my_list.pop()

# Sort the elements of my_list in ascending order (smallest to largest)
my_list.sort()

# Find and print the index of the value 30 in my_list
print(my_list.index(30))  # This prints the index where 30 is located in the sorted list
