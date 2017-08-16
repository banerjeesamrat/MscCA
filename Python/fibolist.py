#upto thousand
l1=[0,1]
while((l1[len(l1)-2]+l1[len(l1)-1])<=1000):
	l1.append(l1[len(l1)-2]+l1[len(l1)-1])
print("List upto 1000")
print(l1)

#first 10
l2=[0,1]
while(len(l2)<10):
	l2.append(l2[len(l2)-2]+l2[len(l2)-1])
print("First 10 elements")
print(l2)