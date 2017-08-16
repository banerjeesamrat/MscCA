l=[]
ans="y"
a_sum=0
product=1

while(ans in "Yy"):
	num=int(input("Enter your number : "))
	l.append(num)
	ans=raw_input("Do you want to continue? : ")
	a_sum=a_sum+num
	product=product*num
print(l)
average=a_sum/len(l)
print("Sum is " + str(a_sum) + ", Product is " + str(product) + ", Average is " + str(a_sum/len(l)))