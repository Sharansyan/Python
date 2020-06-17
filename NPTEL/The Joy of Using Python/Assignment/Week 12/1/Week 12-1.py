# Your last recorded submission was :(Working)
N = int(input())
 
line = []
for i in range(N):
   line.append(input())
   
line = [i.upper() for i in line]
  
print('\n'.join(map(str, line)),end='')



# Sample solutions (Provided by instructor)
lines = []
n = int(input())
for i in range(n):
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print(sentence)
