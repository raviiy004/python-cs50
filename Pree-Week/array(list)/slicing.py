import array as arr

a = [1,2,3,4,5,6,7,8,9,10]
b = arr.array('i', a)

# from starting to index 5
c = b[:5]
print(c)

# remove last 3 elements
d = b[:-3]
print(d)

# from index 3 to end
e = b[3:]
print(e)

# from index 2 to 8
f = b[2:9]
print(f)

# print complete array
g = b[:]
print(g)

# reverse array
h = b[::-1]
print(h)