# Your last recorded submission was : (Wotking)
a=input()
a=str(a)
az=a.count('0')
ao=a.count('1')

if(az==1 or ao==1):
    print('YES',end="")
else:
    print('NO',end="")



# Sample solutions (Provided by instructor)
numbers = []

    
ls = []
x = input()
li = str(x)
for j in li:
    ls.append(int(j))
numbers.append(ls)


for j in numbers:
    count_z = 0
    count_o = 0
    for k in j:
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
        
