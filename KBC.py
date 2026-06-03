# we are going to create a KBC style interface

while True:
    print("QUESTION 1")
    l=["Capital of BIHAR ","1.Patna","2.Lucknow","3.Delhi","Capital of UTTAR PRADESH","Cpital of INDIA"]
    print(l[0])
    print(l[1])
    print(l[2])
    print(l[3])
    
    ans1=input("Enter your answer: ")
   

    match ans1:
        case "1":
            print('''CORRECT ANSWER
            you won 
            +500000 --------------------------------------->''')
            break
        case _:
            print('''wrong answer
            ---------------------------------->''')
            break  
while True:            
    print("QUESTION 2")
    
    print(l[4])
    print(l[1])
    print(l[2])
    print(l[3])

    ans2=input("Enter your answer: ")

    match ans2:
        case "2":
            print('''CORRECT ANSWER
            you won
            +500000 --------------------------------------->''')
            break
        case _:
            print('''WORNG ANSWER
             --------------------------------------->''')  
            break         

while True:            
    print("QUESTION 3")
    
    print(l[5])
    print(l[1])
    print(l[2])
    print(l[3])

    ans3=input("Enter your answer: ")

    match ans3:
        case "3":
            print('''CORRECT ANSWER
            you won
            +500000 --------------------------------------->''')
            break
        case _:
            print('''WORNG ANSWER
            ---------------------------------------->''')  
            break  
while True:

    i=int(input("Number of correct answers: ") )     
    match i:
        
        case 1:
            print("total amount you take home is : ",i*500000)
            break
        case 2:
            print("total amount you take home is : ",i*500000)
            break
        case 3:
            print("total amount you take home is : ",i*500000)
            break 
        case _:
            print("Enter a valid number")


