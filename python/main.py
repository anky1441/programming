# amount=int(input("enter the amount"))
# if amount==10:
#     print("manchurian")
# elif(amount==20):
#     print("chaumein")
# elif(amount==30):
#     print("momos")
# elif(amount==40):
#     print("burger")
# else:
#     print("pizza")
# num1=int (input("enter the number"))
# num2=int (input("enter the number"))
# if(num1>num2):
#     print(num1, "is greater ")
# elif(num1==num2):
#     print(num2, "is equal to", num1)
# else:
#     print(num2, "is greater")
# num3=int(input("enter the number"))
# if num3%2==0:
#     print(num3," is even")
# else:
#     print(num3 ," is odd")
# name=input("enter your name->")
# age=int (input("enter your age->"))
# if age>=18:
#     print("WOW! ",name, ", you are eligible for voting")
# else:
#     print("OH! ",name,", you are not eligible for voting")
# year=int(input("enter the year"))
# if (year%100==0 and year%400==0):
#     print(year,"is a leap year")
# elif (year%100!=0 and year%4==0):
#      print(year,"is a leap year")
# else:
#      print(year,"is not a leap year")
# temp=int(input("enter the temperature celcius"))
# if temp<=0:
#     print("its freezing cold")
# elif temp>0 and  temp<25:
#     print("its cold")

# elif temp>=25 and temp<=35:
#     print("its plesant")
# else:
#     print("its too hot")
# n=int(input("enter the number"))
# for i in range(11):
#     print(n*i)
# a="ankit"
# for i in range(len(a)):
#     if i==9:
#         break
#     print(i,":",a[i])
# else:
#     print("no break introduced") 
# for i in range(1,n+1):
#     print(i)
# for i in range(n,0,-1):
#     print(i)
# for i in range(1,11):
#     print(n,"x",i,"=",i*n)
# sum=0
# for i in range (1,n+1):
#     sum=sum+i
# print(sum)
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)
# sumEVEN=0
# sumODD=0
# for i in range(1,n+1):
#     if i%2==0:
#         sumEVEN=sumEVEN+i
#     else:
#         sumODD=sumODD+i
# print("sum of even numbers",sumEVEN)
# print("sum of odd numbers",sumODD)

# for i in range (1,n+1):
#     if n%i==0:
#         print("factors of ",n,"is",i)
# sum=0
# for i in range (1,n):
#     if n%i==0:
#         sum=sum+i
# if sum==n:
#     print("given number",n,"is","composite")
# else:
#     print("not a composite number")
# c=n//2
# count=0
# for i in range (2,c):
#     if n%i==0:
#         count=1
#         break
# if n==1 or count==1:
#     print(n,"is not a prime number")
# else:
#     print(n,"is a prime number")
# n=input("enter the string->")
# reverse=""
# for i in range(len(n)-1,-1,-1):
#     reverse=reverse+n[i]
# print("reverse of the string",n, "is", reverse)
# if reverse==n:
#     print("given string",n,"is pallindrome")
# else:
#     print("given string",n,"is not a pallindrome")
# n=input("enter the string->>>")
# digit=0
# alpha=0
# symbol=0
# for i in n:
#     if i.isdigit():
#         digit=digit+1
#     elif i.isalpha():
#         alpha=alpha+1
#     else:
#         symbol=symbol+1
# print("digits are-",digit,"<>alphabets are-",alpha,"<>symbols are-",symbol)
# n=input("enter the string->>>")
# for i in n:
#     if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90):
#         alpha+=1
#     elif (ord(i)>=48 and ord(i)<=57):
#         digit+=1
#     else:
#         symbol+=1
# print("digits are-",digit,"<>alphabets are-",alpha,"<>symbols are-",symbol)
# n=int(input("enter the number"))
# while n>0:
#     c=n%10
#     print(c)
#     n=n//10
# n=int(input("enter the number"))
# c=n
# rev=0
# while c!=0:
#     rev=rev*10+c%10
#     c=c//10
# print(rev)
# n=int(input("enter the number"))
# c=n
# rev=0
# while c>0:
#     rev=rev*10+c%10
#     c=c//10
# if rev==n:
#     print("it is pllindrome")
# else:
#     print("not a pallindrome")