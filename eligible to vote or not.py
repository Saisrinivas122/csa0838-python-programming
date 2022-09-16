age = int(input("enter the age:"))
if age >= 18:
    print("eligible for voting")
else:
    print("not eligible for voting")
    print("have to vote after:",(18 - age))
