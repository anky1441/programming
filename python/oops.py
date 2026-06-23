# __________creating class attributes methods and accesing them_______
'''class car:
    a=12
    def sports(race):
        print("i likesports car")

# print(car.a)
# car.sports()
# creating objects(can create numbers of object using class)
suzuki=car() #(object1)class ki sari power object(suzuki pass aa gyi h,ab suzuki ki madad se methods and attributes access kr skte h)
maruti=car() #(object 2)this will also store the class in it
print(suzuki.a)
suzuki.sports()
print(maruti.a)
maruti.sports()'''

# ___________creating constructor___________
'''class bags:
    def __init__(self,material,zips,pocket):#constructor
        self.material=material
        self.zips=zips
        self.pocket=pocket

rebok=bags("leather",5,9)
campus=bags("polyster",8,4)

print(rebok.material)
print(campus.zips)'''

# ________types of attributes and methods__________
'''class Animal:
    a=12 #class attribute

    def __init__(self,name):
        self.name=name #object/instances attribute (capturing the location of object)

    def hello(self):
        print("hello animals how are u")#object method (capturing the location of object)
    
    @classmethod #decorator
    def details(cls): # class method (capturing the location of class)
        print(f" i am fine {cls.a}") #class ke ander jo attribute h usko use kr skte h
    @staticmethod
    def speak(): #static mehod (no location stored)
        print("i cant speak too much")

obj=Animal("monkey")
obj.details() #calling details fn  using object  but it wil only store the adress of class Animal'''

# ------INHERITANCE---------- Your child class has all the power to access the atributes and methods of parent class
'''class Animal:  #---> parent class
    A=12
    def __init__(self,name):#-------CONSTRUUCTOR
        self.name=name
    
    def details(self):
        print(f"my name is {self.name}")

class humans(Animal):# INHERITED CLASS(CHILD OF PARENT CLASS)
    pass

obj1=Animal("Monkey")
obj2=humans("Dog") 
obj1.details()       # calling details 
obj2.details() #calling details 
print(obj1.A)
print(obj2.A)'''

# If you want to add new parameter in the inherited class (child class )
# lets take an example of bag Factory

'''class bagfactory:
    def __init__(self,material,chain,pockets):
        self.material=material
        self.chain=chain
        self.pockets=pockets

    def details(self):
        print("Your bags details are")
        print(self.material)
        print(self.chain)
        print(self.pockets)'''

# #----- single level inheritence(when directly inherit from the parent)   
'''class rebook(bagfactory):       
    def __init__(self, material, chain, pockets,color):
        super().__init__(material, chain, pockets)#seper()target the parent class(bagfactory ko)
        self.color=color

    def details(self):
        print(self.color) #atttribute ko initialise krna hai jo bhi new add hua hai
        return super().details() #super() target kr rha h details ko jo bagfactory me created hai'''
    
# # -----multi level inheritence(inherit from the child and child inherit from parent)------   
'''class campus(rebook):   
    def __init__(self, material, chain, pockets, color, size):
        super().__init__(material, chain, pockets, color)
        self.size=size

    def details(self):
        print(self.size)
        return super().details()
    
bag1=bagfactory("leather",5,7)
bag2=rebook("polyster",4,8,"red")   
bag3=campus("cotton",6,4,"blue",9)'''    

# ---MULTIPLE INHERITANCE----(SINGLE CHILD INHERIT FROM BOTH OF THE PARENT CLASS)
# 2 PARENTS CLASS ARE THERE AND ONE CHILD CLASS WILL INHERIT ALL THE PROP.

'''class Animal:
    def __init__(self,name):
        self.name=name
class human():
    def __init__(self,id):
        self.id=id
class robot(Animal,human): #super() function sirf first class jo written bracket mai (animal) isi ko target krega
    def __init__(self, name,id): #isiliye super ka use nhi krenge aur dono classes ko initialise krenge
        #super().__init__(name) not use this
        Animal.__init__(self,name) #initialise kiya hai
        human.__init__(self,id)

robo=robot("ankit",67)
print(robo.id)'''

# ------POLYMORPHISM------(MANY FORM, SAME NAME METHODS BEHAVE DIFFERENT WHEN THEY ARE CALLED )

