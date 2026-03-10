# print("Hello World") 
# print(2)
# print(2)
# print("2") 
# print(3*2) 
# print('4/2')
# #comments are used to explain what ur code does or to make ur code more readable. python skips this line when running the code.
# # rules for variables names
# # 1. variable names can contain letters, numbers and underscores
# # 2. variable names  cannot start with a number
# # 3. variable can only contain alphanumeric characters and underscores (A-z, 0-9, and -)
# # 4. variable names are case sensitve (age,Age and AGE are three different variables)
# # 5. variable names cannot be a reserved word (like print, for, if,)
# #x=5
# #name="john"
# #age=25
# #isstudent=True
# #print('My name is', name, age, x, isstudent)
# #a = 2
# #b = 3
# #sum = a + b
# #print("sum=", sum)
# #print("difference =", a-b)
# #print("product=", a*b)
# #print("division=", a/b)
# #print("Floor Division =", a // b)
# #print(round(a/b))
# #print("sum=", sum, "difference =", a-b, "product=", a*b, "division=", a/b)
# #print("Division=", 18/4)
# #print("5^2=", 5**2)
# #print("remainder=", 18 %4)
# x=5
# print("x is", x)
# x="My name is Mikiyas"
# print(x)
# x = True
# x = 5
# x = 3.14
# print(x)

