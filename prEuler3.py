t=int(input())
for i in range(0,t):
      length=0
      prifactor=[]
      n=int(input())
      for k in range(2,n+1):
         if n%k==0:
               factor=k
               for j in range(2,factor):
                       if factor%j==0:
                           break
                       else:
                           prifactor.append(factor)
      prifactor.sort
      greatest=prifactor[-1]
      print (greatest)
