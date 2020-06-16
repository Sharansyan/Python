# Your last recorded submission was :
a=int(input("Enter size of the list \n"))

x=[]
print("Enter the elements of the list")

x=[int(x) for i in input.split()]

x.reverse()
y=x
ans=x+y
print(ans)



# Sample solutions (Provided by instructor)
N = int(input())
A = [int(i) for i in input().split(" ")]
B = []
for i in range(len(A)-1, -1,-1):
    B.append(A[i])
C = []
for i in range(len(B)):
    C.append(A[i]+B[i])
for i in range(len(C)):
    if(i==len(C)-1):
        print(C[i])
    else:
        print(C[i],end=" ")