# myNumber=10
# print("type of myNumber", type(myNumber) )
# #strings - anything inside single or double quotes
# #booleans - true or false
# #integers - +/- whole numbers
# #float - desimal numbers
# """this is a multiline comment 
# test test test """
# # strings are immutabley ="hello" 
# y="hello" #mello
# #y[o]="m"
# #print(y) this will give an error because strings are immutable
# z="m" + y[1:]
# print(z)
# #mylist=[1,2,3,4,]
# #y[0]= 5
# #print(y)
# #string operation
# # 1 concatination combining 2 or more items together 
# #syntax obj1 + obj2 + obj3.....
# name1 ="abebe" 
# name2 ="kebede"
# print(name1 + " " + name2) #abebe kebede
# mynum =5 
# print (name1 + " " + str(mynum))#abebe 5
# print(name1, mynum) #abebe 5
# print(name1, mynum, sep="_") #abebe_5
# u='1'
# i=2
# print(u+str(i))
# print(int(u)+i)
# print(u,i,'hello')
# # syntax type(obj)
# print(type(1.5))
# print(type("1.5"))
# print(type(True))
# print(type(None))
# #casting - converting one data type to another data type
# # for strings if the string is not "" => true else => false
# # syntax str(obj), int(obj), float(obj), bool(obj)
# name= "Abdi"
# age=30
# hobby="playing soccer"
# fav_animal= "dog."
# print("My name is "+ (name)+", I am "+ str(age) + " years old."+"and as a hobby i love " +(hobby)+ " and my favorite animal is " + (fav_animal))
# print(f"My name is {name}, I am {age} yearsold, and as a hobby i love {hobby} and my favorite animal is {fav_animal}") # f string
# number=5 
# print(f"My favorite number is {number*2}")
# print("My favorite nymber is "+str(number*2))
# print("My favorite number is",number*2)
# #2 Repetition you can repeat a string multipe times using * operation
# str1=" hello"
# print(str1 * 3)
# print((str1+" ") * 3)
# print((str1+" ") * 2 +"hello")
# #strip
# print((str1*3).strip())
# print("  hello world  ".strip()) 
# m="100"
# n=10.5
# o=30
# #boolean "", none, 0, 0.0, [], {}, () are considered False other True when performing bool operation on them
# print(float(m)+n+float(o))
# print(bool(0))
# print(bool(1))
# print(bool("no"))
# print(bool(-5))
# print(bool("false"))
# print(bool(""))
# print(bool(None))
# #casting and type
# t="123"
# i=int(t) + 5
# print(i)
# print(type(i))
# # 3 indexing - accessing individual characters in a string - []
# # 0 1 2 3 4 5 6 7 8 9 10
# # h e l l o   w o r l d
# #-11-10-9-8-7-6-5-4-3-2-1 
# mystring="hello world"
# print(mystring[5])
# print(mystring[-6])
# print(mystring[1])
# print(mystring[-1])
# print(mystring[-11])
# print('print first 5 characters', mystring[:5])
# #print(mystring[20])shows error because we dont have 20 index
# print('hello'[2])
# 4 Slicing -- use to extract a substring from a string using slicing
# default of step is 1 - dont skip any characters
# start index- inclusive. optional so if not specified - default to 0
# end index - exclusive. optional so if not specified - default to length of string 
# no start index means start from beginning
# no end index means go to the end
# [0,6) => [1,2,3,4,5]
# syntax is myvar[start:end:step.]
# start end step all are optional
# str8="python1programming"
# print(str8[0:6])
# print(str8[0:6:1])
# print(str8[:6])
# print(str8[7:18])
# print(str8[7:])
# print(str8[0:])
# print(str8[0:6:2])
# print(str8[0:15:2])
# print(str8[::])
# print(str8[-1:-3])
# print(str8[0:])
# print(str8[-1:]) 
# print(str8[:-1])
# print(str8[:-1] + str8[-1])
# #5 Length : to determine the length of a string using the len() function
# print("length",len(str8))
# # string methods
# # lower(): convert the string to lowercase sntax strvar.lower()
# # upper(): convert the string to uppercase sntax strvar.upper()
# str9="python programming"
# print(str9.upper())
# print(str9.lower())
# # title - convert first letter of each word to uppercase
# print(str9.title())
# print("python programming".upper())
# print(str9[0:2]+str9[2].upper()+ str9[3:])
# #  strip(): removes leading and trailing whitespace from string #syntax strvar.strip()
# str01="  python programming  "
# print(str01.strip())
# print(len(str01.strip()))
# print(str01.lstrip()) #.lstrip()= left strip removes only leading whitespace
# print(len(str01.lstrip()))
# print(str01.rstrip()) #.rstrip()= right strip removes only trailing whitespace
# # split(): split the string into a list of substrings based on specified separator 
# #syntax strvar.split(separator)
# # return a list of substrings
# # separator - the character i want to split the string on. default is whitespace
# str02="apple, banana, cherry, pear"
# print(str02.split(","))
# print(str02.split())
# print(str02.split('n'))
# # maxsplit- optional- how many times the  split happens. default is -1
# print(str02.split(",",1))
# print("With max split",str02.split(",",1))
# print("With max split",str02.split(",",2))
# str03="1 2 3 4 5"
# print("With max split",str03.split(" ",2))
# sen="if you show me your wounds, i'll know where my care matters most."
# con=(sen[0:3] + sen[-3:])
# print(con)
# upper=con.upper() #uppercase
# print(upper)
# print(upper*2)    #upper*2
# print((upper*2)[4:10]) #slicing
# lower=((upper*2)[4:10]).lower() #lowercase
# print(lower)
# print('length',len(lower)) #length
# section 2
# accepting input from the user
# input
# syntax input(<promptstring>)
# return value is always a string
# age = input("Enter your age:")
# print(age)
# print(type(age))
# x, y=input ("enter two numbers separated by spaces:").split()
# print("Y=",y)
# print("X=",x)
# celsius = float(input("Enter temprature in Celsius:"))
# fahrenheit=(celsius * 9/5) + 32
# print("Temprature in Fahrenheit",fahrenheit)
# relational operators/comparatin operators used to compare value. return boolean value true or false
# <,>,>=,<=,== is equal to,!= is not eqaul to
# c=2
# d=3
# print(c < 3)
# print(c ==2) #Equality check
# print(c != d)
# print ( d > c)
# Assignment operators
# = assignment
# += addition assignment
# -= substraction  assignment
# *= multiplication ass
# /= division ass
# %= modulus ass
# A=5
# A += 3 # A=A+3
# A -= 3 #A=A-3
# A *= 3 #A=A*3
# A /= 3 #A=A/3
# A %= 2 
# logical operators used to combine and manipulate boolean values
# AND return true if both statements are true
# OR return true if one of the statements are true
# NOT reverses the result
# print(c<5 and d>10)
# print(c>d or c <= d)
# print(c > d or c<= d)
# # # not
# print(not(c<5 and d>10))
# print(not(c>d or c <= d))
# print(not"")
# print(not" ")
# conditional statements used to control the flow of the program if,elif(else if), and else
#if condition1:
# code to ececute if condition1 is true
# elif conditon 2
# code to ececute if condition1 is false and condition2 is true
# else:
# #code to excute if both condition1 and condition2 are false

