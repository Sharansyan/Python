# Your last recorded submission was :(Working)
A=int(input())
printDict={x:x*x for x in range(1,A+1)}
print(printDict,end="")
printDict()



# Sample solutions (Provided by instructor)
def printDict():
    n = int(input())
    d=dict()
    for i in range(1,n+1):
        d[i]=i**2
    print(d)
printDict()
