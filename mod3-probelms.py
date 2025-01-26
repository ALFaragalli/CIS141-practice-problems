# 1. Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated. 
# Use the skills you learned in this module to print the word the correct number of times.
word = input("Please enter a word: ")
repeat = int(input("How many times would you like it to be repeated? "))
print(word*repeat)
#2. Prompt the user for their name and their age. Calculate their age next year. 
# Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."
name = input("What is your name? ")
age1 = int(input("How old are you?"))
age2 = age1 + 1
print(f"Hello, {name}! You are {age1} years old. Next year, you will be {age2}")
#3. Prompt the user for a sentence and a word to try to find in that sentence.
# Have the program print out whether the word was found in the sentence. (i.e. True or False)
sentence = input("Please enter a sentence: ")
findword = input("What word would you like to try to find? ")
print(findword in sentence)
#4. Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen.
aword = input("Please enter a word: ")
index1 = int(input("How many letters starting at the beginning of do you want to keep? "))
index2 = int(input("How many letters starting at the end going left of do you want to keep? "))
print(aword[:index1] + aword[-index2:])
#5. Print 3 words with a | character (called a pipe) in between them. Use the appropriate keyword argument in print() to do so.
word1 = input("Please chose a first word: ")
word2 = input("Please chose a second word: ")
word3 = input("Please chose a second word: ")
print(f"{word1}|{word2}|{word3}")
