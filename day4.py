# mylist=["sakshi",23,45,"sandip","foundation","nashik''mahiravani","trambak",89,987,"komal"]
# print(mylist) 
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])
# print(mylist[:])
# print(mylist[::-1])

# mylist=["sakshi",23,45,"sandip","foundation","nashik''mahiravani","trambak",89,987,"komal"]
# print(mylist) 
# mylist[2]="akshay"
# print(mylist)

# mylist=["sakshi",23,45,"sandip","foundation","nashik''mahiravani","trambak",89,987,"komal"]
# print(mylist) 
# if"ankush" in mylist:
#     print("yes")
# else:
#     print("not available")    

# mylist=["sakshi",23,45,"sandip","foundation","nashik''mahiravani","trambak",89,987,"komal"]
# print(mylist) 
# if"sandip" in mylist:
#     print("yes")
# else:
#     print("not available")     

# mylist=["sakshi",23,45,"sandip","foundation","nashik''mahiravani","trambak",89,987,"komal"]
# print(mylist) 
# mylist.append("riya")
# mylist.append("divya")
# print(mylist)

# mylist=["sakshi",23,45,"sandip","foundation","nashik''mahiravani","trambak",89,987,"komal"]
# print(mylist)
# mylist.insert(2,"riya")
# print(mylist)

# mylist.remove("sandip")
# print(mylist)

# newlist=mylist.copy()
# print(newlist)




# mylist=[["sakshi",23,45],["sandip","foundation","nashik''mahiravani"],["trambak",89,987,"komal"]]
# print("example of multidimensional list")
# print(mylist)
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[0][2])
# print(mylist[1][0])
# print(mylist[1][1])
# print(mylist[1][2])
# print(mylist[2][0])
# print(mylist[2][1])

# list1=[1,2,3,4,5]
# print(list1*2)

# list2=[8,9,10,11,12]
# print(list1+list2)

# list2=[8,9,10,11,12]
# del (list2[2])
# #del list2
# print(list2)

# list2=[8,9,10,11,12]
# list2.clear()
# print(list2)


# name="sakshi"
# print(name)
# myname=list(name)
# print(myname)

# mylist=[1,2,3,4,5]
# mylist.reverse()
# print(mylist)

# mylist=[1,2,3,4,5]
# mylist.sort()#---- asending order #for decending order use mylist.sort(reverse=True)
# print(mylist)

# mylist=[1,2,3,4,5]
# mylist.sort(reverse=True)
# print(mylist)

####alising
mylist=[3,4,5,6,7]
newlist=mylist
print(id(mylist))
print(id(newlist))
mylist[0]="sakshi" 
print(mylist)
print(newlist)
