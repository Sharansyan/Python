# Your last recorded submission was :(Working)
n=int(input())
d={x:x*x*x for x in range(1,n+1)}
print(d,end="")



# Sample solutions (Provided by instructor)
n=int(input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i*i

print(d)
