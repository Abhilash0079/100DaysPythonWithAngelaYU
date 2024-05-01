print("Welcome to the Love Calculator!")

#Take input of their names.

name1 = input("What is your name? \n")
name2 = input("What's your partner name? \n")
name1 = name1.lower()
name2 = name2.lower()
name = name1 + name2

#count the first digit

t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
first_digit = t + r + u + e

#Count the second digit

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")
second_digit = l + o + v + e

#Final score

score = int(str(first_digit) + str(second_digit))

#Conditions

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")