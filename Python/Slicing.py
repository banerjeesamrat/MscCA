'''
s="SICSR MScCA/SS"
t=(23,-1,5.7,s)
print(s[0])
print(t[3][0])

for i in range(0,len(s)):
    print(s[i])

for i in s:
    print(i)
'''

#Write a Program to accept string and calculate no of characters in a string
'''
str=input("Enter a String: ")
count=0
for i in str:
    count+=1
print("No of Character in '%s' is : %s "%(str,count))
'''

#Reverse a String without using Len
'''
str=input("Enter a String: ")
print("Reverse of '%s' is '%s' "%(str,str[::-1]))
'''

#Accept a String, Extract 1st and last 3 char in string and store them in another string(Slicing Not Allowed but len is allowed)
'''
str=input("Enter a String: ")

resultStr=""

for i in range(0,3):
    resultStr+=str[i]
for i in range(len(str)-1,len(str)-4,-1):
    resultStr+=str[i]

print("Resultant String is %s"%(resultStr))
'''

#Accept 2 Number n1,n2 extract from 1st number to second
'''
'''
