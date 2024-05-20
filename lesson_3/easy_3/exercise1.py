# Write two different ways to remove all of the elements from the following list:

# Valid solutions
numbers = [1, 2, 3, 4]
numbers.clear()
print(numbers) # => []

numbers = [1, 2, 3, 4]
while numbers:
    numbers.pop() # -1 every time
print(numbers) # => []

numbers = [1, 2, 3, 4]
for _ in range(0, len(numbers)):
    numbers.pop() # -1 every time
print(numbers) # => []

numbers = [1, 2, 3, 4]
for num in numbers[:]:
    numbers.remove(num) # Removes specific number each time
print(numbers) # => []

numbers = [1, 2, 3, 4]
while len(numbers) > 0:
    numbers.pop()# -1 every time
print(numbers) # => []

# Invalid solutions
numbers = [1, 2, 3, 4]
for i in range(0, len(numbers)):
    try:
        numbers.pop(i) # => (0, [1, 2, 3, 4]), (1, [2, 3, 4]), (2, [2, 4])
    except IndexError:
        print(numbers) # => [2, 4]

numbers = [1, 2, 3, 4]
for num in numbers: # numbers changes size/index correspondence each time
    numbers.remove(num)
print(numbers) # => [2, 4]
