# Repeatation of task until a given condition is met
# till condition is true
# for n number of times
'''
j=0
for i in range(0,31,3):
    print("3 x",j, "=", i)


for i in range(1,35,2):
    print(i)
'''
#Print 50 Even Numbers

'''
for i in range(-1,-11,-1):
    print(i)
'''
'''
#Print No of Even Numbers in between 1 and input number
count=0

n1=int(input("Please Enter a Number: "))
for i in range(1,n1+1):
    if (i%2==0):
        count+=1

print("There are",count,"even numbers in between 1 and",n1)

#Print No of Even Numbers in between 1 and input number (Optimized)
count=0
n1=int(input("Please Enter a Number: "))
for i in range(2,n1+1,2):
        count+=1
print("There are",count,"even numbers in between 1 and",n1)


#Print No of Even Numbers in between 1 and input number (More Optimized)
n1=int(input("Please Enter a Number: "))
print("There are",int(n1/2),"even numbers in between 1 and",n1)
'''
'''
#Accept 2 no print from n1 upto n2 including both

n1=int(input("Please Enter first Number: "))
n2=int(input("Please Enter second Number: "))

if n1<n2:
    for i in range(n1,n2+1):
        print(i)
else:
    for i in range(n2,n1-1,-1):
        print(i)

'''

#Accept number and print its factorial
n1=int(input("Please Enter a Number: "))

fact=1

if n1<0:
    print("Enter Correct Number")
else:
    for i in range(n1,1,-1):
        fact*=i
    print("Factorial = ",fact)
