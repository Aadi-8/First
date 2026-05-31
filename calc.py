#practicing python project calculator
a= int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(''' 
1=ADDITION
2=SUBTRACTION
3=MULTILICATION
4=DIVIDE''')

c = int((input("Enter the oprator: ")))

if (c==1):
    print(a+b)
elif (c==2):
    print(a-b)
elif (c==3):
    print(a*b)
elif (c==4):
    print(a/b)
else:
    print("invalid input")



