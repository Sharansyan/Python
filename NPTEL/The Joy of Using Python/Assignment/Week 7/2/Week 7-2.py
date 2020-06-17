# Your last recorded submission was :(Working)
n=int(input());
a=[list(map(int,input().split())) for i in range(n)];
i=0;
sym='YES';
while(i<n-1):
  j=i+1;
  while(j<n):
    if(a[i][j]!=a[j][i]):
      sym='NO';
      break;
    j+=1;
  i+=1;
print(sym,end='');



# Sample solutions (Provided by instructor)
def isSymmetric(mat, N): 
    for i in range(N): 
        for j in range(N): 
            if (mat[i][j] != mat[j][i]): 
                return False
    return True
   

a = int(input())


m = []
for i in range(1,a+1):    
    l = list(map(int, input ().split ()))
    m.append(l)
if (isSymmetric(m, a)): 
    print("YES")
else: 
    print("NO")
