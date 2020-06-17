# Your last recorded submission was : (Working)
N = int(input())
a= list(map(int,input().split()))
k= int(input())
P=a[k-1]
a.sort()
for i in range (len(a)):
    if a[i]==P:
        print(i+1)
        break



# Sample solutions (Provided by instructor)
n=int(input())
a=[int(x) for x in input().split()]
k=int(input())
key=a[k-1]
a.sort()
for i in range(len(a)):
    if key==a[i]:
        print(i+1)
        break
