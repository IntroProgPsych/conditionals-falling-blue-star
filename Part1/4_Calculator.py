# Please write a program which asks the user for two numbers and an operation.
#  If the operation is add, multiply or subtract,
#  the program should calculate and print out the result of the operation
#  with the given numbers.
#  If the user types in anything else,
#  the program should print out nothing.

# Some examples of expected behaviour:

# Sample output
# Number 1: 10
# Number 2: 17
# Operation: add

# 10 + 17 = 27

# Sample output
# Number 1: 4
# Number 2: 6
# Operation: multiply

# 4 * 6 = 24

# Sample output
# Number 1: 4
# Number 2: 6
# Operation: subtract

# 4 - 6 = -2

# Write your code here:

n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))

operation = input("Operation: ").lower()

if operation == "add":
    print(f"{n1} + {n2} = {n1+n2}")
elif operation == "multiply":
    print(f"{n1} * {n2} = {n1*n2}")
elif operation == "subtract":
    print(f"{n1} - {n2} = {n1-n2}")