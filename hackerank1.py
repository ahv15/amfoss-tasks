a0,a1,a2=input(" Give Alice's comparison points seperated by a space").split()
b0,b1,b2=input(" Give Bob's comparison points seperated by a space").split()
alicescore=0
bobscore=0
if int(a0)>100 or int(a1)>100 or int(a2)>100 or int(b0)>100 or int(b1)>100 or int(b2)>100 or int(a0)<1 or int(a1)<1 or int(a2)<1 or int(b0)<1 or int(b1)<1 or int(b2)<1:
       print ("invalid points")
       
else:
        Alice_points=[a0,a1,a2]
        Bob_points=[b0,b1,b2]
        for i in range(0,3):
             if Alice_points[i]>Bob_points[i]:
                    alicescore=int(alicescore) + 1
             elif Bob_points[i]>Alice_points[i]:
                    bobscore=int(bobscore) + 1
Result=[alicescore,bobscore]
print(Result)

