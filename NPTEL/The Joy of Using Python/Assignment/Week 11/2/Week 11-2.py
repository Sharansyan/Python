# Your last recorded submission was :(Working)
word = []
word = list(map(str,input().split(",")))
word.sort()

for i in range(len(word)):
  if i<(len(word)-1):
  	print(word[i],end=",")
  else:
    print(word[i],end="")



# Sample solutions (Provided by instructor)
items=[x for x in input().split(',')]
items.sort()
print (','.join(items))
