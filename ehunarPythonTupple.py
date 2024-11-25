tuple_a = (1,2,3,"a","b","c")
# or 2nd method to define a tuple
tuple_b = 5, 6, 7, 8, "d", "e"

print(tuple_a)

tuple_c = tuple_a[0], tuple_a[3], tuple_b[2]     # it will create a new tuple with desire value of two tuple...we can also reasign it to existing tuple
print(tuple_c)


# Tuple unpacking
tuple_x, tuple_y, tuple_z = tuple_c                 # it will unpack and assign values to new variable
print(tuple_x)
print(tuple_y)
print(tuple_z)