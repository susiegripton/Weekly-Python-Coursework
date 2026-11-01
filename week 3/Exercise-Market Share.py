import matplotlib.pyplot as plt
from random import random
counter=0
for j in range(100):
    Volture=0
    NeonDrive=0
#times=[]
#Volture_owners=[]
#NeonDrive_owners=[]
    for i  in range(10):
        if random()<0.5:
            Volture+=1
        else:
            NeonDrive+=1
# FOR NUMBERS OUTPUT
#print(Volture,NeonDrive)
    for i  in range(1000):
        if random()<Volture/(Volture+NeonDrive):
            Volture+=1
        else:
            NeonDrive+=1
    #times.append(i)
    #Volture_owners.append(Volture)
    #NeonDrive_owners.append(NeonDrive)
# FOR NUMBERS OUTPUT
#print(Volture,NeonDrive)
# FOR PLOT
#plt.plot(times,Volture_owners)
#plt.plot(times,NeonDrive_owners)
#plt.xlabel('Time')
#plt.ylabel('No. owners')
#plt.legend(['Volture', 'NeonDrive'])
#plt.show()
    if Volture>NeonDrive:
            counter+=1
print("Volture Wins:",counter)
print("NeonDrive Wins:",100-counter)
print("Volture Win Percentage:",counter/100*100)
if counter>50:
    print("Volture wins overall!")
elif counter<50:
    print("NeonDrive wins overall!")
else:
    print("They tied!")
    




