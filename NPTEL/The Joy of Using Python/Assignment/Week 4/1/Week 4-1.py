# Your last recorded submission was :
a=input()
a=str(a)
az=a.count('0')
ao=a.count('1')

if(az==1 or ao==1):
    print('YES')
else:
    print('NO')



# Sample solutions (Provided by instructor)
A = input()
ls = []
li = str(A)
for j in li:
    ls.append(int(j))
count_z = 0
count_o = 0
for k in ls:
    if(k==1):
        count_o += 1
    if(k==0):
        count_z += 1

if((count_o == 1) or (count_z == 1)):
    print("YES")

else:
    if((count_o == 0) or (count_z == 0)):
        print("NO")
    else:
        print("NO")
