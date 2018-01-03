import time
arrivaltime=[0,1,2,3]
order=[1,2,3,4]
bursttime=[8,4,9,5]
arrivaltime1=[0,1,2,3]
process=[1,2,3,4]
nprocess=[1,2,3,4]
rtime=[0]*4
finishtime=[0]*4
waittime=[0]*4
n=process.__len__()
i = 0
while i < n:
    j = 1 + i
    while j < n:
        if bursttime[j] < bursttime[i]:
            temp = bursttime[j]
            bursttime[j] = bursttime[i]
            bursttime[i] = temp
            temp1 = process[j]
            process[j] = process[i]
            process[i] = temp1
            temp1 = arrivaltime[j]
            arrivaltime[j] = arrivaltime[i]
            arrivaltime[i] = temp1
        j = j + 1
    i += 1
i=0
j=1
small=bursttime[0]
while i< n:
    if arrivaltime[i] > arrivaltime1[i] and i==0:
        finishtime[i]+=arrivaltime[i]+bursttime[i]
    else:
        if arrivaltime[i] ==0:
            finishtime[i]=finishtime[i-1]+bursttime[i]-1
        else:
            finishtime[i] = finishtime[i - 1] + bursttime[i]
    i+=1

i=0
while i<n:
    waittime[i]=finishtime[i]-arrivaltime[i]-bursttime[i]
    i+=1

print "Processes according to their finishing arrangement:"+str(process)
print "Bursttime according to their finishing arrangement:"+str(bursttime)
i=0
sum=0.0
while i<n:
    sum+=waittime[i]
    i+=1
print "Average waiting time:" + str(sum/n)
i=0
sum=0.0
while i<n:
    sum+=finishtime[i]-arrivaltime[i]
    i+=1
print "Average turn around time:" + str(sum/n)

time.sleep(5)
