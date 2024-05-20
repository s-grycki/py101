# Determine whether the name Dino appears in the strings below
# -- check each string separately:

str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

print('Dino' in str1, 'Dino' in str2) # => False, True
print(str1.find('Dino'), str2.find('Dino')) # => -1, 41

# Using in is better when we're checking based on uncertainty
