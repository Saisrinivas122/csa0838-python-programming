print("Enter Marks Obtained in 5 Subjects: ")
mark1 = int(input())
mark2 = int(input())
mark3 = int(input())
mark4 = int(input())
mark5 = int(input())

tot = mark1+mark2+mark3+mark4+mark5
avg = tot/5
print("average of student is",avg)
if avg>=90:
    print("Your Grade is A")
elif avg>=80 and avg<90:
    print("Your Grade is B")
elif avg>=70 and avg<80:
    print("Your Grade is C")
elif avg>=60 and avg<70:
    print("Your Grade is D")
elif avg>=50 and avg<60:
    print("Your Grade is E")
else:
    print("Your Grade is Fail")
