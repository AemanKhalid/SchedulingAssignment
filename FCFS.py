import time
def FCFS():
    print "Enter number of process:"
    n=input()
    bursttime =[0]*n
    arrivaltime=[0]*n
    process=[0]*n
    order=[0]*n
    finishtime=[0]*n
    starttime=[0]*n
    waittime=[0]*n
    j=0
    while j<n:
        order[j]=j+1
        j+=1
    i=0
    while i<n:
        print "Enter burst time and arrival time of process P" + str(i+1)
        process[i]=i+1
        bursttime[i]=input("Enter burst time")
        arrivaltime[i]=input("Enter arrival time")
        i+=1
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

    print "Average waiting time o all processes is :" +str(sum)

    print "=================================================="
    g=0
    while g<n:
        print "Process " + str(g+1) + " turn around time " +str(finishtime[g]-arrivaltime[g])
        g+=1
    return;

FCFS()
time.sleep(5)