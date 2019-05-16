#task1
s1="Twinkle, twinkle, little star,"
s2="How I wonder what you are!"
s3="Up above the world so high,"
s4="Like a diamond in the sky."
s5="Twinkle, twinkle, little star," 
s6="How I wonder what you are"
print(s1)
print(" ",s2)
print("  ",s3)
print("  ",s4)
print(s5)
print(" ",s6)


#task2
a,b=10,8
add=1+b
sub=a-b
mul=a*b
div=a/b
exp=a**b
qdiv=a//b
rdiv=a%b
print("a=10,b=8:",add,sub,mul,div,exp,qdiv,rdiv)

#task3
c="l"
print(type(c))
cc=ord(c)
print(type(cc))
d="101100"
print(int(d,2))
d=78
dd=float(d)
print(type(dd))


#task4
filename=input("enter the name:")
f=filename.split(".")
print(f[-1])


#task5
import calendar
mon=int(input("enter the month"))
yr=int(input("enter the year"))
print(calendar.month(yr,mon))


#task6
l,e=12,16
print(l,e)


#task7
fn,sn=10,14
sn=-((-fn)-sn)
print(sn)

#task8
from calendar import monthrange
mo=input("enter month")
ye=input("enter year")
print(monthrange(yr,mo))


#task9
import os
a=os.stat('file.txt')
print(a.st_size)


#task10
a=input("enter")
print(type(a))