# age=15
# if age <=16: #example1
#     print("you are a teenager")
# elif age > 16 and age <= 60:
#       print("you are an adult")
# else:
#     print("you are a senior")
# if age >18: #example2
#     print("You are eligible to buy alcohol")
# elif age<18:
#     print("you can't buy alcohol")
# else: 
#      print("You are not eligible to buy alcohol") #example3
# print(("u can drink") if age>=18 else ("no"))


# syntax value if condition is true if <condition> else <value if false>
# f=5
# h=10
# print("f is greater") if f>h else print("h is greater")
# num=int(input("enter a number"))
# if num > 0:
#   print("postive number")
# elif num==0:
#     print("zero")
# else:
#     print("negetive number")    
# num=int(input("Enter a number:"))
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")
# or print(f"{num}is even") if num % 2 == 0  else print(f"{num} is odd")

# celsius=float(input("enter temprature in celsius:"))
# franite=(celsius*9/5+32)
# print(f"the temprature in faranite is:",franite)
# nested conditionals is refer to one conditional statement is nested with in another conditional statement.
# num = int(input("enter a number:"))
# if num >= 0:
#     if num==0:
#         print("zero")
#     else:
#         print("posetive number")
# else:
#     print("negetive number")
# age=int(input("enter ur age"))
# isstudent=(input("Are you student? Y/N")).upper()
# if age>= 18:  
#     if isstudent=="Y":
#           ticketprice =10
#     else:
#               ticketprice =15
# else:
#   if isstudent=="Y":
#    ticketprice = 8
#   else: 
#     ticketprice = 12
# print("your ticket price is $" + str( ticketprice))
#  section 3 loops in python --for loop and while loop they allow u something to repeat over over and again
# while loop in python 
# used to excute a block of statements repeatedly until a given condition is satisfied
# syntax while<condition>:
#             #  <statements>
# i=0
# while i < 5:
#     i += 1 #i=i+1
#     if i==3:
#       continue
#     print(i)
# print("loop ended")
# # break - used to exit out of a while/for loop
# while i<5:
#      print(i)
#      if i==3:
#         break
#      i +=3
# else:
#     print("loop ended")
# print("outside of while loop")    
# count=0
# while (count<3):
#     count=count+1
#     print("hello geek")
# else:
#     print("in else block")
# # continue - used to skip the current iteration of the loop
# i = 0 
# while i<6:
#     i +=1
#     if i==3:
#         continue   
#     print(i)
    
# else:
#   print("loop ended")
    
# for loop
# syntax for<varname> in <iterable>:iterable can be a string ,list, tuple, dictionary,range set etc
#            <statements>
# mystr="hello world"
# for x in mystr:
#         print(x)
# for z in [1,2,3,4,5]:
#   print(z)
# y=["yan","miki","dagi"]
# for v in y:
#   print(v)
  # range generate a sequence of number
  # range (start, stop, step)
  # range(0,5)=[0,1,2,3,4]
  # start(optional)-position to start from. defaults to 0 (inclusive)
  # end(required) - position to stop at.(not inclusive)
  # step(optional)- the amount it should increment by .default to 1


# print()

# print("range with for")
# for o in  range (5):
#     print(o)

# for x in range(3, 10, 2):
#     print(x)


# print()
# b="python"
# for x in b:
#   if x=="t":
#     continue
#   print(x) 
# else:
#   print("finished")
# print("nested while")
# x=[1,2]
# y=[4,5]
# i=0
# j=0
# while i < len(x):
#   while j < len(y):
#     print(x[i],y[j])
#     j+=1
#   i+=1 
#   j=0

# print()
# print("For Loop")
# x = [1, 2, 3, 4, 5]

# for ab in x:
#     print(ab)

# y = ["Abraham", "Kefyalew", "Kaleab"]
# for z in y:
#     for a in x:
#         print(z, a)
# section4
# python set - is the collection of the unordered items. each elements in the set must be
# unique, immutable, and the set remove the duplicate elements
# set are mutable which means we can modify it after its creation
# myset ={True,1, 2, 1, "a", False} # boolean 0/False 1/True 
# print(myset)
# myset={1, "test", True, "python"}
# print(myset)
# myset2={"a",0, "",3.14, (1,3),"False", 27, False}
# print(myset2)

