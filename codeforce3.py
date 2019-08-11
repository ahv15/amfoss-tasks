values=list(map(int,input().split()))
n=values[0]
k=values[1]
count=0
benchmark=0
participants=list(map(int,input().split()))
benchmark=int(participants[k-1])
for i in range(0,n):
 if int(participants[i])>benchmark or int(participants[i])=benchmark and int(participants[i])>0 :
                count=count+1
print (count)
