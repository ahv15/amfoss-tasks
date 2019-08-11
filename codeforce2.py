n=int(input())
wordarray=[]
for i in range(0,n):
   word=str(input())
   if len(word)<11 :
     wordarray.append(word)
   else:
     word=word[0]+str(len(word)-2)+word[-1]
     wordarray.append(word)
print (wordarray) 
