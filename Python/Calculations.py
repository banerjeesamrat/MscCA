#Accept 10 numbers Find Max, Min, Average, Sum, Product of these numbers.
'''
for i in range(0,10):
    numbers=int(input("Enter Numbers: "))
    if i==0:
        max=numbers
        min=numbers
        sum=numbers
        product=numbers
    else:
        if numbers>max:
            max=numbers
        if numbers<min:
            min=numbers
        sum+=numbers
        product*=numbers


print("Maximum of 10 Numbers = ", max)
print("Minimum of 10 Numbers = ", min)
print("Sum = ", sum)
print("Average = ", sum/10)
print("Product = ", product)
'''
#Accept a no Print it in reverse , check whether it is palindrome. Palindrome means original no, reversed no are same. Example if no = 1221, then recersed no are same.
'''
no1 = str(int(input("Enter a number: ")))
rev_no1 = str(no1)[::-1]
print(rev_no1)

if no1==rev_no1:
    print("Palindrome")
else:
    print("Not Palindrome")

'''

#Accept a no and convert it into binary, octal, hexadecimal. Do not use bin, oct, hex functions
'''
no1 = int(input("Enter a Number: "))
#if no1 < 0:
    #strBinary="-"
#else:
    #strBinary=""

noBinary=no1
noOctal=no1
noHexadecimal=no1

strBinary=""
while noBinary !=0:
    strBinary=str(noBinary%2)+strBinary
    #noBinary=noBinary//2
    noBinary=int(noBinary/2)
print("Binary = ", strBinary)

strOctal=""
while noOctal !=0:
    strOctal=str(noOctal%8)+strOctal
    noOctal=int(noOctal/8)
print("Octal = ", strOctal)

strHexadecimal=""
while noHexadecimal !=0:
    x=noHexadecimal%16
    if x==10:
        strHexadecimal="A"+strHexadecimal
    elif x==11:
        strHexadecimal="B"+strHexadecimal
    elif x==12:
        strHexadecimal="C"+strHexadecimal
    elif x==13:
        strHexadecimal="D"+strHexadecimal
    elif x==14:
        strHexadecimal="E"+strHexadecimal
    elif x==15:
        strHexadecimal="F"+strHexadecimal
    else:
        strHexadecimal=str(x)+strHexadecimal
    noHexadecimal=int(noHexadecimal/16)
print("Hexadecimal = ", strHexadecimal)
'''

'''
no1 = int(input("Enter a Number: "))

num_sep=[0,0,0,0,0]

mod=10

for i in range(0,5):
    num_sep[i]=no1%mod
    no1=no1//mod
    #mod*=10
    print(no1)

print(num_sep)
print(1568//10)
'''
#Accept n1, n2. Round of n1 upto n2 decimal places.
'''
n1=float(input("Enter a Number: "))
n2=int(input("Enter Round off Places: "))

modNo=1
if n2>=0:
    for i in range(0,n2):
        modNo=modNo/10
else:
    for i in range(0,n2,-1):
        modNo=modNo*10

#print(round(n1,n2))
remainder=n1%modNo
if remainder>=5*0.1*modNo:
    remainder-=modNo
print("Rounded Number: ",n1-remainder)
'''
#Accept n1(Decimal) and base(64/8(0 to 7)/7(0 to 6)). Convert n1 to the respective base.
'''
#aLL project hard copy and submit before tuesday
no1 = int(input("Enter a Number: "))
noBase = int(input("Enter Base Number: "))
no=no1
strBase=""
while no1 !=0:
    strBase=str(no1%noBase)+strBase
    no1=int(no1/noBase)
print("Base",noBase,"of Number",no,"=", strBase)
'''