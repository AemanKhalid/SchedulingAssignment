import time
n=3
timeslice=4
bursttime =[16,3,3]
arrivaltime=[0,1,2]
process=[1,2,3]
waittime=[0]*n
remain=[0]*50
finishtime=[0]*n

print "Process are:"+str(process)
print "Arrival time of process:"+str(arrivaltime)
print "Burst time of process:"+str(bursttime)
print "Time slice is:"+str(timeslice)

i=0
t=0
count=0
while i<n:
    j = 1 + i
    if bursttime[i] >=timeslice:
        remain1 = bursttime[i] - timeslice
        count+=1
        t += timeslice
        while j<n:
            if arrivaltime[j] <=remain1 and count <n:
                remain[j]=bursttime[j]
            j+=1
        remain[j]=remain1
    else:
        finishtime[i] += bursttime[i]+t
        t += bursttime[i]
    k=0
    while k<n:
        bursttime[k]=remain[k]
        k+=1
    i+=1
if finishtime[0] ==0 and arrivaltime[0]==0:
    finishtime[0]=finishtime[n-1]+remain1

i=0
while i<n:
    waittime[i]=finishtime[i]-arrivaltime[i]-bursttime[i]
    i+=1
i=0
sum=0.0
while i<n:
    sum+=waittime[i]
    i+=1
print "Average waiting time:"+str(sum/n)

turntime=[0]*n
i=0
while i<n:
    turntime[i]=finishtime[i]-arrivaltime[i]
    i+=1
i=0
sum=0.0
while i<n:
    sum+=turntime[i]
    i+=1
print "Average turn around time:"+str(sum/n)
time.sleep(10)