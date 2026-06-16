# open("firsttry.txt",'x')#this will only create file
# file=open("superman.txt","w")
# data=input("enter the data u want to write")
# file.write(data)
# file=open("../c/armstrong.c","r")#../c/ means one folder peeche jana
# print(file.read())
#./ current folder
#dir current folder ki files dekhne ke liye
# ---use of with-- it uses to automatically open and closes the file after work performed
with open("superman.txt","a") as f:
    f.write(" " + "just checking the with function")
print("done")