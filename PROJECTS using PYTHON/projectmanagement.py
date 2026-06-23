# ----____-----PROJECT ON STUDENT MANAGEMENT SYSTEM-----____------(USING OOPs)
import json
from pathlib import Path
from abc import ABC, abstractmethod

database="school_data.json" #database stored the info in the form of dictionary
data={"students":[],"teachers":[]} # creating a copy so that we can change teh data multiple times 

if Path(database).exists():
    with open (database,'r') as f:
        content=f.read()
        if content:
            data=json.loads(content) #copying content into the data file

def save():
    with open(database,'w') as f:
        json.dump(data,f,indent=4)

class personal(ABC):

    @abstractmethod
    def get_roles(self):
        pass

    @abstractmethod
    def register(self):
        pass

    @staticmethod
    def email_verification(email):# sirf email ke liye use kr rhe h isliye staic h iska role nahi object e h na hi class me
        if "@" in email and "." in email:
            return True
        else:
            return False

class Student(personal):

    def get_roles(self):
        return "student"

    def register(self):
        name=input("enter your name-:")
        roll_no=int(input("enter your roll number-->"))
        age=int (input("enter your age-->"))
        email=input("enter your email-->")

        if not personal.email_verification(email):
            print("invalid email")
            return 
        for i in data['students']:
            if i['roll_no']==roll_no:
                print("student already exist")
                return
        data['students'].append({
            "name":name,
            "roll_no" : roll_no,
            "age" : age,
            "email" :email,
            "grades" :{}
        })
        save()
        print(f"student{name} registered")
    
    def grade_add(self):

        roll_no=int(input("enter your roll number-->"))
        subject=input("enter your subject name-->")
        marks=int(input("enter your marks-->"))

        for i in data['students']:
            if i['roll_no']==roll_no:
                i['grades'][subject]=marks
                save()
                print("grade added successfully")
                return
        print("student not found")
    
    def show_details(self):

        roll_no=int(input("enter your roll number-->"))

        for i in data['students']:
            if i['roll_no']==roll_no:
                grades=i['grades']
                avg=sum(grades.values()) / len(grades) if grades else 0

                print(f"name : {i['name']}") 
                print(f"roll number is : {i['roll_no']}") 
                print(f"email id is : {i['email']}") 
                print(f" age is : {i['age']}")
                print(f"grades are: {i['grades']}") 
                print(f"average marks are : {avg:.1f}")
                return 

stud = Student()

class Teachers(personal):

    def get_roles(self):
        return "Teacher"
    
    def register(self):

        name=input("enter your name-->")
        email=input("enter your email id-->")
        emp_id=int(input("enter your emp id number-->"))
        age=int(input("enter your age-->"))
        subject=input("ennter the subject you are specialized in-->")

        if not personal.email_verification(email):
            print("Invalid Email-ID")
            return
        
        for i in data['teachers']:
            if i['emp_id']==emp_id:
                print("teacher already exists")
                return
            
        data['teachers'].append({
            "name": name,
            "email":email,
            "emp_id":emp_id,
            "age":age,
            "subject":subject
        })
        save()
        print(f"regisered {name} sussesfully")

    def show_details(self):    

        emp_id=int(input("enter the employee id number-->"))

        for i in data['teachers']:
            if i['emp_id']==emp_id:
                print(f" name is : {i['name']}")
                print(f"emp id number is: {i['emp_id']}")
                print(f"email is: {i['email']}")
                print(f"age is : {i['age']}")
                print(f"subject is : {i['subject']}")
                return
        print("teacher not found")

employee=Teachers()

print("press 1 to registered as Student")
print("press 2 to registered as teacher")
print("press 3 to add grades of students")
print("press 4 to show the details of Student")
print("press 5 to show the details of teacher")

choice=int (input("enter your choice-->"))

if choice==1:
    stud.register()

elif choice==2:
    employee.register()

elif choice==3:
    stud.grade_add()

elif choice==4:
    stud.show_details()

elif choice==5:
    employee.show_details()