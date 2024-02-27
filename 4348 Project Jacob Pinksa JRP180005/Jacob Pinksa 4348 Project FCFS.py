#!/usr/bin/env python
# coding: utf-8

# In[17]:


#Jacob Pinksa JRP180005
def findFinishTime(processes,n, at, bt, ft):
    for i in range(0, n):
        ft[0] = bt[0]
        for i in range(1, n):
            if ft[i-1] > at[i]:
                ft[i] = ft[i-1] + bt[i]
            else :
                ft[i] = at[i] + bt[i]

def findResponseTime(processes, n, ft, at, rt):
    rt[0] = 0

    for i in range(1, n ):
        rt[i] = ft[i - 1] - at[i]


def findTurnAroundTime(processes, n, at, ft, tat):
    for i in range(n):
        tat[i] = ft[i] - at[i]


def findavgTime( processes, n, at, bt, st, dt, da):
    
    ft = [0] * n   
    rt = [0] * n
    tat = [0] * n
    total_bt = 0
    total_tat = 0
    total_total_st = 0
    total_total_tat = 0
    
    findFinishTime(processes, n, at, bt, ft)


    findResponseTime(processes, n, ft, at, rt)


    findTurnAroundTime(processes, n, at, ft, tat)

    minute = 60
    while (minute <= 660):
        total_st = 0
        total_tat = 0
        
        count = 0
        if(minute/60 <= 10):
            print("Minute " + str(minute/60))
        else:
            print("Minute " + str(minute/60) + " and beyond")
        print( "Processes\tArrival time" + "\tService time" + "\tBurst time " + "\tFinish time " 
              + "\tResponse time" + "\tTurn around time ")
        if(minute <= 600):
            for i in range(n):
                if(ft[i] <= minute):
                    if(ft[i] > (minute - 60)):
                        total_st = total_st + st[i]
                        total_tat = total_tat + tat[i]
                        print(" " + str(i + 1) + "\t\t" + str(at[i]) + "\t\t" + str(st[i])  
                              + "\t\t" + str(bt[i]) + "\t\t" + str(ft[i]) + "\t\t" +
                            str(rt[i]) + "\t\t" +str(tat[i]))
                        count += 1
                        #if(ft[i] > maxft):
                            #maxft = ft[i]
        else:
            for i in range(n):
                    if(ft[i] > (minute - 60)):
                        total_st = total_st + st[i]
                        total_tat = total_tat + tat[i]
                        print(" " + str(i + 1) + "\t\t" + str(at[i]) + "\t\t" + str(st[i])  +
                             "\t\t" + str(bt[i]) + "\t\t" + str(ft[i]) + "\t\t" +
                            str(rt[i]) + "\t\t" +str(tat[i]))
                        count += 1
                        #if(ft[i] > maxft):
                           # maxft = ft[i]
        if(total_st > 0 and total_tat > 0):
            if(minute/60 <= 10):
                print("\nMinute " + str(minute/60))
            else:
                print("\nMinute " + str(minute/60) + " and beyond")
            print("Average service time = %.5f "%((total_st) / count) )
            print("Average turn around time = %.5f "% (total_tat / count))
            print("Ratio of Turn around time to Service time = %.5f "%(total_tat/total_st))
            print("Throughput = " + str(count/(180)) + "\n")
        total_total_st = total_total_st + total_st
        total_toal_tat = total_total_tat + total_tat
        minute += 60
        
    

    print("\nTotal\nAverage service time = %.5f "%(total_total_st /n) )
    print("Average turn around time = %.5f "% (total_total_tat / n))
    print("Ratio of Turn around time to Service time = %.5f "%(total_total_tat/total_total_st)) 
    print("Throughput = "+ str(n/ft[n-1]))

if __name__ =="__main__":
    
    processes = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16 ,17, 18, 19, 20, 21, 22, 23 , 24, 25,
            26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
    n = len(processes)


    arrival_time = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44,
                    46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94]

    service_time = [6, 12, 8, 10, 4, 9, 10, 6, 9, 6, 7, 10, 13, 8, 4, 17, 8, 14, 2, 10, 11, 1, 15, 16, 17, 20,
                    25, 16, 13, 17, 13, 19, 5, 7, 18, 10, 15, 16, 15, 17, 12, 5, 3, 8, 10, 15, 17, 13]
    
    disk_time = [1,2,1,0,2,1,3,1,2,0,0,1,3,1,2,2,1,1,4,2,1,0, 1,2,3,6,1,2,1,3,2,1,4,1,3,2,3,3,1,2,2,1,1,0, 1, 2, 3, 4]
    disk_activity = [1,2,1,0,2,3,4,2,1,0,0,3,2,5,2,1,3,4,1,1,2,0, 3,2,3,1,6,2,1,3,1,5,2,1,3,2,3,1,2,5,1,2,3,0, 2, 1, 3, 4]
    burst_time = [0] * n
    
    for i in range(n):
        burst_time[i] = service_time[i] + (disk_time[i]*disk_activity[i])
    

    findavgTime(processes, n, arrival_time, burst_time, service_time, disk_time, disk_activity)



# In[ ]:




