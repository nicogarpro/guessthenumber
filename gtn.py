import random
import time

# List of posible numbers

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

number = random.choice(list)

print("Guess a number from 1 to 10\nYou get 3 chances")

num1 = int(input())

if num1 == number:
    print("Correct!!")

elif num1 > number:
    print("Lower")

elif num1 < number:
    print("Higher")

num2 = int(input())

if num2 == number:
    print("Correct!!")

elif num2 > number:
    print("Lower")

elif num2 < number:
    print("Higher")

num3 = int(input())

if num3 == number:
    print("Correct!!")

elif num3 > number:
    print("Game over\nThe number was", number)

elif num3 < number:
    print("Game over\nThe number was", number)

time.sleep(3)
