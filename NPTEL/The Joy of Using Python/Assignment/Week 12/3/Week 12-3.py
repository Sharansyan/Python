# Your last recorded submission was :(Working)
email = input()

index1 = email.index('@')
index2 = email.index('.')

print(email[index1+1:index2],end='')



# Sample solutions (Provided by instructor)
import re
emailAddress = input()
pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2,emailAddress)
print(r2.group(2))
