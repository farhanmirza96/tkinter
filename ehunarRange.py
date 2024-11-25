print(list(range(10)))          # create list
print(list(range(1, 10)))       # create list with starting point

even = list(range(0, 20, 2))
odd = list(range(1, 20, 2))

print(even)
print(odd)

print(even[2])     # print index value
print(even.index(6))    # print value index location

list_2 = (range(7, 1000, 7))
num = int(input ("Please enter a number to find divisible in a list: "))
print(f"{num} is divisible by seven: {num in list_2}")   # it will show result in buleon