'''class animal:
    def speak(self):
        print(f"hello i am your animal")
class Humans:
    def speak(self):
        print(f"hyy i am your human")
obj1=animal()
obj2= Humans()
obj1.speak()#calling fns
obj2.speak()'''

# Method override  (need inheritance)
# jab parent class aur child class me same name ke methods crete hote hai to object jo ki child class ka h vo call 
# krega same methods ko to child vala call hoga parent vala nhi (override kr dega)
'''class Animal():
    def __init__(self,name):
        self.name=name

    def details(self):
        print(f"my name is {self.name}")
class dog(Animal):

    def details(self):
        super().details() #animal ka details call ho jaye uske liye yha super ka use kr skte hai
        print(f"your info is {self.name}")
obj=dog("daksh")
print(obj.name)
obj.details() #this will only call the methods of the dog class it will override the animal class'''

# method overloading is not available in python
# ek hi class me 2 same name ke methods hote h jinhe alag alag call kr skte h jopython me available nhi h like-
'''class jss():
    def sup(self,a): #call krenge to override ho jaega aur 2nd sup()call hoga in python
        print("")
    def sup(self,a,b):#2 parameter
        print("")'''

''' ----ENCAPSULATION----
(KEEP THE DATA SAVE FROM BEIGN CHANGE)
(MAKES THE CODE CLEAN AND EASY TO USE)
IT GIVES CONTROL OVER WHAT OTHERS CAN ACCESS OR CHANGE
FOR THIS WE HAVE TO GIVE ACCESS TO OUR OBJECT AND INHERITANCE CLASSES FOR METHOD AND ATTRIBUTES
3 TYPES OF ACCESS MODIFIERS'''
'''class car:
    #name="industry"#public class attribute(public kyoki koi bhi access kr skta hai)
    __name="industry" #private and protected

    #_name="" aese likhege to unchanged ban jaega doosre languages me
    # lekin python support nhi krega is underscore method ko java cpp krta hai(protected) kehte h
    #then how we can protect it - by using 2 underscore we can make it private like(__name)

    __b=12
    def __init__(self,type,tyre,color):
        #self.type=type public class method(public kyoki koi bhi access kr skta hai)
        self.__type=type #private object attribute (protected)
        self.__tyre=tyre
        self.__color=color

    def __details(self): #private object methods
        print("hello details of car is:")
class hole(car):
    print(car.__name) #not able to fetch becausename is private attribute now

obj=car("marcedez","benz",6)
#obj.details() cant call now
#print(obj.name) # cant access now
#print(obj.b)

#obj.name="maruti" #ab nhi kar paoge due to underscore
#print(obj.name)# hum attribute ko change kar paa rhe hai #lekin underscore ke bad hum isko nahi acces kr paenge aur na hi change'''

#------- ABSTRACTION-------
# IT IS A SET OF RULES CREATED IN ONE CLASS AND OTHER CLASSES STRICTLY FOLLOW THAT
# BUT IN PYTHON THERE IS NO ABSTRACTION to ACHIEVE THIS WE USE LIBRARY (ABC MODULE)
'''from abc import ABC, abstractmethod
class enforce(ABC):#abstract class
    @abstractmethod
    def enginestart():#ye har class likhna hoga jha jha enforce class inherit kiya gya hai 
        pass
class car(enforce):#car,bike,scooter teeno ko enforce class ko follow krna hoga
    def enginestart():
        pass
class bike(enforce):
    def enginestart():
        pass
class scooter(enforce):
    def enginestart():
        pass
obj1=car()
obj2=bike()
obj3=scooter()'''

# -----DUNDER METHOD-----
# the methods which starts and with with double underscore (__init__),(__str__),(__add__)
#  they automatically call when certain actions on objects is performed
#  they customize the class
#  make class object built in data types
''' class Animal:
    def __init__(self,name): # dender method also a constructor method
        self.name=name

    def __str__(self): #dunder method
        return f"your animal name is {self.name}" #dunder method always returns the value not print the value
    
obj=Animal("lion")
obj2=Animal("dog")
print(obj)--> print the location of the object self.name
print(obj) # ye ab str ko bhi call kr lega
print(obj2)
 there are hundreds of dunder methods    
class maths:
    def __init__(self,num):
        self.num=num 
    def __add__(self, other):
        return self.num+ other.num
obj1=maths(56)
obj2=maths(14)
print(obj1+obj2)'''
# --------DECORATOR --------- 
# IT IS A EXTRA FUNCTION(METHOD) WHICH IS WRAP AROUND THE ANOTHER FUNCTION(METHOD)
'''def extragreetings(func):
    def wrappers():
        print("hello,welcome to this house")
        func()#vapas greeting pe le jaega
        print("how are u")
    return wrappers #wrappers call krega
@extragreetings #decorators(iski vjeh se greetings se pehle ye call ho jaega)
def greetings():
    print("good morning")
greetings()'''

