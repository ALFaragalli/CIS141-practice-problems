#1. Construct a truth table for the expression: (A AND B) OR (NOT B) where A and B each can be True or False.
# Your truth table should be commented out (as it's not valid Python code!)
'''
A B     (A AND B)     (NOT B)      (A AND B) OR (NOT B)
T T     T             F             T
T F     F             T             T
F T     F             F             F
F F     F             T             T

'''

#2. The headlights of a car should only automatically turn on when the daylight outside is below a certain threshold.
# If a sensor threshold is below the number 8, print "Headlights On"; otherwise, print "Headlights Off".
sensor = int(input("What number is the sensor threshold at? "))
if sensor < 8:
    print("Headlights On")
else:
    print("Headlights Off")

#3. Prompt the user for their bank balance. Evaluate whether the balance is less than $100.
# Print True if the user’s balance is below $100; print False, otherwise.
Balance = int(input("What is your bank balance? $"))
if Balance < 100:
    print("True")
else:
    print("False")
#4. A theater wants to enforce age restrictions for movie tickets. Ask the user for their age, and tell them whether they can see G
# (appropriate for under 13), PG-13 (appropriate for 13 to 17), or R (appropriate for over 18) rated movies.
age = int(input("What is your age? "))
if age < 13:
    print("you can see G rated movies!")
elif age <= 17:
    print("You can see both G and PG-13 rated movies!")
else:
    print("You can see all G, PG-13, and R rated movies!")
#5. A store charges $5 for shipping on any order under $50. If the order amount is $50 or more, shipping is free.
# Ask the user for the order total and print the total cost, including shipping.
order = int(input("How much is your order total? $"))
if order < 50:
    print(f"Your total is ${order + 5}! Including shipping")
else:
    print(f"Your total is ${order}! Shipping is free! ")
    
