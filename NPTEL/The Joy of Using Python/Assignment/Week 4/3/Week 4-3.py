# Your last recorded submission was : (Working)
r,c =input().split(" ")
r=int(r)
c=int(c)
mat=[[0 for i in range(c)]for j in range(r)]
val=1
for i in range(r):
  for j in range(c):
    mat[i][j]=val
    val=val+1
for i in range(r):
  for j in range(c):
    if j !=(c-1):  
       print(mat[i][j],end=" ")
    else:
       print(mat[i][j],end="")
  if i!=(r-1):
    print()



# Sample solutions (Provided by instructor)
a,b=map(int,input().split())

count=1
m = []
for i in range(1,a+1):
    l = []
    for j in range(1,b+1):
        l.append(count)
        count+=1
    m.append(l)

for i in range(a):
    for j in range(b):
        if(j==b-1):
            print(m[i][j], end="")
        else:
            print(m[i][j], end=" ")
    if(i!=a-1):
        print()
