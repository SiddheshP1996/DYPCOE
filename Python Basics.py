#variables and strings
name = "Siddhesh" #string
age = 21  #integer

#arithmetic operators and strings
age1 = 20
age2 = 18

#for integers

#addition operator
age1 + age2

#subtraction operator
age1 - age2

#multiplication operator
age1 * age2

#division operator
age1 / age2

#for strings
sent1 = "My name is Siddhesh"
sent2 = "I'm 20 years old"

#adding strings
sent1 + sent2
sent = "%s is the Prime Minister of India."   # %s for strings
sent%("Narenra Modi")
sentence = "He is the %d number of Prime Minister."     # %d for integers
sentence%(18)
codingList = ["C++","Java","HTML5"]   #list

#adding an array of string in the string
codingList.append("Javascript")
codingList.append("MySQL")

#replacing an array of string in the string
codingList[0] = "C & C++"

#deleting an array of string in the string
del codingList[4]

#another list
platformList = ["Visual Studio Code","Atom","Anaconda"]

#adding two lists
codingList + platformList

#list og numbers
listNum = [2,34,65,78,123]

# max() function
max(listNum)

# min() function
min(listNum)

#use of Dictionary
student = {"Darshan":20, "Siddharth":20, "Abhishek":21}

#change the number
student["Darshan"] = 21

#deleting the dictionary
del student["Siddharth"]

# find length of the dictionary
len(student)

# NOT TO DO
dict = {"Sid":21, "Sid":24, "Sid":34}

#tuples cannot be modified individually neither can be deleted
tup1 = ("oranges","apples","bananas")
tup2 = (12,14)

#addition of tuples
tup1 + tup2
tup3 = tup1 + tup2

#deletion of tuples
del tup3

#length of tuples
len(tup1)

#multiplication of tuples same as of list
tup2 * 3

#conditional statements

# if condition
if(5 > 3):
    print("Hello")

#if-else condition
if(3 < 2):
    print("Hello")
else:
    print("The condition was not true")

3>=2   #greater than equal to
3<=2   #less than equal to
3==3   #equal to
3!=2   #not equal to
3==2   

# (<, >, <=, >=, ==, !=)  Relational Operators
#elif condition
age = 21
if(age < 15):
    print("Ypu are young")
elif(age >= 15 and age < 18):
    print("You are a teenager")
else:
    print("You are an adult")


#For Loops
list = ["Apples","Bananas","Oranges"]
tup = (12,15,14)

for fruits in list:
    print(fruits)


for numbers in tup:
    print(numbers)

for i in range(0,11):
    print(i)

for i in range(1,11):
    print(i)

#calling even numbers
for i in range(0,11,2):
     print(i)


#first 10 multiples of 5
for i in range(0,51,5):
    print(i)


#Nested For Loop
for i in range(0,5):
    for j in range(0,3):
        print(i*j)



#While Loops
c = 0
while c < 5:
    print(c)
    c = c + 1


#break statement
c = 0
while c < 5:
    print(c)
    if c ==3:
        break
    c = c + 1


#continue statement
c = 0
while c < 5:
    c = c + 1
    if c == 3:
        continue
    print(c)


#pass statement
c = 0
while c < 5:
    c = c + 1
    if c == 3:
        pass
    print(c)

# try and except case
try:
    if name > 3:
        print("Hello")
except:
    print("There's someting wrong with your code - please check again")


#Functions 
def HelloWorld():    #defining a function
    print("Hello World")
HelloWorld()     #calling of function


def returnAdd(num1, num2):
    return(num1 + num2)
sum = returnAdd(23,32)
print(sum)


#In-Built Functions
abs(23)   #absolute value function
abs(-32)


bool(0) #always Fales  #booliean function
bool(1)   #always True
bool(None)  #always False
bool(100) # Always True
# In general except for the valus ) and None the Bool() return True always


dir()    #directory of string to know its availabilities

#help()   # to get help for about the method


#eval()    #evaluate function used for mostly single line of code
sent = 'print("Hi")'
eval(sent)

#exec()    #execution function used for mostly complicated and more lines of code
exec(sent)

a=1
str(a)     # making to look like a string
float(a)   # making to look like a float
int(a)    # making to look like a integer


#Object Oriented OPrograming

class Person:
    pass

p = Person()
p


class Person:
    def getName(self):
        print("Sid")
    def getAge(self):
        print(20)

p = Person()
p.getName()
p.getAge()


#Initialization function [__init__()]

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        print("Your name is " + self.name)
    def getAge(self):
        print("Your Age is " + self.age)

p1 = Person("Siddhesh","20")
p1.getName()
p1.getAge()

#Inheritance concept with Initialization function

class Parent:
    def __init__(self):
        print("This is a Parent class")
    def ParenrFunc(self):
        print("This is a Parent Func")
p = Parent()
p.ParenrFunc()


class child(Parent):
    def __init__(self):
        print("This is a Child class")
    def ChildFunc(self):
        print("This is a Child Func")
c = child()
c.ChildFunc()
c.ParenrFunc()

#@Overwriting method


class Parent:
    def __init__(self):
        pass
    def test(self):
        print("Parent")
p = Parent()
p.test()


class child(Parent):
    def __init__(self):
        pass
    def test(self):
        print("child")
c = child()
c.test()


# feasable solution : no of approaches to solve the question

# optimal solution : the best one to solve the question 