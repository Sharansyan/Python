# Your last recorded submission was :(Working)
n=int(input());
a=[list(map(int,input().split())) for i in range(n)];
for i in range(n):
  for j in range(n):
    end = '' if j == n-1 else ' ';
    if(i>=j):                          #the assignment was to print the lower triangular matrix .'. i>=j
      print(a[i][j], end=end);
    else:
      print(0, end=end);
  end = '' if i == n-1 else '\n';
  print('',end=end); 



# Sample solutions (Provided by instructor)
a = int(input())


m = []
for i in range(1,a+1):    
    l = list(map(int, input ().split ()))
    m.append(l)

for i in range(a):
    for j in range(a):
        if(i>=j):
            if(j==a-1):
                print(m[i][j], end="")
            else:
                print(m[i][j], end=" ")
        else:
            if(j==a-1):
                print(0, end="")
            else:
                print(0, end=" ")
    if(i!=a-1):
        print()
