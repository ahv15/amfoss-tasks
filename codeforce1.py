import math
n,m,a= map(int,input().split())
x=0
y=0
numberofflagstones=0
x=math.ceil(n/a)
y=math.ceil(m/a)
numberofflagstones=x*y
print(numberofflagstones)
