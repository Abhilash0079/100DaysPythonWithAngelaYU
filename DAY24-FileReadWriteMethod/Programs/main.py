file = open('D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY24-FileReadWriteMethod/Programs/my_file.txt')
contents = file.read()
print(contents)
file.close()

# write in the file
# it will overwrite the entire text with the new text.
with open('D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY24-FileReadWriteMethod/Programs/my_file.txt', mode='w') as f:
    f.write("Hello, My name is Abhilash Kumar.\n")
    f.write("I am 24 years old.\n")
    f.write("My favourite food is Biryani.\n")

# using the append method
with open('D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY24-FileReadWriteMethod/Programs/my_file.txt', mode='a') as f:
    f.write('Appended text\n')
# Using with command

with open('D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY24-FileReadWriteMethod/Programs/my_file.txt') as file:
    contents = file.read()
    print(contents)
# no use to close() function here.

with open('D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY24-FileReadWriteMethod/Programs/new_file.txt', mode='w') as f:
    f.write("It will create the file if it doesn't exist.")
