no1=float(input("Enter First  Number: "))
no2=float(input("Enter Second Number: "))
no3=float(input("Enter Third  Number: "))

max=no1
if no2>max:
    max=no2
if no3>max:
    max=no3
print("Maximum of 3 Number is ",max)

if(no1>no2 and no1>no3):
    alertText="A ("+no1+") is Maximum"
elif(no2>no3 and no2>no1):
    alertText="B (" +no2+ ") is Maximum"
elif(no3>no1 and no3>no2):
    alertText="C ("+no3+") is Maximum"
elif(no1==no2 and no1==no3):
    alertText="All ("+no1+") are Equal"
elif(no1==no2):
    if(no1>no3):
        alertText="A & B ("+no1+") are Maximum"
    else:
        alertText="C ("+no3+") is Maximum"
elif(no1==no3):
    if(no1>no2):
        alertText="A & C ("+no1+") are Maximum"
    else:
        alertText="B ("+no2+") is Maximum"					
elif(no2==no3):
    if(no2>no1):
        alertText="B & C ("+no2+") are Maximum"
    else:
        alertText="A ("+no1+") is Maximum"
print(alertText)