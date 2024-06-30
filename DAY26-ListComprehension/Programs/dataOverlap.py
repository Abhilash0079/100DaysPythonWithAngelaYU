with open('D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY26-ListComprehension/Resources/file1.txt') as file1:
  l1 = file1.readlines()
  

with open('D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY26-ListComprehension/Resources/file2.txt') as file2:
  l2 = file2.readlines()
  

result = [int(num) for num in l1 if num in l2]



# Write your code above 👆
print(result)