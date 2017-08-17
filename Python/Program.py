#Write a program to accept 2 Strings and Compare
'''
str1=input("Enter First String: ")
str2=input("Enter Second String: ")

if(len(str1)>len(str2)):    
    shortStr=str2
    longStr=str1
else:
    shortStr=str1
    longStr=str2

result=0

for i in range (0,len(shortStr)):
    if(shortStr[i]>longStr[i]):
        print("\"%s\" is greater than \"%s\"" %(shortStr,longStr))
        result=1
        break
    elif(shortStr[i]<longStr[i]):
        print("\"%s\" is greater than \"%s\"" %(longStr,shortStr))
        result=1
        break
if (result==0):
    if(len(str1)==len(str2)):
        print("\"%s\" is equals to \"%s\"" %(longStr,shortStr))
    else:
        print("\"%s\" is greater than \"%s\"" %(longStr,shortStr))
'''
#Accept Values in the List and find how many times each value is repeated.

l=[]
while(True):
    value=int(input("Enter a Value: "))
    if (value<0):
        break
    l.append(value)
print(l)

k=[]
for i in range (0, len(l)):
    if (l[i] not in k):
        k.append(l[i])
        
for i in range(0,len(k)):
    count=0
    for j in range(0,len(l)):
        if(k[i]==l[j]):
            count+=1
            #l[j]=0
            # k=l[0:j]
            # j=l[j+1:]
            # print(k)
            # print(j)
            # l=k+j
            # print(l)
            # print("D")
    print("%s is printed %d times." %(k[i],count))
