                            # Table using for and while loop

# vnum1 = int(input ("Enter a number of a table you want to print: "))
# for i in range (1, 21):
#     print (f' {vnum1} × {i} = {vnum1*i} ')
# ***********************************

# vnum1 = int(input('Ener a number: '))
# i = 1
# while i<=10:
#     print (f'{vnum1} × {i} = {vnum1*i}')
#     i += 1
#  **********************************
    
# i = 5
# i += 2
# print (i)
#  **********************************

#   list comprihantion
vlist = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print (vlist)
print (type(vlist))
vlist2 = [i for i in range(10)]
print (vlist2)
vlist3 = [square**2 for square in range(10)]
print (vlist3)
vlist4 = [round(sqroot**0.5) for sqroot in vlist3]
print (vlist4)

# finding even in list
vEven = [x for x in range(10) if x%2 == 0]
print (vEven)
print (type(vEven))

# finding odd in list
vOdd = [y for y in range(10) if y%2 == 1]
print (vOdd)

# finding LCM
vMax = int(input('Enter first number: '))
vMin = int(input('Enter second number: '))

lcm = vMax
while lcm % vMin !=0:
    lcm += vMax
print (f'LCM of {vMax} and {vMin} is {lcm}')

# quit sentence
userInput = input ('Enter a sentence or type "quit" to exit: ')

while userInput.lower() != 'quit':
    print (f'You typed {userInput}')
    userInput = input ('Enter another sentence or type "quit" to exit: ')

print ('Loop exited because you type exit: ')

# condition
marks = int(input('Enter your marks: '))
if marks <= 30:
    print('You are failed: ')

elif marks >30 and marks <=40:
    print ('You got D grade: ')

else:
    print (' You passed the test: ')

# find two numbers whos sum is 9

twoSum = [2, 7, 15, 11, 5, 8, 6, 1, 3]
print (twoSum)
# for printing single or multiple index
print (twoSum[0], twoSum[3])
# for print all values
for i in twoSum:
    print(i)
ind = int(input('Enter an index number you want to print its value: '))
target = ind
print = (twoSum[target])

# print every character of a string
s1 = "Python language"

l = len(s1)
x = 0
while x < l:
    print(s1[x])
    x += 1

print("End of loop")

# Adding number from user input
sum = 0
x = ""
while x != "N":
    x = input("Enter a number to add of press 'N' to exit ")
    if x != 'N':
        sum = sum + int(x)

print(sum)