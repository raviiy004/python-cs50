# 1. unsing del()
d={"a": 1, "b": 2, "c": 3}
del d["b"]
print(d)

#2 usnig pop

f={"e":3, "f":4, "g":5}
val = f.pop("f")
print(f)
print(val)

#3 using popitem
g={"h":6, "i":7, "j":8} 
val = g.popitem()
print(g)

#4 using clear
h={"k":9, "l":10, "m":11}
h.clear()
print(h)