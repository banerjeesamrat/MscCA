#accept 2 lists. check whether first list exists in second list or not.

list1=[]
list2=[]

print("Accept list1")
for x in range(0,5):
	list1.append(int(input("Enter a number : ")))
print("Accept list2")
for x in range(0,10):
	list2.append(int(input("Enter a number : ")))

flag=1
for x in range(0,len(list1)):
	if(list1[x]!=list2[x]):
		print("List 1 doesn't exist in List 2")
		flag=0
		break
if (flag==1):
	print("List 1 does exist in List 2")