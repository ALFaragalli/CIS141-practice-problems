# 1. Create a program that prints the following output to the screen: "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."
print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")
# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.
import math
num1 = int(input("Chose a first number "))
num2 = int(input("Chose a second number "))
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1//num2)
# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)
a = int(input("What is the length of a? "))
b = int(input("What is the length of b? "))
c = int(input("what is the length of c? "))
s = int(1/2*(a+b+c))
A = int(math.sqrt(s*(s-a)*(s-b)*(s-c)))
print(A)
# 4. Create a program that computes different statistics given five numbers including the total, 
# average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).
num1 = int(input("Chose a first number: "))
num2 = int(input("Chose a second number: "))
num3 = int(input("Chose a third number: "))
num4 = int(input("Chose a fourth number: "))
num5 = int(input("Chose a fifth number: "))
numbers = num1, num2, num3, num4, num5
total = sum(numbers)
print(f"Total: {total:.2f}")
average = (num1+num2+num3+num4+num5)/5
print(f"Average: {average:.2f}")
minimum = min(numbers)
print(f"Minimum: {minimum:.2f}")
maximum = max(numbers)
print(f"Maximum: {maximum:.2f}")
range_value = maximum - minimum
print(f"Range: {range_value:.2f}")
variance = sum((x-average) ** 2 for x in numbers)/len(numbers)
standard_deviation = math.sqrt(variance)
print(f"Standard Deviation: {standard_deviation:.2f}")12
