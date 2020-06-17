# Your last recorded submission was : (Working)
x = input()
print(x.swapcase(),end = '')



# Sample solutions (Provided by instructor)
s = input()


def convert(ss):
    # Convert it into list and then change it
    newSS = list(ss)
    for i,c in enumerate(newSS):
        newSS[i] = c.upper() if c.islower() else c.lower()
    # Convert list back to string
    return ''.join(newSS)


print(convert(s))
