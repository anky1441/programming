# l=[23,34,78,1,34,90,56,34,2,78]
# l[1]=7
# print(l[5:])
# for i in l:
#     print(i)
# for i in range(len(l)):
#     print(l[i])
# l.append(30)
# l.insert(3,30)
# print(l)
# b=l.pop()
# print(l)
# print(b)
# l.remove(4)
# print(l)
# l.pop(3)
# l.sort()
# l.sort(reverse=True)
# l.reverse()
# b=len(l)
# print(b)
# positive and negative number in list
# pos=[]
# neg=[]
# # print("enter the numbers in list")
# given=[3,-1,4,-5,9]
# for i in given:
#     if i>=0:
#         pos.append(i)
#     else:
#         neg.append(i)
# print(pos,neg)
# list=[10,20,30,40]
# sum=0
# for i in list:
#     sum=sum+i
# print("the average of the list of the elements are->>>",sum/len(list))
# l=[4,8,2,9,1,10]
# largest=l[0]
# for i in range(len(l)):
#     if l[i]>largest:
#         largest=l[i]
#         index=i
# print("greatest element is",largest,"at index",index)
# first_Largest=l[0]
# second_Largest=l[0]
# for i in range(len(l)):
#     if l[i]>first_Largest:
#         second_Largest=first_Largest
#         first_Largest=l[i]
#     elif i>second_Largest:
#         second_Largest=i
# print("second greatest element is",second_Largest)
# l=[10,1,3,8,5,7]
# for i in range(len(l)-1):
#     if l[i]>l[i+1]:
#         print("list is not sorted")
#         break;
# else:
#     print("list is sorted")
# ####### T U P L E
# tuple=(1,2,3,4,5,6,7,7,7,7,7)
# print(type(tuple))
# print(tuple)
# for i in tuple:
#     print (i)
#     print(tuple.index(7))
#     print(tuple.count(7))
# ----- S E T S ----------
# s1={1,2,3,"hello",(1,2,3)}
# print(type(s1))
# a="ankit"
# print(hash(a))
# print(s1)
# print(s1)
# # a=(s2-s1)
# # print(type(a))
# s1-=s2
# print(s1)
# s1.add(67)
# for i in s1:
#     print(i)
# s2.discard(9)
# a=s2.pop()
# s2.remove(90)
# print(s2)
# print(a)
# s1={12,23,34,45,56}
# s2={12,23,34,90,7,8,87}
# s3={12,23,34}
# print(s3.issubset(s1))
# print(s3<=s1)
# print(s2.issuperset(s3))
# print(s2>=s3)
# print(s1.symmetric_difference(s2))
# print(s1^s2)
# s1^=s2
# print(s1)
# print(s1.union(s2))
# print(s1|s2)
# -------->D I C T I O N A R Y>------------
#d={1:"ankit",2:"srivastva"}
# print(type(d))
# print(d[1])
# d[3]=25169089
# d[2]="SRIVASTVA"
# print(d)
# print(d.get(1))
# print(d.items())
# print(d.keys())
# print(d.values())
# d[3]=6
# print(d)
# b=d.pop(1)
# print(b)
# print(d)
d2={1:10,2:20,3:30,4:40,5:50}
# print(d2.popitem())
#print(d2.setdefault(6,60))
# d2.update({6:60})
# print(d2)
# for i in d2:
#     print(d2[i])
# -------->>>>>E X C E P T I O N A L   H A N D L I N G---------->>>>>>>
#   exception(errors) can be handle through----try, except , else, finally , raise 
# a=int(input("enter the number a-->> "))
# b=int(input("enter the number b-->> "))
# try:
#     print(a/b)
# except Exception as arr:
#     print(f"it is showing error as {arr}")
# # ----->>except chalega to else nhi chalega
# else:
#     print("no error occured ")
# #-------FINALLY hmesha chlta h block-----
# finally:
#     print(f"code will run ") 
# c= input("what is your name----->>> ")
# print(f"your name is {c}")

# -------->>>>> R A I S E (used to crete error)>>>>>----------

age=int(input("entery yoour age"))
if age<18:
    raise ValueError("you are not eligible")
print("you are eligible")
