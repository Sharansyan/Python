# Your last recorded submission was :(Working)
def checkmissing(a): 
    l = len(a)
    sum_a = sum(a)
    total_a = (l+1)*(l+2)/2
    return total_a - sum_a

a = []
a = list(map(int , input().split()))
a.sort()
checkmissing(a)
print(int(checkmissing(a)),end="")



# Sample solutions (Provided by instructor)
# getMissingNo takes list as argument 
def getMissingNo(A): 
    n = len(A) 
    total = (n+1)*(n+2)/2
    sum_of_A = sum(A) 
    return total - sum_of_A 
  
# Driver program to test above function 
li=[]
li= list(map(int, input ().split ())) 
miss = getMissingNo(li) 
print(int(miss)) 
