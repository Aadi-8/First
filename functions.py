

for i in range(2,9,3):
    print(i+3)
print("now while loop")  
a=5
while (a>0):
    print(a)
    a = a+1
    if (a==7):
        break
# to continue but skip specific
print("continue statement")
for b in range(1,3):
    print(b-1)
    if (b==2):
        print("dd")
        continue

print("functions")

def fun1(a,b):
        i=float((a*b)/(b-a))
        print(i)
#we can use if else in def 
fun1(8,13)
# using pass we can defin the function later and the code dont throw error
def fun2(a,b):
        pass

#fixed argument and return calling without print 
def fun3(a=3,b=5):
        return float((a+b)/2)  #return is a keyword not a veriable do not use = sign 
    
c=fun3(6,8)     #fun replace the value it is not bind to default value
d=fun3()        #for this the function use the default values
e=fun3(4)       #here a=4 and b i default 5
print(c)       
print(d)        
print(e)      

def fun4(*numbers):
        sum=0
        for i in numbers:
                sum = (sum + i)
        # t = (sum)/len(numbers)      # this should be indented in def 
        # print(t)                  we can use this but we are using return
        return sum/len(numbers)
f=fun4(2,3,7,8)
print(f)


l=[1,2,3,4,55]
print(l[4])

