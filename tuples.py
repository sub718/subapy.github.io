a=("samsung","apple")
b=("vivo","oppo")
c=a+b
print(c)
e=(a,b)
print(e)
f=str(input())
g=str(input())
print(f+" "+g)
#h=str(input())
#i=int(input())
#d=h,i
#print(d)
x=[1,2,3]
z=['rose','lotus','jasmine']
print(list(zip(x,z)))
x=(1,2,3)
z=('rose','lotus','jasmine')
print(zip((x,z)))
x=[1,2,3]
z=['rose','lotus','jasmine']
print((x,z))
x=[1,2,3]
z=['rose','lotus','jasmine']
print(x,z)
l=[('suba',1),('shri',2),('devi',3)]
letters,numbers=zip(*l)
print(letters)
print(numbers)
l=[('suba',1),('shri',2),('devi',3)]
n,m=zip(*l)
print(n)
print(m)
matrix=[[1,2,3],[2,3,4],[5,6,7]]
transposed=list(*matrix)
print(transposed)
a=(1,2,3,4)
b=(6,7,8,9)
c=a+b
print(c)
print(c.count(7))



