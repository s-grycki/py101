# What will the following code print and why?
# Don't run it until you have tried to answer

num = 5

def my_func():
    num = 10

my_func()
print(num) # => 5

# The value pointed to by num remains 5 because the assignment within my_func
# only creates a new locally scoped variable with the same name
