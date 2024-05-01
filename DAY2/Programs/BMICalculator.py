#Take height and weight as input
height = input("Enter the height in meter: ")
weight = input("Enter the weight in kg: ")

BMI = int(weight)/ (float(height) * float(height))
print(int(BMI))