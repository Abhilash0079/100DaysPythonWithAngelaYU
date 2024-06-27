# with open('D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY25-ReadFileUsingCSVandPandas/Resources/weather_data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv

# with open('D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY25-ReadFileUsingCSVandPandas/Resources/weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     # it will return an object "<_csv.reader object at 0x000001C82A2F0BE0>"
#     # print(data)
#     temperature = []
#     for row in data:
#         print(row)
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))

#     print(temperature)

import pandas

data = pandas.read_csv('D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY25-ReadFileUsingCSVandPandas/Resources/weather_data.csv')
print(data)
print(data['temp'])

print(type(data))
print(type(data['temp']))

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(len(temp_list))

# Find average temperature

avg_temp = sum(temp_list)/len(temp_list)
print(avg_temp)
# using pandas
print(data['temp'].mean())
print(data['temp'].max())

# # Get data in columns
print(data['condition'])
print(data.condition)

# Get data in row
print(data[data.day == "Monday"])

# Challenge: To print the row having maximum temperature
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

# Challenge : Get monday temperature in celceius
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Abhilash"],
    "scores": [76, 65, 98]
}

data_frame = pandas.DataFrame(data_dict)
#print(data_frame)
data_frame.to_csv('D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY25-ReadFileUsingCSVandPandas/Resources/new_data.csv')
