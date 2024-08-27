a=int(input())
b=int(input())
c=str(a+b)
print(c)
d=str(input())
e=str(input())
f=d+ " " +e
print(f)
print(f+" is  "+c)
a=[1,2,3,4,{1,2,3},[1,2,3],(1,2,3),0.5]
print(len(a))
print(type(a))
a.append(5)
print(a)
a.append([2,3,4])
print(a)
a.extend([2,3,4,5])
print(a)
print(a[2])
a.append("subathira")
print(a)
a[-5]="shri devi"
print(a)
del a[7]
print(a)

