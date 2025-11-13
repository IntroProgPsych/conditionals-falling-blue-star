# You are tasked with creating a simple grading system for a class. 
# Write a Python program that takes a student's score as input
#  and calculates and prints its corresponding letter grade based on the following grading scale:

# 90 or above: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F

n = input("score: ")
if n.isnumeric(): n = int(n)

grade = None

if n < 60: grade = 'F'
elif n < 70: grade = 'D'
elif n < 80: grade =  'C'
elif n < 90: grade = 'D'
else: grade = 'A'

print(f"your grade is {grade}")

