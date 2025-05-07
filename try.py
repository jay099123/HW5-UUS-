import random
import numpy as np
import math


sernum = 3       # server數量
serlist = [i for i in range(1, sernum + 1)] # server index從1開始
serverMS = [ 0 for _ in range(sernum)]       # 紀錄每個server最後完工時間
print("serverMS:", serverMS)

num_job = 10     # 共幾個工件
idserver = 0     # 某一工件進入系統時idle的機器數量
idserver_record = []  # 紀錄每一iteration是哪些server有idle
idserver_record.append([i for i in range(1, sernum + 1)]) # server index從1開始
 
A = [0.42, 3.64, 4.32, 7.36, 10.66, 11.0, 13.34, 16.96, 21.68, 22.27]          # A[i] = Arrival time of job i 
S = []         # S[i] = Starting time of job i 
C = []           # C[i] = Completion time of job i 
W = []           # W[i] = Waiting time of job i
server = []      # server[i] = Server index of job i
temp = []

interarrival_time = [0.42, 3.22, 0.68, 3.04, 3.3, 0.34, 2.34, 3.62, 4.72, 0.59]
service_time = [7.17, 5.39, 7.97, 9.02, 9.04, 8.04, 10.0, 6.32, 7.18, 6.41]

print("arrival_time(A):", A)
print("service_time:", service_time)
print("idserver_record:", idserver_record)


for i in range(1, num_job+1):
    if i == 1:                                  # 第一個工件直接指派給server1
        S.append(A[i-1])
        C.append(round(S[i-1] + service_time[i-1], 2))
        serverMS[0] = C[i-1]          # 紀錄server1的完工時間
        W.append(0)
        server.append(1)                        # 紀錄工件1的server index
        print("S", S)
        print("C:", C)
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
            C.append(round(S[i-1] + service_time[i-1], 2))
            W.append(0)
            server.append(idserver_record[i-1][0])
            print("server:", server)
            serverMS[idserver_record[i-1][0]-1] = C[i-1]  
            print("serverMS:", serverMS)
        else:                                   # 若無idle
            S.append(min(serverMS))
            C.append(round(S[i-1] + service_time[i-1], 2))
            W.append(round(S[i-1] - A[i-1], 2))
            server.append(serverMS.index(min(serverMS))+1)
            print("server:", server)
            serverMS[serverMS.index(min(serverMS))] = C[i-1]  
            print("serverMS:", serverMS)  
        

        idserver = 0

print("\n")
print("start: ", S)
print("completeion: ", C)
print("waiting: ", W)
print("server: ", server)
print("temp: ", temp)
print("idserver_record: ", idserver_record)


