# ##-----------------------file handling-------------------------------------------

# #  Q1

# f= open("myfile.txt","w")
# print("name of file :",f.name)
# print("file mode :",f.mode)
# print("readeble :",f.readable())
# print("writeable  :",f.writable())
# print("file closed  :",f.closed)
# f.close()
# print("file closed :",f.closed)

  #----------add data in file---------

# f = open ("myfile.txt","w")
# f.write("/n pune is smart city")
# f.write("/n nagpur is smart city")
# f.write("/n banglore is smart city")
# f.write("/n nashik is smart city")
# f.close()
# print("file operation is done")

# f = open ("myfile.txt","w")
# f.write("/n pune is smart city")
# f.close()
# print("file operation is done")

# f = open ("myfile.txt","a")
# f.write("/n pune is smart city")
# f.write("/n nagpur is smart city")
# f.write("/n banglore is smart city")
# f.write("/n nashik is smart city")
# f.write("/n indore is smart city")
# f.close()
# print("file operation is done")

#-----------------inserting list----------------------
# f=open("newfile.txt","w")
# mylist=["sakshi","divya","riya"]
# f.writelines(mylist)
# f.close()
# print(" done! ")

#----reading data----------
# f=open ("myfile.txt","r")
# print(f.read())
# f.close()


# with open("myfile.txt","w") as f:
#     f.write("sakshi/n")
#     f.write("divya/n")
#     f.write("riya/n")
#     print("file closed:",f.closed)
#     print("file closed:",f.closed)
     
# f1=open("file name","rb")
# f2=open("rossom.jpg","wb")
# data=f1.read()
# f2.write(data)

#------------csvfile---------------------
# import csv 
# f=open("student.csv","a",newline="")
# a=csv.writer(f)
# #a.writerow(["studentID","roll no","name","mobileno"])

# studentid=int(input("enter id:"))
# rollno=int(input("roll no:"))
# mobileno=int(input("enter mobile no:"))
# name=input("name:")
# a.writerow([studentid,rollno,name,mobileno])
# print("student record has save ")

# import csv 
# f=open("student.csv","a",newline="")
# a=csv.writer(f)

# studentid=int(input("enter id:"))
# rollno=int(input("roll no:"))
# mobileno=int(input("enter mobile no:"))
# name=input("name:")
# Pepar1=int(input(" P1 MARKS:"))
# Pepar2=int(input(" P2 MARKS:"))
# Pepar3=int(input(" P3 MARKS:"))
# email=input("email:")


# if Pepar1>40 and Pepar2>40 and Pepar3>40:
#     result="pass"
#     print(" u are pass")
# else:
#     result="fail"
#     print(" u are fail")

# total=Pepar1+Pepar2+Pepar3
# percentage= total/3

# a.writerow([studentid,rollno,name,mobileno,Pepar1,Pepar2,Pepar3,total,percentage,result])
# print("student record has save ")

#--------------------queue--------------------------------------------------------------------
import sys

class Queue:
    def __init__(self, queuesize):
        self.queuesize = queuesize
        self.myQueue = []

    def isFull(self):
        if len(self.myQueue) == self.queuesize:
            return True
        else:
            return False

    def isEmpty(self):
        if len(self.myQueue) == 0:
            return True
        else:
            return False

    def enQueue(self, value):
        if self.isFull():
            print("Queue is Full!")
        else:
            self.myQueue.append(value)

    def display(self):
        if self.isEmpty():
            print("Queue is Empty!")
        else:
            print(self.myQueue)

    def deQueue(self):
        if self.isEmpty():
            print("Queue is Empty!")
        else:
            print(self.myQueue.pop(0))        
     
    def frontPeek(self):
        if self.isEmpty():
            print("Queue is Empty!")
        else:
            print(self.myQueue[0])   

    def deleteQueue(self):
        self.myQueue=None  

size = int(input("Enter Queue Size: "))
queobj = Queue(size)

while True:
    print("1. EnQueue")
    print("2. Display")
    print("3. DeQueue")
    print("4. Front Peek")
    print("5. Delete Queue")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        queobj.enQueue(value)

    elif choice == 2:
        queobj.display()

    elif choice == 3:
        queobj.deQueue()

    elif choice == 4:
        queobj.frontPeek()

    elif choice== 5:
        queobj.deleteQueue()

    elif choice== 6:
        sys.Exit   

                


    

   