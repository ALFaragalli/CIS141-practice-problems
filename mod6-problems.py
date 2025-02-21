#1. Given a list of numbers, write code to iterate through the list and calculate the sum of all even numbers. Print the resulting sum.
numbers = [87, 12, 45, 98, 33, 67, 24, 76, 59, 81]
evens = 0
for num in numbers:
    if num % 2 == 0:
        evens += num
print("Sum of the even numbers:", evens)

#2. With a list of strings provided, write code that counts how many times the word "Olympic" appears in the list, and then print the count.
sentence = ["Olympic", "College", "Bremerton", "Shelton", "Poulsbo", "Olympic", "College", "Bremerton", "Shelton", "Poulsbo"]
count = 0

for word in sentence:
    if word == "Olympic":
        count += 1
print("'Olympic' in sentence:", count)

#3. Given a list of strings, write code to create a new list that includes only the strings longer than three characters.
# Print the resulting filtered list.
word_list = ["cat", "dog", "catipillar", "elephant", "buffalo", "rat", "mouse", "fly"]
filtered = []

for word in word_list:
    if len(word) > 3:
        filtered.append(word)
print(filtered)

#4. For a list of integers, write code that counts how many numbers are positive and how many are negative, then print both counts.
numbers1 = [-12, 32, 7, -5, 0, -93, 13, 84, -75, -16]
positive = 0
negative = 0

for num in numbers1:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
print(positive, "numbers are positive")
print(negative, "numbers are negative")

#5. For a list of integers, use a loop to build a new list where each element is the square of the corresponding element in the original list.
# Print the new list.
numbers2 = [2, 7, 5, 3, 4, 8]
squared = []

for num in numbers2:
    squared.append(num ** 2)
print("Squared Numbers:", squared)
