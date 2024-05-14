# What will the following code print and why?
# Don't run it until you have tried to answer

def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var) # => 'Hello World'

    inner()

outer()

# The inner function has inner_var available in the local scope, and since
# this function is only trying to access a variable, it will look up the
# outer scope to find outer_var
