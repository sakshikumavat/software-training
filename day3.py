

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     result = a / b

# except (ValueError, ZeroDivisionError) as message:
#     print("Enter valid number:", message)

# except:
#     print("This is default exception")

# else:
#     print("All OK")
    

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     result = a / b

# except (ValueError, ZeroDivisionError) as message:
#     print("Enter valid number:", message)
# finally:
#     print("i will always excuted")


# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     try:
#         print = a / b

#     except  ZeroDivisionError as message:
#      print( message)
# except ValueError as message:
#     print( message)


# try:
#      a = int(input("Enter a number: "))
#      b = int(input("Enter another number: "))
#      result = a / b

# except (ValueError, ZeroDivisionError) as message:
#      print("Enter valid number:", message)

# except:
#      print("This is default exception")

# else:
#      print("All OK")
# finally:
#      print("i will always excuted")     

# bank_balance = 1000
# if bank_balance < 2000:
#     raise Exception("Insufficient balance")
# else:
#     print("You can withdraw money")

# import logging

# logging.basicConfig(filename="log.txt", level=logging.DEBUG)
# logging.debug("This is debug message")
# logging.info("This is info message")
# logging.error("This is error message")
# logging.warning("this indicates warning info")
# logging.critical("this indicates critical info")  
# 
# import logging
# logging.basicConfig(filename="log.txt", level=logging.DEBUG)

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     result = a / b
# except (ValueError, ZeroDivisionError) as message:
#     print(message)
#     logging.exception(message)
# print("This is default exception")        

# phy=int(input("Enter marks of physics: "))
# chem=int(input("Enter marks of chemistry: "))
# math=int(input("Enter marks of maths: "))
# total=phy+chem+math
# percentage=total/3
# print("Total marks:", total)
# print("Percentage:", percentage)

# if phy>=40 and chem>=40 and math>=40:
#     print("You are pass")   
# else:
#     print("You are fail") 

# gender=input("Enter your gender like M/F: ")
# if percentage>=65 and gender=="M":
#     print("You are pass with first class")
# else:
#     print("You are not eligible for first class")

# import sys


# def addition():
#     a=int(input("add value of a:"))
#     b=int(input("add value of b:"))
#     print(a+b)

# def subtraction():
#     a=int(input("add value of a:"))
#     b=int(input("add value of b:"))
#     print(a-b)  

# def division():
#     a=int(input("add value of a:"))
#     b=int(input("add value of b:"))
#     print(a/b) 

# def multiplication():
#     a=int(input("add value of a:"))
#     b=int(input("add value of b:"))
#     print(a*b)      


# while True:

#     print("1.addition")
#     print("2.subtraction")
#     print("3.division")
#     print("4.multiplication")
#     print("exit")
   
#     choice=int(input("enter your choice :") )
#     if choice ==1:
#         addition()
#     elif choice==2:
#         subtraction()
#     elif choice==3:
#         division()
#     elif choice==4:
#         multiplication()

#     elif choice==5:
#         sys.exit()
 # stack implimentation with size limit              
#stack implementataion with size limit
# import sys

# class Stack:
#     def __init__(self, size):
#         self.size = size
#         self.stack = []

#     def push(self, value):
#         if len(self.stack) == self.size:
#             print("Stack is Full")
#         else:
#             self.stack.append(value)
#             print("Pushed:", value)

#     def pop(self):
#         if len(self.stack) == 0:
#             print("Stack is Empty")
#         else:
#             print("Popped:", self.stack.pop())

#     def peek(self):
#         if len(self.stack) == 0:
#             print("Stack is Empty")
#         else:
#             print("Top Element:", self.stack[-1])

#     def display(self):
#         if len(self.stack) == 0:
#             print("Stack is Empty")
#         else:
#             print("Stack:", self.stack)

#     def deleteStack(self):
#         self.stack.clear()
#         print("Stack Deleted")


# size = int(input("Enter stack size: "))
# obj = Stack(size)

