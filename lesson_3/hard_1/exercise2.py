# What does the last line in the following code output?

dictionary = {'first': [1]}
num_list = dictionary['first'] # => [1]
num_list.append(2) # => [1, 2]

print(num_list) # => [1, 2]
print(dictionary) # => {'first': [1, 2]}

# num_list references the same list object that nested in the dictionary
