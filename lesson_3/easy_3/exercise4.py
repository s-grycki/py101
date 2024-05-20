# What will the following code output?

my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy() # Shallow copy of list
my_list2[0]['first'] = 42
print(my_list1) # => [{"first": 42}, {"second": "value2"}, 3, 4, 5]

# This code only creates a shallow copy of the list. This means that references
# to inner objects are shared between the 2 variables even though they point
# to 2 different lists in the heap
