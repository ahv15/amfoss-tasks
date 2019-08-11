n=int(input())
candles=0
m=0
candleheight=list(map(int,input().split()))
candleheight.sort()
candles=candleheight[n-1]
for i in range(0,n):
      if candleheight[i]==candles:
           m=m+1
print (m)
      





