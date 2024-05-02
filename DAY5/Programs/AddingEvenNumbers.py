target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇

total_sum = 0
for i in range(target+1):
  if i % 2 == 0:
    total_sum+=i

print(total_sum)