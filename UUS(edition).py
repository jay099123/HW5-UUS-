# Assignment Rules：
# 1. first available server
# 2. If tied, smallest server index            創造一個陣列，包含job到來以及job完工的時間，再把它們升冪排序
#                                              檢查參數是否可行

import random
import numpy as np
import math
seed = 40
random.seed(seed)
# lower_bound = int(input("請輸入下界："))
# upper_bound = int(input("請輸入上界："))
# size = int(input("請輸入job數量："))
# sernum = int(input("請輸入sever數量："))
lower_bound = 0  # lower bound for uniform distribution
upper_bound = 10 # upper bound for uniform distribution

sernum = 3       # server數量
serlist = [i for i in range(1, sernum + 1)] # server index從1開始
serverMS = [ 0 for _ in range(sernum)]       # 紀錄每個server最後完工時間
print("serverMS:", serverMS)

num_job = 100     # 共幾個工件
intersum = 0 
idserver = 0     # 某一工件進入系統時idle的機器數量
idserver_record = []  # 紀錄每一iteration是哪些server有idle
idserver_record.append([i for i in range(1, sernum + 1)]) # server index從1開始
 
A = []           # A[i] = Arrival time of job i 
S = []           # S[i] = Starting time of job i 
C = []           # C[i] = Completion time of job i 
W = []           # W[i] = Waiting time of job i
server = []      # server[i] = Server index of job i
temp = []

# for s in range(sernum):
#     server.append(i+1)

interarrival_time = [round(random.uniform(0, 5), 2) for i in range(num_job)]
service_time = [round(random.uniform(5, 10), 2) for i in range(num_job)]
A = [round(sum(interarrival_time[:i+1]), 2) for i in range(num_job)]


for i in range(num_job):
    intersum += interarrival_time[i]

print("interarrival_time:", interarrival_time)
print("service_time:", service_time)
print("arrival_time:", A)
print(round(intersum, 2))
print(S)

# 第一個工件直接指派給server1
# 第二個開始：
#   1. 有idle：
#     a. 直接進入該idle server
#     b. 如果有多個idle，則選擇最小的server index
#   2. 沒有idle：
#     a. 等到有server idle(產生waiting time)
#     b. 注意如果有多個server同時idle，則選擇最小的server index(少數情況)

for i in range(1, num_job+1):
    if i == 1: 
        print("ROUND 1")                                 # 第一個工件直接指派給server1
        S.append(A[i-1])
        C.append(round(S[i-1] + service_time[i-1], 2))
        serverMS[0] = C[i-1]          # 紀錄server1的完工時間
        W.append(0)
        server.append(1)                        # 紀錄工件1的server index
        print("S:", S)
        print("C:", C)
        print("W:", W)
        print("server:", server) 
        print("serverMS:", serverMS)
    else:
        print("\n")
        print("ROUND", i)                                       # 第二個工件開始
        for j in range(1, sernum+1):                   # 確認idle server數量
            if A[i-1] >= serverMS[j-1]:
                idserver += 1
                temp.append(j)
        print("temp1:", temp, " #該輪idle server")               # 紀錄server index
        print("idserver:", idserver)                                    # 紀錄server index
        idserver_record.append(temp)
        print("idserver_record:", idserver_record)
        temp = []                           
        if idserver >= 1:                       # 若有idle
            S.append(A[i-1])
            print("S", S)
            C.append(round(S[i-1] + service_time[i-1], 2))
            print("C:", C)
            W.append(0)
            print("W:", W)
            server.append(idserver_record[i-1][0])
            print("server:", server)
            serverMS[idserver_record[i-1][0]-1] = C[i-1]  
            print("serverMS:", serverMS)
        else:                                   # 若無idle
            S.append(min(serverMS))
            print("S:", S)
            C.append(round(S[i-1] + service_time[i-1], 2))
            print("C:", C)
            W.append(round(S[i-1] - A[i-1], 2))
            print("W:", W)
            server.append(serverMS.index(min(serverMS))+1)
            print("server:", server)
            serverMS[serverMS.index(min(serverMS))] = C[i-1]  
            print("serverMS:", serverMS)  
        

        idserver = 0


print("\n")
print("arrival", A)
print("start: ", S)
print("completeion: ", C)
print("waiting: ", W)
print("server: ", server)
print("temp: ", temp)
print("idserver_record: ", idserver_record)

total_wait = 0
for x in W:
    total_wait += x
print("Average waiting time:", round(total_wait/num_job, 2))
