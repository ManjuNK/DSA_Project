# Python3 code to demonstrate working of
# Get unique tuples from list
# using dict.fromkeys() + list()

# initializing list
test_list = [(4, 5), (6, 1), (4, 5), (6, 1)]

# printing original list
print("The original list is : " + str(test_list))

# Get unique tuples from list
# using dict.fromkeys() + list()
res = list(dict.fromkeys(test_list))

# printing result
print("List after removal of duplicates " + str(res))
