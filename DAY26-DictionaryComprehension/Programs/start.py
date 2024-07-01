# new_dict = {new_key:new_value for item in list}

# new_dict = {new_key:new_value for (key, value) in dict.items()}

# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

import random
names = ["Aman", "Raj", "Abhilash", "Abhishek", "Amy", "Atul"]
student_score = {student: random.randint(40, 100) for student in names}
Agrade_student = {student: score for (student, score) in student_score.items() if score > 90}
