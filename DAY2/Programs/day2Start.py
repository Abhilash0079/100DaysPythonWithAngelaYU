#Data Types

#String
print("Hello"[4])

#Integer
print(123 + 345)
#Float
3.14159
#Boolean
True
False
num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")
a = float(123)
print(type(a))
print(70 + float("100.5"))
print(str(70) + str(100))
print(3 * (3 + 3) / 3 - 3)
print(round(8 / 3, 2))
print(8 // 3)
result = 4 / 2
result /= 2
print(result)
score = 0
score+=1
height = 1.8
isWinning = True
#f-String
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")