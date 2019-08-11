t=int(input())
for i in range(0,t):
     n=int(input())
     fibseq=1
     fibseq1=0
     fibseq2=0
     s=0
     sum=0
     while s<1:
       if fibseq<n:
           fibseq2=fibseq
           if fibseq2%2==0:
                sum=sum+fibseq2
           fibseq=fibseq+fibseq1
           fibseq1=fibseq2
       if fibseq>=n:
           s=1   
           print(sum)
