

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


        
          


