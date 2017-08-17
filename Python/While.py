#Write a Short Program to guess the number

count=1
guess=10
no=0

while(count<=5):
    no=int(input("Guess a Number: "))
    if(no==guess):
        break
    else:
        count+=1
if no!=guess:
    print("You Couldn't Guess")
else:
    print("Number Guessed Correctly in %d Guesses." % (count))

'''

in case of 'or' if 1st cond is not true then only 2nd is checked
in case of 'and' if 1st cond is true then only 2nd is checked

'''

'''
while(True):
    no=input("Enter a Number: ")
    if(no<0):
        continue
    print("Working Fine")
'''