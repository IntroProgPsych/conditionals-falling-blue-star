
age = int(input("type your age: "))
if age>=18 and age<100:
    print("you are an adult")
elif age>100:
    print("you are too old")
elif age>0:
    print("you are a child")
else:
    print("you havent been born yet")