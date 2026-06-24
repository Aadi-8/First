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
