football=input()
length=0
c=0
check=0
length=len(football)
for i in range (0,length-1):
        if football[i]==football[i+1]:
              c=c+1
              
        elif c>6:
              check=1
              print ("YES")
              break
        else:
             c=0
if check!=1 :
     print ("NO")
             
             
         
