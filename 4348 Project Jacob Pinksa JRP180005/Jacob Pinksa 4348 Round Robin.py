#!/usr/bin/env python
# coding: utf-8

# In[47]:


#Jacob Pinksa JRP180005
def findWaitingTime(processes, n, at, bt, rt, ft,
                        wt, quantum):
    rem_bt = [0] * n


    for i in range(n):
        rem_bt[i] = bt[i]
    t = 0 

    while(1):
        done = True
        
        for i in range(n):
            if (at[i] <= t):
                if(rt[i] == -1):
                    rt[i] = t - at[i]

                if (rem_bt[i] > 0) :
                    done = False 
                
                    if (rem_bt[i] > quantum) :
                        t += quantum

                        rem_bt[i] -= quantum
                
                    else:
                
                        t = t + rem_bt[i]

                        wt[i] = t - bt[i] - at[i]
                        ft[i] = at[i] + bt[i] + wt[i]

                        rem_bt[i] = 0
                

        if (done == True):
             break
            
def findTurnAroundTime(processes, n, bt, wt, tat):
    
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def findavgTime(processes, n, at, bt, quantum, st):
    wt = [0] * n
    tat = [0] * n
    rt = [-1] * n
    ft = [0] * n
    total_total_st = 0
    total_total_tat = 0
   
    findWaitingTime(processes, n, at, bt, rt, ft, wt, quantum)

    findTurnAroundTime(processes, n, bt, wt, tat)
    
    minute = 60
    while (minute <= 660):
        total_st = 0
        total_tat = 0
        
        count = 0
        maxft = 0
        if(minute/60 <= 10):
            print("Minute " + str(minute/60))
        else:
            print("Minute " + str(minute/60) + " and beyond")
        print("Processes\tArrival Time\tBurst Time\tResponse Time\tWaiting",
                    "Time\tFinish Time\tTurn-Around Time")
        if(minute <= 600):
            for i in range(n):
                if(ft[i] <= minute):
                    if(ft[i] > (minute - 60)):
                        total_st = total_st + st[i]
                        total_tat = total_tat + tat[i]
                        print(" ", i + 1,"\t\t", at[i],"\t\t", bt[i],
                            "\t\t", rt[i],"\t\t", wt[i], "\t\t", ft[i],"\t\t", tat[i])
                        count += 1
                        #if(ft[i] > maxft):
                            #maxft = ft[i]
        else:
            for i in range(n):
                    if(ft[i] > (minute - 60)):
                        total_st = total_st + st[i]
                        total_tat = total_tat + tat[i]
                        print(" ", i + 1,"\t\t", at[i],"\t\t", bt[i],
                            "\t\t", rt[i],"\t\t", wt[i], "\t\t", ft[i],"\t\t", tat[i])
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
    """
    print("Minute 2")
    print("Processes\tArrival Time\tBurst Time\tResponse Time\tWaiting",
                    "Time\tFinish Time\tTurn-Around Time")
   
    for i in range(n):
        if(ft[i] > 60):
            if(ft[i] <= 120):
                total_st = total_st + st[i]
                total_tat = total_tat + tat[i]
                print(" ", i + 1,"\t\t", at[i],"\t\t", bt[i],
                "\t\t", rt[i],"\t\t", wt[i], "\t\t", ft[i],"\t\t", tat[i])
            
    print("Minute 3")
    print("Processes\tArrival Time\tBurst Time\tResponse Time\tWaiting",
                    "Time\tFinish Time\tTurn-Around Time")
    for i in range(n):
        if(ft[i] > 120):
            if(ft[i] <= 180):
                total_st = total_st + st[i]
                total_tat = total_tat + tat[i]
                print(" ", i + 1,"\t\t", at[i],"\t\t", bt[i],
                    "\t\t", rt[i],"\t\t", wt[i], "\t\t", ft[i],"\t\t", tat[i])
            
    print("Minute 4")
    print("Processes\tArrival Time\tBurst Time\tResponse Time\tWaiting",
                    "Time\tFinish Time\tTurn-Around Time")
    for i in range(n):
        if(ft[i] > 180):
            if(ft[i] <= 240):
                total_st = total_st + st[i]
                total_tat = total_tat + tat[i]
                print(" ", i + 1,"\t\t", at[i],"\t\t", bt[i],
                    "\t\t", rt[i],"\t\t", wt[i], "\t\t", ft[i],"\t\t", tat[i])
    """
    print("\nTotal\nAverage service time = %.5f "%(total_total_st /n) )
    print("Average turn around time = %.5f "% (total_total_tat / n))
    print("Ratio of Turn around time to Service time = %.5f "%(total_total_tat/total_total_st))
    maxft = 0
    for i in range(n):
        if(ft[i] > maxft):
            maxft = ft[i]
    print("Throughput = " + str(n/maxft))
    
    

if __name__ =="__main__":
    

    proc = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16 ,17, 18, 19, 20, 21, 22, 23 , 24, 25,
            26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
    n = len(proc)


    arrival_time = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44,
                    46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94]

    service_time = [6, 12, 8, 10, 4, 9, 10, 6, 9, 6, 7, 10, 13, 8, 4, 17, 8, 14, 2, 10, 11, 1, 15, 16, 17, 20,
                    25, 16, 13, 17, 13, 19, 5, 7, 18, 10, 15, 16, 15, 17, 12, 5, 3, 8, 10, 15, 17, 13]
    
    disk_time = [1,2,1,0,2,1,3,1,2,0,0,1,3,1,2,2,1,1,4,2,1,0, 1,2,3,6,1,2,1,3,2,1,4,1,3,2,3,3,1,2,2,1,1,0, 1, 2, 3, 4]
    disk_activity = [1,2,1,0,2,3,4,2,1,0,0,3,2,5,2,1,3,4,1,1,2,0, 3,2,3,1,6,2,1,3,1,5,2,1,3,2,3,1,2,5,1,2,3,0, 2, 1, 3, 4]
    burst_time = [0] * n
    
    for i in range(n):
        burst_time[i] = service_time[i] + (disk_time[i]*disk_activity[i])

   
    quantum = 1;
    findavgTime(proc, n, arrival_time, burst_time, quantum, service_time)



# In[ ]:





# In[ ]:




