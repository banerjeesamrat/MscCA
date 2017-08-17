#Accept a String store each char in list, reverse list and convert back to string.
'''
str = input("Enter a String: ")
l=[]
for i in str:
    l.append(i)
print(l)

i=0
while((len(l)-i-1)>i):
    temp=l[i]
    l[i]=l[len(l)-i-1]
    l[len(l)-i-1]=temp
    i+=1
print(l)

result=""
for i in l:
    result+=i
print(result)
'''

'''
#Accept Values Two Lists Check Whether 1st list exists in another list. IN operator
l=[]
inpt=0
while(inpt>=0):
    inpt=int(input("Enter a Value to Insert in List 1: "))
    if (inpt<0):
        break
    l.append(inpt)

print(l)

k=[]
inpt=0
while(inpt>=0):
    inpt=int(input("Enter a Value to Insert in List 2: "))
    if (inpt<0):
        break
    k.append(inpt)

print(k)

flag = "T"
for i in range (0,len(l)):
    if(l[i]!=k[i]):
        flag="F"
        print("List 1 Doesn't Exists in List 2.")
        break
if(flag=="T"):
    print("List 1 Exists in List 2.")
    '''

l1=[1,2,3]
l2=[4,5,6,7,8]
l3=[]

'''
minlen=0
maxlen=0
if(len(l1)>len(l2)):
    maxlen=len(l1)
    minlen=len(l2)
else:
    maxlen=len(l2)
    minlen=len(l1)

'''
'''
for i in range(0, maxlen):
    if(i<len(l1)):
        l3.append(l1[i])
    if(i<len(l2)):
        l3.append(l2[i])

'''

for i in range(0, len(l1)):
    l3.append(l1[i])
    l3.append(l2[i])
print(l3)

l3.extend(l2[i-1:])
print(l3)