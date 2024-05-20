# How can you determine whether a given string ends with an exclamation mark
# (!)? Write some code that prints True or False depending on whether
# the string ends with an exclamation mark

str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

print(str1[-1] == '!', str2[-1] == '!') # => True, False
print(str1.endswith('!'), str2.endswith('!')) # => True, False
