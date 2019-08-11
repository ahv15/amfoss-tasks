t=int(input())
for i in range(0,t):
     factorial=1
     j=1
     n=int(input())
     for i in range(0,n+1):
          factorial=i*factorial
     while j<factorial:
       j=j+1   
       for k in range (0,n):
             smallest=0
             if j%k==0:
               smallest=smallest+1
               if smallest==n-1:
                     print (j) 
                     break  
