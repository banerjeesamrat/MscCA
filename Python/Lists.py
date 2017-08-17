'''
List is a Collection of value of any type
or Tuple is also simillar but the value of tuple cant be changed later on

l=[25,30,30,-10]
l1=[25, "MSc", "Sum", "Sem 1", 65, 18.5]
l=[]

'''
'''
l=[25,30,"Kushal",-10]

l[0]=l[1]*l[0]

l.append("100"*2)
print(l[4])
print(len(l))
print("")

for i in l:
    print(i)
'''

#Dynamic Lists
'''
l=[]
flag="Y"
while(flag in "Yy"):
    n=int(input("Enter Value: "))
    l.append(n) # At The Append
    flag=input("Do You Want To Add More. Y/N: ")
    #flag.upper()
#print(l)

sum=0
product=1
min=l[0]
max=l[0]

for i in range (0,len(l)):
    #print(l[i])
    sum=sum+l[i]
    product*=l[i]
    if(l[i]>max):
        max=l[i]
    if(l[i]<min):
        min=l[i]

print("Sum = %d" % (sum))
print("Product = %d" % (product))
print("Average = %d" % (sum/len(l)))

print("Max = %d" % (max))
print("Min = %d" % (min))
'''

'''
#Store first 27 E1 Numbers in the list
i=1
l=[]
while(i<=27):
    l.append(i*2)
    i+=1
print(l)

#Store first 27 Odd Numbers in the list Without using N
i=1
l=[]
while(i<=27):
    l.append((i*2)-1)
    i+=1
print(l)
'''

'''
i=1
l=[]
while(i<=27):
    l.append((i*2)-1)
    l.append(i*2)
    i+=1
print(l)
'''

'''
#Print Fibonacci upto 1000

j=1
i=0
while(i<=1000):
    print(i)
    i=i+j
    j=i-j
'''

#OR

l=[0,1]
i=2
while(True):
    if(l[i-1]+l[i-2]):
        l.append(l[i-1]+l[i-2])
        i+=1
    else:
        break;


'''
#First 10 Elements of Series
count=1
l=[]

j=1
i=0
while(count<=10):
    l.append(i)
    i=i+j
    j=i-j
    count+=1
print(l)
'''