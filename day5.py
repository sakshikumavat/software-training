##dictionary


#Q1
# mydict={
#     101: 'Amit',
#     102: 'Sumit',   
#     "103": 'Rohit',
#     "104": 'Sakshi',
#     "101": 'prashant',
#     102: 'sakshi',

# }
# print(mydict)
# print(type(mydict))

#Q2

# mydict={
#     101: 'Amit',
#     102: 'Sumit',   
#     "103": 'Rohit',
#     "104": 'Sakshi',
#     "101": 'prashant',
#     102: 'sakshi',

# }

# print(mydict)
# a=mydict[102]
# print(a)

#Q3

# mydict={
#     101: 'Amit',
#     102: 'Sumit',   
#     "103": 'Rohit',
#     "104": 'Sakshi',
#     "101": 'prashant',
#     102: 'sakshi',

# }

# mydict[102]="riya"
# print(mydict)

# Q4

# mydict={
#     101: 'Amit',
#     102: 'Sumit',   
#     "103": 'Rohit',
#     "104": 'Sakshi',
#     "101": 'prashant',
#     102: 'sakshi',

# }

# for x in mydict:
#     print(x)         #------by default looping statement access the key of dictionary

#     Q5

# mydict={
#     101: 'Amit',
#     102: 'Sumit',   
#     "103": 'Rohit',
#     "104": 'Sakshi',
#     "101": 'prashant',
#     102: 'sakshi',

# }

# for x in mydict.values():
#     print(x)         #------by default looping statement access the values of dictionary


   # Q6

# mydict={
#     101: 'Amit',
#     102: 'Sumit',   
#     "103": 'Rohit',
#     "104": 'Sakshi',
#     "101": 'prashant',
#     102: 'sakshi',

# }

# for x,y in mydict.items():
#     print(x,y)         #------by default looping statement access the key and values of dictionary  


#Q7    

# mydict={
#     101: 'Amit',
#     102: 'Sumit',   
#     "103": 'Rohit',
#     "104": 'Sakshi',
#     "101": 'prashant',
#     102: 'sakshi',

# }

# mydict['mobile']="1234567890"
# print(mydict)  #------add new key and value in dictionary

# Q8

# mydict={
#     101: 'Amit',
#     "proffesion": 'engineer',
#     "city": 'Delhi'
# }
# mydict.pop("proffesion")
# print(mydict)  #------remove key and value from dictionary

# Q9

# mydict={
#     101: 'Amit',
#     "proffesion": 'engineer',
#     "city": 'Delhi'
# }
# newdict=mydict.copy()
# print(newdict)  #------create a copy of the dictionary

#Q10


# mydict={}


#  #------create a dictionary using dictionary comprehension
# if mydict=={}:
#     print("dictionary is empty")
# else:
#     print(mydict)

#Q11



# mydict={"A":50,"B":60,"C":70}
# print("maximum value key is:",
#       max(mydict.keys()))  #------find maximum value in dictionary

#Q12
# mydict={"A":50,"B":60,"C":70}
# print("minimum value key is:",
#       min(mydict.keys()))  #------find minimum value in dictionary
 
#Q13

# mydict={"A":50,"B":60,"C":70}
# print("mydict.reverse () is:",dict(reversed(list(mydict.items()))))  #------reverse the dictionary

#Q14

# mydict1={"A":50,"B":60,"C":70}
# mydict2={"A":50,"D":60,"E":70}
# if mydict1.keys() & mydict2.keys():
#     print(" key:",mydict1.keys() & mydict2.keys())  #------compare two dictionary keys
# else:
#     print("both dictionary keys are not same")  #------compare two dictionary keys





#array---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Q1 

# def linearSearch( array,target):
#     for i in range(len(array)):
#         if array[i]==target:
#           return i
        
#     return -1

# array=[1,2,3,4,5,6,7,8]
# target = 9
# result = linearSearch(array,target) #calling function
# if result!=-1:
#    print("element found=",result)
# else:
#    print("element not found")
   

def linearSearch(array):
    for i in range(len(array)):
        if array.max & array.min:
            print(max & min)
    



