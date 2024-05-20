# Given the following similar sets of code, what will each code snippet print?

def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")     # => ['one']
print(f"two is: {two}")     # => ['two']
print(f"three is: {three}") # => ['three']



def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")     # => ['one']
print(f"two is: {two}")     # => ['two']
print(f"three is: {three}") # => ['three']



def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")     # => ['two']
print(f"two is: {two}")     # => ['three']
print(f"three is: {three}") # => ['one']
