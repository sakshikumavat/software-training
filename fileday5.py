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


with open("myfile.txt","w") as f:
    f.write("sakshi/n")
    f.write("divya/n")
    f.write("riya/n")
    print("file closed:",f.closed)
    print("file closed:",f.closed)
     

