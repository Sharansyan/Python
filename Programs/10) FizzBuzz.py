x=input()
x=int(x)
for i in range(1,x+1):
    if(i%15==0):
        print(str(i)+" = FizzBuzz")
    else:
        if(i%3==0):
            print(str(i)+" = Fizz")
        else:        
            if(i%15==0 ):  
                print(str(i)+" = Buzz")
            else:
                print(str(i)+") ")
        
# or we can use
# def fizzbuzz(x):
# this will take input of x from the user