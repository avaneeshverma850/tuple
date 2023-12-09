#Tuple
#tuple is a class
#tuple is immutable
#tuple is a sequance
#tuple is hashable
#tupel is a sequance
#create tuple object
t1=(1,2,3,4)
print(type(t1))
t2=()
print(type(t2))
t=(2)
print(type(t))#int type
t3=(10,)
print(type(t3)) #tuple type
t4=2,3,4,5
print(type(t4))
#indexing
a=(1,2,3)
print(a[0])
print(a[1])
print(a[2])
print(a[-3])
print(a[-2])
print(a[-1])
#slicing operator
b=(1,2,3,4,5,6,7,8,9,10)
print(b[::1])
print(b[:4:2])
#accessing the elements
c=(1,2,3,4,5,6,7,8,9)
i=0
while(i<len(c)):
    print(c[i],end=' ')
    i=i+1
print()
#using for loop
for x in c:
    print(x,end=" ")
print()
#built in method are :1-len(),2-min(),3-max(),4-sum(),5-sorted()
print(sum(c))
print(sorted(c))#return in list all the value
print(min(c))
print(max(c))
#concatenation and repetion
t1=(10,20)
t2=(11,22,33)
print(t1+t2)
print(t1*3)
#comaprision operator
print(t1>t2)
print(t1==t2)
#tuple object methods
print(t1.index(10))
print(t1.index(20))
print(t1.count(20))
#Slicing operator
t1=(1,2,3,4,5,6)
print(t1[::-1]) #reverse a operator
t1=()
print(type(t1))
t2=tuple([1,2,3])
print(t2)
t3=tuple(range(5))
print(t3)
#heterogeneous element
t2=(34,True,5,6,4-5j,[4,5])
print(t2[-1])
print(t2[-2])
print(t2[-3])
print(t2[-4])
print(t2[-1][1])