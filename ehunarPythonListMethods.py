a = [1,2,3,"a","b","c"]
b = [4,5,6,"d","e","f"]

c = a + b

print(c)

# adding by builtin method

a.extend(b) # we can also add single value like this...........    a.extend("x")
print(a)
a.append("x") # adding value in a list
print(a)

a.pop()    # remove last element
print(a)

a.remove("e")  # remove desire value
print(a)

print(a.count(3))   # count and display how many 3 in a list

# a.sort()          # will sort only if data type is same in a list
# a.sort(reverse=true)     # will reverse it
# a.reverse()        # direct method
# print(a)

# print(min(a))     min value intigers datatype only
# print(max(a))     max value intigers datatype only

a[0] = "b"         # replace value on 0 index  this method is called mutability
print(a)

