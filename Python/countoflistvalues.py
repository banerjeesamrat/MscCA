#accept some values in the list and find out how many times each value is repeated

n=int(input("How many values : "))

#declarations
myList=[]
unique=[]

#accepting every number
for i in range(0,n):
	myList.append(int(input("Enter the value : ")))

for i in range(0, len(myList)):
	count=1
	for j in range(i+1, len(myList)):
		if(myList[i]==myList[j]):
			count=count+1
	if(myList[i] not in unique):
		unique.append(myList[i])
		print("%d comes %d times." %(myList[i],count))	