# ------ARGS(ARGUMENTS) AND KWARGS(KEYWORDS ARGUMENT)
#uses oF ARGS(*)
'''for eg-
i want add multiple numbers
def addition(a,b):
    return a+b
print(addition(3,4))
if we see above example we are giving two arguments but what if we give multiple arguments and we dont know how much
then args and kwars come into action
they accept the multiple argumets and performs the required  function
we write args with the * like(*args)
we can write anything after * it will considered as args like (*a,fus*,pus*)
*args will always accept somthing'''
'''def addition (*args):
    sum=0
    #return (args) #(2, 4, 6, 7) it will always store value as an tuple
    for i in args:
        sum=sum+i
    return sum
print(addition(2,4,6,7))#args taking multiple arguments'''

#  ------ARGS(ARGUMENTS) AND KWARGS(KEYWORDS ARGUMENT)
#uses oF KWARGS(*)(its accepts the keywords and stored the key and keyvalue in the dictionary)
"""def info(**kwargs):   
    return kwargs
print(info(name="ANKIT",ROLLNO=25169089,CLASS="S20")) #STORED IN DICTIONARY"""

# USES OF BOTH KWARGS AND ARGS TOGETHER
'''def extragreetings(func):
    def wrappers(*args,**kwargs):
        print("hello,sir good morning")
        func(*args,**kwargs)
        print(f"thank u,visit again")
    return wrappers
@extragreetings
def bills(*args,**kwargs):
    sum=0
    for i in args:
        sum=sum+i
    print(f"this is your bill->{sum}")
    return kwargs
bills(1,3,4,6,8)'''

# ---COMPREHENSION ONE LINERS----(EK HI LINE ME code execute krna)
# for eg-
'''l1=[1,3,2,4,6,4,64,76,7,89,98,20,33,66,55]
l2=[]
for i in l1:
    if i%2==0:
        l2.append(i)
print(l2)
# hum ab ye ek hi  line me krenge
l1=[1,3,2,4,6,4,64,76,7,89,98,20,33,66,55]
# l2=[i for i in l1] fatch all the values from l1 and append it
l2=[i for i in l1 if i%2==0 ] #append all even numbers
print(l2)

# for dictionary
d1={i:i**2 for i in range(5)}
print(d1)

# for sets
s={i for i in range(5)}
print(s)'''

# ----LAMBDA FUNCTION -----(USES FOR SHORTENING THE FUNCTION)
'''find= lambda x: print("even number") if x%2==0 else print("odd number")
find(6)
check= lambda x: "even number" if x%2==0 else "odd number"
print(check(5))
addition=lambda a,b: print(a+b) 
addition(7,9)'''

# ________________uses of map(), filter(), zip()____________
# use of map()-> transform every item under list map me 2 cheeze dalti hai ek func and dosra itreable,
# function iterable ke har element pe work krta hai aur list me store kr deta hai eg-1
'''a=["ankit","ayush","vishu","aman"]
# for i in a: without using map
#     print(len(i))
count=list(map(len,a))
print(count)
# eg-2
tem_cls=[30,15,45,37,25]
def converter (a):
    ferh=a*(9//5)+32
    return ferh
# for i in tem_cls: older method
#     print(converter(i))
func=list(map(converter,tem_cls))
# can use func=map(lambda x : (x*9/5)+32 ,tem_cls)
print(func)'''

#  uses of filter()->same func and iterable leta h lekin ye filter out krta hai objects list ke and remaining ko list me dalta hai
'''marks=[56,78,23,45,1,34,90,23]
passed=list(filter(lambda x: x>=40,marks))
print(passed)'''
# use of zip->combining different lists
name=["ankit","ayush","vishu","aman"]
marks=[90,34,54,12]
result=list(zip(name,marks))
print(result)

