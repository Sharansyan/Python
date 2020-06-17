#entering the value of range
a,b = input().split(",") 
a= int(a)
b= int(b)

#saving the even values in the list1
list1 = []  
for i in range(a,b+1): 
  if i%2==0:
      list1.append(i)
     
# creating a new list which will have onlt even numbers(in elements too
list2 = [[i] for i in list]


'''
for i in range(len(list1)):
    x=list1[i]
    count1 = x.count('1')
    count3 = x.count('3')
    count5 = x.count('5')
    count7 = x.count('7')
    count9 = x.count('9')
    if count1>=1: 
        if count3>=1:
            if count5>=1:
                if count7>=1:
                    if count9>=1:
                        list1.remove(i)
'''

print(list1)
'''
# Python3 code to demonstrate  
# to convert list of string and characters 
# to list of characters 
# using list comprehension 
  
# initializing list   
test_list = [ 'gfg', 'i', 's', 'be', 's', 't'] 
  
# printing original list 
print ("The original list is : " + str(test_list)) 
  
# using list comprehension 
# to convert list of string and characters 
# to list of characters 
res = [i for ele in test_list for i in ele] 
  
# printing result  
print ("The list after conversion is : " +  str(res)) 
'''