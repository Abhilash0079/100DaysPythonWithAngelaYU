number = [1, 2, 3]
new_number = [n + 1 for n in number]
print(new_number)

name = "Abhilash"
new_list = [letter for letter in name]
print(new_list)

range_list = [n * 2 for n in range(1, 5)]
print(range_list)

names = ["Aman", "Raj", "Abhilash", "Abhishek", "Amy", "Atul"]
new_names = [i for i in names if len(i) < 5]
print(new_names)

cap_name = [n.upper() for n in names if len(n) > 5]
print(cap_name)