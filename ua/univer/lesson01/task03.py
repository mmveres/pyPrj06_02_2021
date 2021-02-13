x = 2.001
y = 2.002
x+=0.002000000001
y+=0.001
is_equal = abs(x-y)<0.001
print("is_equal x y",is_equal)
print(round(x,3))
print(round(y,3))