# Lists are also a data type in Python. Lists are used, to store an amount of data.
# The data a list contains is not relevant, it can be everything.

# An example:
list = ["Julian", "Max", "Jenny", "Yasin", 23, 12, 64, 41]

# The list contains the names Julian, Max, Jenny, and Yassin.
# It also contains the numbers 23, 12, 64, 41.
# Well but what to do now? Let's try to request this data!
# To do that, you need to know that a list has a so called "list-index".
# This index allows you to work with the data on it's position.
# Generally in programming, the computer starts counting at 0 instead of 1.
# And it's no different with lists. So if we want to request our first object ("Julian"), we need to use the 0th list-index.

# That works the following:
print(list[0])
#          ^ This is the index.

# Well now, let's try to add a value to the list.
list.append("Joma")
# With the '.append()' function you can add values to a list.