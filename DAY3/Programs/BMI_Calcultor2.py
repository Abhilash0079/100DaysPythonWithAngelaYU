#Take input from the user

height = float(input("Enter your height in meter: "))
weight = int(input("Enter your weight in kg: "))

#Calculate BMI

bmi = int(weight/(height * height))
#print(bmi)

#Condition

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")