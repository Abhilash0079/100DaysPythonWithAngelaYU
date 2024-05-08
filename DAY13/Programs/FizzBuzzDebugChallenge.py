# target = int(input())
# for number in range(1, target + 1):
#   if number % 3 == 0 or number % 5 == 0: ### have to check both condition so use 'and' instead of 'or'
#     print("FizzBuzz")
#   if number % 3 == 0: #use elif not if
#     print("Fizz")
#   if number % 5 == 0: #use elif not if
#     print("Buzz")
#   else:
#     print([number])  #premove [] square bracket.


######## Solution

target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)