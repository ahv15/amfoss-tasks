n=int(input())
X=0
for i in range(0,n):
      x=input()
      if x[-1]=="+" or x[0]=="+" :
            X=X+1
      elif x[-1]=="-" or x[0]=="-" :
            X=X-1
print (X)
      
