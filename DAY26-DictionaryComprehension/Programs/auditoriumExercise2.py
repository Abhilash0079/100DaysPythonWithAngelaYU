weather_c = eval(input())
# 🚨 Don't change code above 👆

# Write your code 👇 below:
weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)
