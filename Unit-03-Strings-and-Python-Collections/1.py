
sentence = input("Enter a sentence: ")

print("Length:", len(sentence))

print("Uppercase:", sentence.upper())

print("Lowercase:", sentence.lower())

print("After removing spaces:", sentence.strip())

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

print("After replacement:", sentence.replace(old_word, new_word))

character = input("Enter a character to count: ")

print("Character count:", sentence.count(character))

start_text = input("Enter starting substring: ")
end_text = input("Enter ending substring: ")

print("Starts with:", sentence.startswith(start_text))
print("Ends with:", sentence.endswith(end_text))

# String concatenation
str1 = "Hello"
str2 = "Python"

print("Concatenation:", str1 + " " + str2)

# String repetition
print("Repetition:", str1 * 3)

# Membership operators
print("'Python' in sentence:", "Python" in sentence)
print("'Java' not in sentence:", "Java" not in sentence)
