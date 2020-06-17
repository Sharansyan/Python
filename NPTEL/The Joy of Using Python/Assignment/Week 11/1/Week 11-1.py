# Your last recorded submission was : (Working)
import math 

c = 50
h = 30
d =[]
d = list(map(int, input().split(",")))

result = []

for i in range(len(d)):
    ans = (2*c*d[i]) / h
    result.append(math.sqrt(ans))

result1 = [round(num) for num in result]

for i in range(len(result1)):
  if i<(len(result)-1):
    print(result1[i],end=",")
  else:
    print(result1[i],end="")



# Sample solutions (Provided by instructor)
import math
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print (','.join(value))
