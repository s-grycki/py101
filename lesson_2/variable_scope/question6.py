# What will the following code print and why?
# Don't run it until you have tried to answer

def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x) # => 'Inner 1:' 25

    def inner_func2():
        print("Inner 2:", x) # => 'Inner 2:' 15

    inner_func1()
    inner_func2()

my_func()

# inner_func1 and inner_func2 have parallel level function scopes. This means
# that values initialized in one is inaccessible to the other. Therefore,
# inner_func2 can only access the x initialized in the my_func scope
