# FileNotFoundError
# with open("a_file.txt", "r") as file:
#     file.read()

# Key Error
# a_dict = {"Key": "Value"}
# print(a_dict["pass"])

# Index Error
# a = ["ram", "shyam", "Krishna"]
# print(a[3])

# TypeError
# text = "abc"
# print(text + 5)

# try - except - else - finally
try:
    file = open("D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY30-PasswordManagerWithSearch/Resources/a_file.txt")
    a_dict = {"Key": "Value"}
    print(a_dict["Key"])
except FileNotFoundError:
    file = open("D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY30-PasswordManagerWithSearch/Resources/a_file.txt", "w")
    file.write("File Created")
except KeyError as error_message:
    print(f"The key {error_message} doesn't exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File has closed.")
