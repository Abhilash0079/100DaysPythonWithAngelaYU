# new_dict = {new_key:new_value for item in list}

# new_dict = {new_key:new_value for (key, value) in dict.items()}

# new_dict = {new_key:new_value for (key, value) in dict.items() if test}
import pandas
import random
names = ["Aman", "Raj", "Abhilash", "Abhishek", "Amy", "Atul"]
student_score = {student: random.randint(40, 100) for student in names}
Agrade_student = {student: score for (student, score) in student_score.items() if score > 90}

# Looping through dictionaries

student_dict = {
    "student": ['Abhilash', 'Raj','Manish'],
    "score": [92, 95, 97]
}

for (key, value) in student_dict.items():
    print(key, value)


student_df = pandas.DataFrame(student_dict)
print(student_df)

# Loop through Dataframe

for (key, value) in student_df.items():
    print(key)
    # print(value)

# Loop through the row of Dataframe
for (index, row) in student_df.iterrows():
    # print(row)
    print(row.student)
    # print(row.score)

    if row.student == "Raj":
        print(row.score)
