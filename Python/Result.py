m1=int(input("Enter Marks of 1st Subject out of 100: "))
m2=int(input("Enter Marks of 2nd Subject out of 100: "))
m3=int(input("Enter Marks of 3rd Subject out of 100: "))

totalMarks = m1+m2+m3
print("Total Marks = ",totalMarks)

percent = round((totalMarks/3),2)
print("Percentage = ",percent,"%")

if m1<40 or m2<40 or m3<40:
        print("Failed in Subjects")
elif percent>70:
        print("Passed with Distinction")
elif percent>=60:
        print("Passed with Ist Division")
elif percent>=50:
        print("Passed with IInd Division")
elif percent>=40:
        print("Passed with IIIrd Division")
else:
        print("Failed")