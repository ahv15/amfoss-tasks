t=int(input())
sum=0
for i in range (0,t):
   n=int(input())
   for k in range(0,n):
          if k%3==0 or k%5==0:
            sum=sum+k
   print (sum)
   sum=0
