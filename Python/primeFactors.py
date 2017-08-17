no=int(input("Enter a Number: "))
for i in range(no,0,-1):
    if(no%i==0):
        prime='Y'
        for j in range(2,i):
            if(i%j==0):
                prime='N'
                break;
        if prime=='Y':
            print("%d is a Prime Factor" %(i))
        else:
            print("%d is not a Prime Factor" %(i))