#Write a func similar to insert, remove, and reverse
#i.e. Insert a Value without using insert method
#i.e. Remove a Value without using remove method
#i.e. Reverse a List without using reverse method

l=[0,1,2,315,63,5,5,6,7]
print(l)

l.append(0)
print(l)
#insert at index of 4
indx=4
for i in range(len(l)-1,indx,-1):
    temp=l[i]
    l[i]=l[i-1]
    l[i-1]=temp
l[indx]=150

print(l)

'''
#remove at index of 4
indx=4
for i in range(indx,len(l)-1):
    l[i]=l[i+1]
l.pop()

print(l)
'''

'''
#reverse a list
i=0
while(True):
    if((len(l)-i-1)<=i):
        break
    temp=l[i]
    l[i]=l[len(l)-i-1]
    l[len(l)-i-1]=temp
    i+=1
print(l)
'''