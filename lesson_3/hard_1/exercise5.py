# What do you expect to happen when the greeting variable is referenced
# in the last line of the code below?

if False:
    greeting = "hello world"

print(greeting) # => Uninitialized variable error (NameError)

# Greeting exists as an identifier in memory, but is never assigned a value
