# What is the output of the following code?

answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8) # => 34

# new_answer points to the number 50, and answer still points to 42 when
# subtracted by 8
