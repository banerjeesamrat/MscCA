#accept 2 strings and check which is greater

string_1=raw_input("Enter a string : ")
string_2=raw_input("Enter another string : ")

i=0
flag=0

while(i!=len(a) and i!=len(b)) :
	if(string_1[i]>string_2[i]):
		print("%s is greater" %string_1)
		flag=1
		break
	elif(string_2[i]>string_1[i]):
		print("%s is greater" %string_2)
		flag=1
		break
	i=i+1

if(flag==0):
	if(i==len(string_1) and i==len(string_2)):
		print("Strings are equal.")
	elif(i<len(string_1)):
		print("%s is greater" %string_1)
	elif(i<len(string_2)):
		print("%s is greater" %string_2)