# # sets - unordered, unique, mutable
# # elements in the set must be immutable
# # immutable datatypes - strings, numbers, tuples
# # mutable- lists , dictionaries
# # set uses for unique ids
# # syntax for set  curly braces {} or set(iterable)
# myset3=set((True, 2, 1, 1, "a", False))
# print(myset3)
# # empty set =set()  not by {} cause this represent dictionary
# # {item1, item2,...} - creat a set
# # set(iterable1, iterable2...)- creat a set
# # set()- also to cast to set
# x=set()
# print(type(x))
# y={}
# print(type(y))
# z=set([1,2,"Test", "M", "F","Sunday"])
# print(z)
# r=[1,2,3,4]
# a=set(r)
# print(a)
# print(type(a))
# # adding items to set
# # add() to add a single item to the set
# aa={0, 4 , 6 , True}
# aa.add(9)
# print(aa)
# # update() to add multiple item to the set
# weeks={"monday", "tuesday", "wednesday"}
# months={"jan", "feb"}
# weeks.update(months)
# print(weeks)
# month3=[1,2,3] #list
# weeks.update(month3)
# print("Adding list to a set", weeks)
# weeks.update((10,21)) #tuple
# print("adding tuple to set", weeks)
# print()
# weeks.update("cd") # update splits the string to indivitual character
# print("adding string to set", weeks)
# weeks.add("cg") # add puts it as it is  
# print(weeks)
# print()
# #removing items from the set
# # discard() function if the item does not exist in the set then the set remain unchanged 
# # remove() where this one shows an error
# # discard
# weeks.discard("cg")
# print("After discarding", weeks)
# weeks.add("cg")
# weeks.remove("cg")
# print("After remove",weeks)
# # better to use .remove().... list =[] square bracket, tuples=() paranteses, set={} curly braces
# # .clear() to clear the set
# print()
# weeks.clear()
# print("after clearing the set", weeks)
# # del use to delet things item or anything
# # del weeks
# # print(weeks)
# # checking if item exists - in, not in
# print()
# set1={"monday", "tuseday", "wednesday"}
# if "thursday" not in set1:
#   set1.add("thursday")
# else:
#   set1.add("friday")
# print(set1)

