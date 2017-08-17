#While User Enters Numbers Check if it is Prime or Not
'''
no=2
while(no>1):
    no=int(input("Enter a Number : "))
    prime='Y'
    if (no<=1):
        prime='N'
    else:
        #for i in range(2,no):
        for i in range(2,int(no/2)+1): #no square root is also OK like no / 2
            if(no%i==0):
                prime='N'
                break;
    if prime=='Y':
        print("%d is a Prime Number" %(no))
    else:
        print("%d is not a Prime Number" %(no))
'''

#Store 1st 25 Prime Numbers in a List
num=2
count=0
l=[]

while(count<25):
    prime='Y'
    for i in range(2,int(num/2)+1): #no square root is also OK like no / 2
        if(num%i==0):
            prime='N'
            break
    if prime=='Y':
        l.append(num)
        count+=1
        #print("%d is a Prime Number" %(num))
    #else:
        #print("%d is not a Prime Number" %(num))
    num+=1
print(l)