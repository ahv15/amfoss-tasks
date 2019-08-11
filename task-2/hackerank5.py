time=input()
newtime=0
if time[-2:]=="AM":
       time=time[:-2]
       print (time)
elif time[:2]=="12" and time[-2:]=="AM":
       newtime=00
       time=time[:-2]
       time=time[2:]
       newtime=str(newtime)
       time=newtime+time
       print (time)
elif time[-2:]=="PM":
       newtime=int(time[:2])
       newtime=newtime + 12
       time=time[:-2]
       time=time[2:]
       newtime=str(newtime)
       time=newtime+time
       print(time)
       