# print("thursday"in set1)
# print("thursday"not in set1)
# print()
# sample_set={"Yellow", "Orange", "Black"}
# # ex.1 add a list of elements to a set
# colors=("Green","White")
# sample_set.update(colors)
# print("adding new items to the set",sample_set)
# # ex2 remove item orange from the set
# sample_set.remove("Orange")
# print("set with out orange item",sample_set)
# print()
# # set opreration
# # union of two sets to combine two or more sets into one set in python use the union() function.
# # syntax set1.union(set2, set3,...)
# # <iterable>.union(iterable)
# # | - union - set1 | set2 |set3
# E={"monday","tuesday","wed"}
# F={"wed","thursday"}
# G={"friday","saturday","sunday"}
# result=E.union(F,G)
# print(result)
# D=[1,2,3]
# print(E.union(D))
# set1={1, 2, 3}
# set2={"a", True, 3, 3.14}
# print(set1 | set2)
# print()
# # the intersection of two sets - only the items in all sets being compared are included in the final set
# # syntax set1.intersection(set1, set2,...)
# # set1 & set2 & set3..... - & intersection symbol, if we use & all types need to be the same data type 
# Q={1,2,3,4,5}
# W={3,4,5,6}
# S=[3,5,6,7]
# print(Q.intersection(W))
# print(Q.intersection(W,S))
# print(Q & W)
# # print(Q & W & S) raises error, need to be same data type 
# A={1,2}
# B={3,4}
# print((A & B))
# myset6={"a", "b", "c"}
# myset7="bcdef"
# print(myset6.intersection(myset7))
# myset6.add("gh")
# print(myset6)
# myset6.update([1,2,3],"19")
# print(myset6)
# # iterable list, string, dic
# print()
# # the intersection_update() method
# # intersection but doesnot return a new set, rather it operates on the original set
# # set.intersection_update.()
# p={1,2,3,4}
# y={2, 3, 5}
# print(p)
# p.intersection_update(y)
# print(p)
# print()
# o={1,2,3,4,5}
# f={2,3,4}
# v={3,4,7}
# o.intersection_update(f,v)
# print(o)
# print(v)
# print()
# r={1,2}
# j=set()
# x=(r.intersection_update(j))
# print(x)
# print("r",r)
# j.intersection_update(r)
# print("j",j)
# print()
# # differences syntax set1.difference(set2,set3..)
# # A - B => must be the same data type
# A={"monday","tuesday","wednesday"}
# B={"tuesday","wednesday"}
# V={"saturday"}
# C=set()
# D=[1,2,3]
# print(1,A.difference(B)) #1
# print(2,B.difference(A)) #2
# # print(D.difference(A)) shows erorr because difference works only when the set comes first
# print(3,A.difference(C)) #3
# print(4,C.difference(A)) #4
# print(5,A.difference(V,D)) #5
# print(len(A.difference(V,D)))
# print()
# # python dictionary
# # represenet by{key: value, key: value} {} curly braces
# # dic keys must be immutable - tuples, string, int, booleans, etc
# # mutable - lists, sets, dict
# # ordered, changable, do not allow duplicates
# # dict(key=value, key=value,.....)
# student={
#          "name":"alex",
#          "id":1,
#          "gender":"male",
#          "name":"kefyalew",
#          "gender":"female",
#          True:"female",
#          (1,2):"test",
#          2:"two"
#                      }
# student["name"]="kal"
# print(student)
# print(type(student))
# student["Departement"]="IT"
# # accesssing item in dictionary -[]
# print(student["name"])
# # print(student["age"]) shows key error
# student["age"]=12
# print("After Adding age",student)
# print()
# student2=dict(Name="tigi", id= 8, one="one")
# print(student2)
# student2.update({"id":22,"Name":"test","department":"it"})
# print(student2)
# x=student2.get("Name2", "id") #if the value "Name2" doesnt exist it gives "id"
# print(x)
# print()
# # delete key
# employee={"Name":"Abraham","Age":24, "Gender":"M"}
# del employee["Gender"]
# print(employee)
# # employee.clear() # to clear everything
# print(employee)
# print(len(employee))
# print()
# # del  employee #deleteing the variable
# # print(employee) # gives erorr
# # pop(key)- removes a specific key value pair
# # default(optional)- value to use if the key does not exist i.e if u dont want yo throw
# # an error you can assign a default value
# y=employee.pop("Age") 
# print(y)
# u=employee.pop("x","not found")
# print(u)
# print(employee)
# print()
# # iterating dictionary 
# stu3={
#          "name":"alex",
#          "id":1,
#          "gender":"male",
#          "name":"kefyalew",
#          "gender":"female",
#          True:"female",
#          (1,2):"test",
#          2:"two"
#                    }
# print("print only key")                  
# for x in stu3:
#     print(x)
# print()
# print("print key value pairs")
# for x in stu3:
#   print(x,stu3[x])
# print()
# print("key and only one item for all")
# for x in stu3:
#   print(x,stu3["name"])
#   print()
# print()
# # length to count the length of dictionary
# print("length of a ditctionary",len(stu3)) 
# print()
# keys=list(stu3.keys()) #['name','id','gender']
# i=0
# while i < len(keys):
#   key=keys[i]
#   value=stu3[key]
#   print(key, value)
#   i +=1
# print()
# # explictly tell it to give you only the keys
# print("printing only the keys")
# for x in stu3.keys():
#   print(x)
# print()
# # printing only the value
# print("printing only the values")
# for x in stu3.values():
#   print(x)
# print()
# # printing both the value
# print("printing both the values")
# for x in stu3:
#   print(x,stu3[x])
# print()
# # .item() - printing both key value pairs items property
# print("printing both key value pairs items property")
# for x, y in stu3.items():
#   print(x,y)
print()
# python function a function is a block of code which only runs when it is called
#  you cam pass data known as a parameters into a finction
# a function can return a data as a result
# syntax def <functionname>(parameter1, parameter2, parameter3 etc)    function name has no space  parameter are optional
def printfullname(firstname, lastname): #parameters
    print(f"My name is {firstname} {lastname}") 
    print(firstname+" "+lastname)
    x=2
    print(x+2)
def printcar(car,model):
    print(f"this {car} car model is {model}" )
def printhello():
    return "hello world!!!" 
def add(a,b):
    return a + b

printfullname("john","doe" ) # arguments # calling the function
printfullname("jane", "doe")
printcar("bmw","1996") #the number of the arguments must match the parameters

x=add(2,3)
print(x)
print(add(2,3)) #or
print(add("ayele"," abdi")) 
if x >5:
  print("greater than 5")
