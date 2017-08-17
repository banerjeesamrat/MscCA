#write a program to accept a string. Store characters of string in the list.
#Reverse the list and put it in a seperate string

my_string=raw_input("Enter a string : ")
my_list=[]

for x in my_string:
	my_list.append(x)

i=0
j=len(my_list)-1

while((i-j) not in [0,1]):
	temp=my_list[i]
	my_list[i]=my_list[j]
	my_list[j]=temp
	i=i+1
	j=j-1

new_string=""
for x in my_list:
	new_string=new_string+x

print(new_string)