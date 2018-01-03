import time
print "Enter number of process:"
n=input()
bursttime =[0]*n
arrivaltime=[0]*n
process=[0]*n
priority=[0]*n
finishtime=[0]*n
starttime=[0]*n
waittime=[0]*n

i=0
while i<n:
    print "Enter burst time and priority number of process P" + str(i+1)
    process[i]=i+1
    bursttime[i]=input("Enter bursttime:")
    priority[i]=input("enter priority number:")
    i+=1
i=0
while i<n:
    j=1+i
    while j<n:
        if priority[j] < priority[i]:
            temp = bursttime[j]
            bursttime[j] = bursttime[i]
            bursttime[i] = temp
            temp=process[j]
            process[j]=process[i]
            process[i]=temp
            temp= priority[j]
            priority[j] = priority[i]
            priority[i] = temp

        j=j+1
    i+=1
print bursttime
print priority
print process
k=1
finishtime[0]= finishtime[0]+bursttime[0]+arrivaltime[0]
starttime[0]=arrivaltime[0]
while k<n:
    finishtime[k]=finishtime[k-1]+bursttime[k]
    starttime[k]=finishtime[k-1]
    k+=1
g=0
while g<n:
    waittime[g]=starttime[g]-arrivaltime[g]
    print "waiting time of process " +str(g+1) + " is " + str(waittime[g])
    g+=1
sum=0.0
d=0
while d<n:
    sum=sum+waittime[d]
    d+=1
sum=float(sum/n)
print "Average waiting time of all processes is :" +str(sum)

print "=================================================="
g=0
while g<n:
    print "Process " + str(g+1) + " turn around time " +str(finishtime[g]-arrivaltime[g])
    g+=1

time.sleep(5)