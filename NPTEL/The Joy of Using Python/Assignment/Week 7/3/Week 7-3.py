# Your last recorded submission was : (Working)
m,n=map(int,input().split())
a=[list(map(int,input().split())) for i in range(m)];
b='YES';
for i in range(m):
  for j in range(n):
    if(a[i][j]!=0 and a[i][j]!=1):
      b='NO';
      break;
  if(b=='NO'):
    break;
print(b,end='')



# Sample solutions (Provided by instructor)
def isBinaryMatrix(mat,M,N): 
    for i in range(M): 
        for j in range(N): 
            # Returns false if element 
            # is other than 0 or 1. 
            if ((mat[i][j] == 0 or mat[i][j] == 1)==False): 
                return False; 
  
    # Returns true if all the  
    # elements are either 0 or 1. 
    return True; 

a,b=map(int,input().split())


m = []
for i in range(1,a+1):    
    l = list(map(int, input ().split ()))
    m.append(l)
if (isBinaryMatrix(m,a,b)): 
    print("YES")
else: 
    print("NO")
