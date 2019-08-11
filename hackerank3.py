n=int(input())
diff=[]
diag1=0
diag2=0
absdiff=0
for i in range(0,n):
      diff=list(map(int,input().split()))
      diag1=diag1+int(diff[i])
      diag2=diag2 + int(diff[n-i-1])
      absdiff=abs(diag1-diag2)
print (absdiff)

