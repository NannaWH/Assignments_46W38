x = 3 # Try x = 3 and x = 30
y = None
for i in range(10):
    if i%2 == 0:
        x += i
    
    if x >= 11 and x < 20:
        y = x * i
    else:
        y = x + i
    while x < 10:
        x = x + 1
    if y > 20:
        break
    if y > 10:
        continue
x = x + 1
print(x, y, i)

# x=3 then x=10, y=12 and i = 9 

# x=30 then x=30, y=30 and i = 0