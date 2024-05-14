# What will the following code do?
# Don't run it until you have tried to answer

def my_func():
    num = 10

my_func()
print(num) # => NameError (num)

# This code will cause an error because num was initialized in a function
# scope and we're trying to access it in the global (an outer) scope