else:
  print("less than or equals to 5")
print(printhello())
print()
# arbitary arguments, *args
# if we dont know how many arguments that passed into our function
# * infront of parameter name denotes arbitary parameter since we dont know how many arguments 
#  we are passing
def my_function(*kids):
    print(type(kids))
    print(kids)
    print("the youngest child is "+(kids[2]))
    print("the youngest child is "+str(kids[2]))
    for x in kids:
      print(x)
my_function("abebe","kebede","dani")
def operation(num1,num2):
    return(num1+num2,num1-num2,num1*num2,num1/num2)
result=operation(2,3)
print("result",result)
print("sum",result[0])
print("difference",result[1])
print()
# keyword arguments
# we can also send arguments with key = value syntax
def students(st1, st2, st3):
    print("student 2",st2)
students("Alex", "kefyalw", "kalab")
students(st2="Alex",st3="kefyalw",st1="kalab")
students(st3="Alex", st1="kefyalw",st2 = "kalab")
print()
def printstudnetnames(students):
    for x in students:
     print(x)
printstudnetnames(["Alex","kefyalw","kalab"])
def sumofnumbers(numberslist):
  total=sum(numberslist)
  return total
total1=sumofnumbers([1,2,3,4,5])
print("the sum of my numbers is ", total1)
print("the sum of my numbers is ", sumofnumbers([1,2,3,4,5])) #or
print()
# Arbittary keyword args, **kwargs
def myfunction(**kid):
   print(type(kid))
   print("his last name is"+kid["lname"])
   for key, val in kid.items():
    print(key,val)
myfunction(fname="tobias",lname=" refs")   
print()
# default parameter value the deafult must come last
# combination of postiton + default arguments
def  printfirstnames(lastname,fname= "jones"):
    print("first name " + fname.title())
    print("Last name ", lastname.title())
printfirstnames("michael")
printfirstnames("michael","smith")
printfirstnames(fname="michael",lastname="smith")
print()
def nationality(name):
  if name=="kefyalew":
    return "Ethiopian"
  elif  name=="john":
    return "American"
  else:
     return "unknown"
print("nationality",nationality("kefyalew"))
print("nationality",nationality("john"))
print()
#passing a list as an arguments
def printfruitnames(fruit):
    fruit.append("pear")
    return fruit
fruits=["apple","banana","mango"]
# myfruitlist=printfruitnames(fruits)
# print("my firut",myfruitlist)    #or
# print("my fruits",printfruitnames(fruits)) #or
printfruitnames(fruits)
print("fruits", fruits) #or
print()
# the pass statement
def somefunction():
   pass
y=10
if y < 10:
  print("less than 10")
else: 
  print("something")
while y < 1:
  pass
print()
# recursion
# when a function calls itself

def factorial(num):
  if num==0:
    return 1
  else:
    return num * factorial(num -1)
print("factorial",factorial(3))
print()
# 3 * factorial(2)=6
# 2 * factorial(1)=2
# 1 *1=1
# # factorial
# 4!=4*3*2*1
# 4!=4*3!
# fibonacci sequence 1,1,2,3,5,8,13...
def fibonacci(num):
  if num == 1 or num==2:
    return 1
  else:
    return fibonacci( num - 1) + fibonacci(num - 2)
print(fibonacci(4))
print()
def countdown(n):
  if n <=0:
    print("take off!")
  else:
     print(n)
     countdown(n-1)
countdown(5)       
print("hello","ali!")

# number = int(input("Enter a number: "))

# while number != 0:
#     if number % 2 == 0:
#         print("Even!")
#     else:
#         print("Odd!")
#     number = int(input("Enter a number: "))   
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
print()
# nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])
print()
# Create a list called snacks with 3 items

# Print the first and last item

# Add a 4th item using append()

# Remove the second item using pop()

# Print the final list
# snacks=["kolo","chips","qq"]
# print(snacks[0],snacks[2])
# snacks.pop(1)
# print(snacks)

# Create two empty lists:
# cart → to store snack names
# cart_prices → to store prices
# Use a while loop to repeatedly ask the user for an item number.
# If the user types "done", stop the loop.
# Otherwise:
# Convert their input to a number
# Add the snack name to cart
# Add the price to cart_prices
# Print a confirmation message, e.g., "Chips added to cart!"
