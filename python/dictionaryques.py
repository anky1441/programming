# -------------merging two dictionary---------------

'''d1={1:10,2:20,3:30}
d2={4:40,5:50,6:60}
# d1.update(d2) //by using methods 
# print(d1)
# by using vanilla python
for i in d2:
    d1[i]=d2[i]
print(d1)'''

# -------------------sum of keyvalues of dictioary-----------------

'''d3={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
sum=0
for i in d3:
    sum=d3[i]+ sum
print("sum of the value in d3 is",sum)'''

# ----------counting the values of the list using dictionary------------

'''l=["a","b","c","d","a","b","a","b","c","a","c","b","b","c","c","a","a"]
d={}
for i in l:
    if i in d.keys():
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)'''

# ----------adding common key value in dict----------

d1={"a":2,"b":4,"c":6,"d":3}
d2={"c":7,"d":5,"e":4,"f":8}
for i in d2:
    if i in d1.keys():
        d1[i]=d1[i]+d2[i]
    else:
        d1[i]=d2[i]
print(d1)