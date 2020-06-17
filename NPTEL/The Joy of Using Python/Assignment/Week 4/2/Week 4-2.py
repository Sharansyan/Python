# Your last recorded submission was : (Working)
x=int(input())
ans=1
for i in range(1,x+1,1):
    ans=ans*i
print(ans)



# Sample solutions (Provided by instructor)
k = int(input())

fac = 1
for i in range(1,k+1):
    if(k==0):
        break
    fac=fac*i

print(fac)
