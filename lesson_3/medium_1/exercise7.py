# One day, Spot was playing with the Munster family's home computer,
# and he wrote a small program to mess with their demographic data:

munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"

# After writing this function, he typed the following code:
mess_with_demographics(munsters) # => Mutates dictionary

# Before Grandpa could stop him, Spot hit the Enter key with his tail.
# Did the family's data get ransacked? Why or why not?

# Yes. The function mutates the dictionary without doing any reassignment
# beforehand. This means both the local variable and global variable were
# impacted
