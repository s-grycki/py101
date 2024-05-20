# In the previous problem, our first answer added 'Dino' to the list like this:

flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.append("Dino")

# How can we add multiple items to our list (e.g., 'Dino' and 'Hoppy')? 
# Replace the call to append with another method invocation.

flintstones.extend(['Dino', 'Hoppy'])
print(flintstones)
# => ['Fred', 'Barney', 'Wilma', 'Betty', 'Bambam', 'Pebbles', 'Dino', 'Hoppy']
