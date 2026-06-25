

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
# if (__name__)=="__main__":
s1={2,4,56,78}
s2={1,3,4,69,99}
#s1 s2 is sets we can use union and intersection in sets and we can perform all set operation of maths
print(s1.union(s2))
print(s1.intersection(s2))
# s1.update(s2)        # this will update s1 with the union of s1 and s2
# print(s1)            #this will print updated s1 we can do same for intersecion
print(s1.pop())

# error handling 
#try and except meth
try :
    a = int("3")
    print(a)
except:
    print("wrong input")
l=[2,3,4,5,6]
try:
   print(l[7])
except:
    print("we do not get 4 ")

#importing modules
import os
# for i in range(1,6):                            #this make folder as many as we want 
#     os.mkdir(f'os module/dir{i}')
# os.rename("os module/dir3","os module/fol3")    #this renames the file or folder and we can also do like append creating file
# from Mod1 import s1                             #this import working automatically as we run this 

#File handleing

# with open("file.txt",'r') as f:
#     print(f.read())
#     f.seek(4)                              #changes the starting point
#     print(f.tell())                        #tell the starting point

# with open("file.txt",'w') as f:
#     f.write('wonderfull world')          #this delete everything and write the line we entered
# with open("file.txt",'a') as f:
#     print(f.write('\n wonderfull world \n'))    #add wonderfull world every time we run the code

#LAMBDA Function
sum = lambda x,y:x+y
avg = lambda x,y,z:(x+y+z)/3
square=lambda x:x*x
print(sum(3,4))
print(avg(2,4,6))
#MAP:FILTER:REDUCE
l=[2,3,4,5,6,7]
m=[9,2,6,2,3,4]
p = list(map(sum,l,m))
print(list(map(square,l)))               #we can take output as list,tumple or any iterable format
print(p)

print(tuple(filter(lambda x:x>3,l)))     #we can define function here also

from functools import reduce 

t = reduce(sum,l)                         #we have to import reduce
print(t)
