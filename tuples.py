#1.Write a Python program to create a tuple.
'''
t = (10,20,30)
print(t,type(t))
'''

#2.Write a Python program to create a tuple with different data types.
'''
t = (10,"Welcome",89.23,True)
print(t)
'''

#3.Write a Python program to create a tuple of numbers and print one item.
'''
t = (10,20,30,50)
print(t[2])
'''

#4.Write a Python program to unpack a tuple into several variables.
'''
t = (10,20,"welcome")
a,b,c = t
print(a)
print(b)
print(c)
'''

#5.Write a Python program to add an item to a tuple.
'''
t = (10,"Welcome",89.23,True)
print(t)
li = list(t)
li.append("Thanos")
t = tuple(li)
print(t)
'''

#6.Write a Python program to convert a tuple to a string.
'''
t = ('w','e','l','c','o','m','e')
print(t)
st = ''.join(t)
print(st)
'''

#7.Write a Python program to get the 4th element from the last element of a tuple.
'''
t = (10, 'Welcome', 89.23, True, 'Keshav')
print(t[3])
print(t[-1])
'''

#8.Write a Python program to create the colon of a tuple.
'''
import copy
t = ("HELLO", 5, [], True)
print("Original :- ",t)
d_p = copy.deepcopy(t)
print("Deep copy :- ",d_p)
d_p[2].append(50)
print("Deep copy after modify : ",d_p)
print("Original copy after modify :",t) 
'''

#9.Write a Python program to find repeated items in a tuple.
'''
t = (10,20,30,40,10,20,50)
d = {}
for i in t:
    if(i not in d):
        d[i] = 1
    else:
        d[i] += 1
for i,j in d.items():
    if(j == 2):
        print("Repeted items are :- ",i)
'''

#10.Write a Python program to check whether an element exists within a tuple.
'''
t = (10, 20, 30, 40, 10, 20, 50)
ele = 100
if(ele in t):
    print("Elements are present in tuple :- ",ele)
else:
    print("Elements are not present in tuple :- ",ele)
'''

#11.Write a Python program to convert a list to a tuple.
'''
li = [10,20,30,40]
print(li,type(li))
t = tuple(li)
print(t,type(t))
'''

#12.Write a Python program to remove an item from a tuple.
'''
t = (10,20,30,40,"welcome")
print(t)
li = list(t)
li.remove(30)
t = tuple(li)
print(t)
'''

#13.Write a Python program to slice a tuple.
'''
t = (10,20,30,40,"welcome",True)
print(t)
print(t[::-1])
'''

#14.Write a Python program to find the index of an item in a tuple.
'''
t = (10,20,30,40,"welcome",True)
print(t.index(30))
'''

#15.Write a Python program to find the length of a tuple.
'''
t = (10,20,30,40,"welcome",True)
print(len(t))
'''

#16.Write a Python program to convert a tuple to a dictionary.
'''
keys = (10,20,30)
values = ("ten","twenty","thirty")
d = dict(zip(keys,values))
print(d,type(d))
'''

#17.Write a Python program to unzip a list of tuples into individual lists.
'''
li = [(10,"ten"),(20,"twenty"),(30,"thirty")]
a,b = zip(*li)
print(list(a))
print(list(b))
'''

#18.Write a Python program to reverse a tuple.
'''
t = ((10,"ten"),(20,"twenty"),(30,"thirty"))
print(t)
print(t[::-1])
'''

#19.Write a Python program to convert a list of tuples into a dictionary.
'''
li = [(10,"ten"),(20,"twenty"),(30,"thirty")]
print(li)
d = {}
for item in li:
    key = item[0]
    value = item[1]
    d.update({key:value})
print(d,type(d))
'''

#20.Write a Python program to print a tuple with string formatting.
'''
t = (100, 200, 300)
print("This is a tuple ",t)
'''

#21.Write a Python program to replace the last value of tuples in a list.
'''
li = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print(li)
new = []
for i in li:
    li = list(i)
    li[-1] = 100
    new.append(tuple(li))
print(new)
'''

#22.Write a Python program to remove an empty tuple(s) from a list of tuples.
'''
li = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print(li)
while () in li:
    li.remove(())
print(li)
'''

#23.Write a Python program to sort a tuple by its float element.
'''
li = [('item1', '12.20'),('item8', '1.10'), ('item2', '15.10'), ('item3', '24.5')]
print(li)
def fun(ele):
    return ele[-1]
new = sorted(li,key=fun,reverse=True)
print(new)
'''

#24.Write a Python program to count the elements in a list until an element is a tuple.
'''
li = [10,20,30,40,50,("welcome",12)]
print(li)
count = 0
for i in li:
    if(type(i) == tuple):
        break
    count += 1
print(count)
'''

#25.Write a Python program to convert a given string list to a tuple.
'''
st = "python 3.0"
print(st)
t = tuple(st)
print(t)
'''

#26.Write a Python program to calculate the product, multiplying all the numbers in a given tuple.
'''
t = (2, 4, 8, 8, 3, 2, 9)
product = 1
for i in t:
    product *= i
print("Product - multiplying all the numbers of the said tuple: ",product)
'''

#27.Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
'''
t = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
print(t)
li = []
zero,first,sec,third = [],[],[],[]
for item in t:
    zero.append(item[0])
    first.append(item[1])
    sec.append(item[2])
    third.append(item[3])

total0 = sum(zero)
count0 = len(zero)
avg0 = total0 / count0

total1 = sum(first)
count1 = len(first)
avg1 = total1 / count1

total2 = sum(sec)
count2 = len(sec)
avg2 = total2 / count2

total3 = sum(third)
count3 = len(third)
avg3 = total3 / count3

li.extend([avg0,avg1,avg2,avg3])
    
print("Final :- ",li)
'''

#28.Write a Python program to convert a tuple of string values to a tuple of integer values.
'''
t = (('333', '33'), ('1416', '55'))
print(t)
new = []
for item in t:
    li = []
    for i in item:
        li.append(int(i))
    new.append(tuple(li))
print(new)
'''

#29.Write a Python program to convert a given tuple of positive integers into an integer.
'''
t = (10, 20, 40, 5, 70)
st = ''
for i in t:
    if(i > 0):
        st += str(i)
print(int(st))
'''

#30.Write a Python program to check if a specified element appears in a tuple of tuples.
'''
t = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
merged = sum(t,())
if 'White' in merged:
    print("True")
elif 'Olive' in merged:
    print("False")
'''

#31.Write a Python program to compute the element-wise sum of given tuples.
'''
li = [
    (1, 2, 3, 4),
    (3, 5, 2, 1),
    (2, 2, 3, 1)
    ]
print(li)
zero,one,two,three = [],[],[],[]
for i in li:
    zero.append(i[0])
    one.append(i[1])
    two.append(i[2])
    three.append(i[3])
res = []
r1 = sum(zero)
r2 = sum(one)
r3 = sum(two)
r4 = sum(three)
res.extend([r1,r2,r3,r4])
print("Final :- ",res)
'''

#32.Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples.
'''
li = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
res = []
for item in li:
    total = 0
    for i in item:
        total += i
    res.append(total)
print(res)
'''

#33.Write a Python program to convert a given list of tuples to a list of lists.
'''
li = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
print(li)
new = []
for i in li:
    new.append(list(i))
print(new)
'''
    























































        
        




















































































    





































































































