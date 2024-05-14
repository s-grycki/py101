# What will the following code print and why?
# Don't run it until you have tried to answer

num = 5

def my_func():
    print(num)

my_func() # => 5

# This works because my_func is only trying to access a variable which was
# declared in an outer scope
