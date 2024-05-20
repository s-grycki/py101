# Starting with the string:

famous_words = "seven years ago..."

# Show two different ways to create a new string with
# "Four score and " prepended to the front of the string

famous_words = "seven years ago..."
famous_words = "Four score and " + famous_words
print(famous_words)

famous_words = "seven years ago..."
famous_words = f'Four score and {famous_words}'
print(famous_words)
