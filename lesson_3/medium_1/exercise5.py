# What do you think the following code will output?

nan_value = float("nan")

print(nan_value == float("nan")) # => False. Python doesn't allow value equivalency checking for nan

# How can you reliably test if a value is nan?
from math import isnan
print(isnan(float('nan'))) # => True
