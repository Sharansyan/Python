# Your last recorded submission was :(Working)
line = input()

upper = sum(map(str.isupper, line))
lower = sum(map(str.islower, line))

upper = str(upper)
lower = str(lower)
list = []
list.append(upper)
list.append(lower)

print(' '.join(list),end='') 



# Sample solutions (Provided by instructor)
s = input()
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print(d['UPPER CASE'],d['LOWER CASE'])