# while True:
#     print("\n1.Push")
#     print("2.Pop")
#     print("3.Peek")
#     print("4.Display")
#     print("5.Delete Stack")
#     print("6.Exit")

#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         value = int(input("Enter value: "))
#         obj.push(value)

#     elif choice == 2:
#         obj.pop()

#     elif choice == 3:
#         obj.peek()

#     elif choice == 4:
#         obj.display()

#     elif choice == 5:
#         obj.deleteStack()

#     elif choice == 6:
#         sys.exit()

#     else:
#         print("Invalid Choice")

# stack implementation with size limit
# import sys

# class Stack:
#     def __init__(self, stackSize ):
#          self.stackSize = stackSize # stack size define
#          self.myStack =[] #list represent stack
#          print("Stack has created")
         
#     def isFull(self):
#         if len(self.myStack) == self.stackSize:
#             return True
#         else:
#             return False
        
#     def isEmpty(self):
#         if self.myStack ==[]:
#             return True
#         else:
#             return False
        
        
#     def push(self,value): # user define parameter using push method
#         if self.isFull():
#             print("Stack is Full")
#         else:
#             self.myStack.append(value)
    
#     def display(self):
#         if self.isEmpty():
#             print("Stack is Empty")
#         else:
#             print("Stack =",self.myStack)
            
#     def pop(self): #pop method 
#         if self.isEmpty():
#             print("Stack is Empty")
#         else:
#             print(self.myStack[-1]) 
            
#     def peek(self):
#         if self.isEmpty():
#             print("Stack is Empty")
#         else:
#             print(self.myStack[-1])
            
#     def deleteStack(self):
#         self.myStack = None   
#         print("Stack is deleted")                     
            
    
# size = int(input("Enter The size of stack :"))
# obj = Stack(size)

# while True:
#     print("1.Push")
#     print("2.Display")
#     print("3.Pop")
#     print("4.Peek")
#     print("5.Delete Stack")
#     print("6.Exit")
#     choice = int(input("Enter Your choice"))
#     if choice == 1:
#         value = int(input("Enter the value to push in stack")) # 
#         obj.push(value)# push method 
#     elif choice == 2:
#         obj.display()# display method 
#     elif choice == 3:
#         obj.pop() # pop method 
#     elif choice == 4:
#         obj.peek()
#     elif choice == 5:
#         obj.deleteStack()
#     elif choice == 6:
#         sys.exit()
# print("prashant777".isalnum())
# print("prashant".isalpha())
# print("777".isdigit())
# print("prashant".islower())
# print("PRASHANT".isupper())
# print(" My Name is prashant777".istitle())
# print(" ".isalnum())
# print(" ".isspace())
# print("HELLO".startswith("HE"))
# print("HELLO ".endswith("LO "))

#membership operator
# 1.in 2.not in

#from os import name


# Name="help4code"
# print("h" in Name)
# print("z" in Name)
# print("z" not in Name)

#for(initialization; condition;ince/dec)
# for i in range(1,5):
#     print(i)

# for i in range(5):
#     print(i)    

# for i in range(5,0,-1):
#     print(i)

# for i in range(1, 11):
#     print(i*2," ",i*3," ",i*4," ",i*5," ",i*6," ",i*7," ",i*8," ",i*9," ",i*10)
#     print("---------------------------------------------------")    
#     for j in range(1, 11):
#         print(j*11,"",j*12,"",j*13,"",j*14,"",j*15,"",j*16,"",j*17,"",j*18,"",j*19,"",j*20)

# list3=[1,2,3,4,5]
# for i in list3:
#         print(i)

# list=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# for x in list:
#     sum=sum+x
# print("sum of list is:",sum)    


# mycart=[10,20,300,450,800,70,700]
# for i in mycart:
#     if i>400:
#         print("item is not available")
#         break 
#     print(i)

#     mycart=[10,20,300,450,800,70,700]
# for i in mycart:
#     if i>400:
#         print("item is not available")
#         continue
#     print(i)

count=0
for i in range(9):
    if i%2==0:
        print(i)
    else:
        print(i)
        count+=1
print("count of odd number is:",count)