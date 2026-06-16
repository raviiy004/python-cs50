import array as arr
a= arr.array('i',[1,2,3])
print(a)

# for i in range(len(a)):
#  print(a[i], end=" ")

a.insert(2,6)
print(a)

a.append(5)
print(a)

for i in range(len(a)):
    print(a[i], end=" ")