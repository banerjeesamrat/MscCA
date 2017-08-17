#It is a basic Program showing implementation some maths functions and basic functions


"""
Visual Studio Shortcut to Run Program
ctrl + shift + b
or
better
F1 or ctrl + alt + n
and to stop
F1 or ctrl + alt + m
"""

#Basic Operations Done

print(int("5"))
print(abs(-15))
print(5/12)
print(round(15.15661612,2))

a = float(input("Enter a No: "))
print(a)
print(type(a))
#print(type(a))


#Vowels and Consonant

a=raw_input("Enter A Character: ")
if a in "AEIOUaeiou":
	print("Vowel")
else:
	print("Consonant")
#print(a)