# What will the following two lines of code output?

print(0.3 + 0.6) # => 0.899999999999999 (Floating point precision problem)
print(0.3 + 0.6 == 0.9) # => False (Floating point precision problem)

# Solution 1: decimal class
from decimal import Decimal
print(float(Decimal('0.3') + Decimal('0.6')) == 0.9) # => 0.9 (as a decimal class - not a float)

# Solution 2: math class
from math import isclose
print(isclose(0.3 + 0.6, 0.9)) # => True (close within a degree of tolerance)
