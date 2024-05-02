# Input a list of student scores
student_scores = input().split()
# Convert each score to an integer
for n in range(len(student_scores)):
  student_scores[int(n)] = int(student_scores[n])
# Write your code below this row 👇
highest_score = 0

for i in student_scores:
  if i > highest_score:
    highest_score = i

print(f"The highest score in the class is: {highest_score}")
