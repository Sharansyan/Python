# Your last recorded submission was : (Working)
x = input()
a = []
for char in x:
    a.append(char)

l = len(a)-1
print(a[0]+a[1]+a[l-1]+a[l], end="")



# Sample solutions (Provided by instructor)
s=input()
if len(s)<2:
    print("",end="")
else:
    print(s[:2]+s[len(s)-2:len(s)],end="")
