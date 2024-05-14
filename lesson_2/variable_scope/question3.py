# What will the following code print and why?
# Don't run it until you have tried to answer

num = 5

def my_func():
    global num
    num = 10

my_func()
print(num) # => 10

# The global keyword is used in my_func. This loads in global variable num,
# so the next line now works as reassignment to a variable accessible in the
# local scope
