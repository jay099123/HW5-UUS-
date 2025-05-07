import random
import numpy as np
import math
# seed = 40
# random.seed(seed)

"""
Inputting the parameters for the simulation
1. Lower and upper bounds for interarrival time
2. Lower and upper bounds for service time
3. Number of servers
4. Number of jobs

"""
def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

while True:

    a = get_valid_float("Enter lower bound for interarrival time: ")
    b = get_valid_float("Enter upper bound for interarrival time: ")
    c = get_valid_float("Enter lower bound for service time: ")
    d = get_valid_float("Enter upper bound for service time: ")
    S = get_valid_int("Enter the number of servers: ")
    n = get_valid_int("Enter the number of jobs: ")

    """
    Setting lists and variables for the simulation

    """
    serlist = [i for i in range(1, S + 1)]      # server index for each server
    serverMS = [ 0 for _ in range(S)]           # server time(for completing the current job) for each server

    idserver = 0                                               # number of idle servers when a job arrives                                
    idserver_record = []                                       # record of idle server index for each job                              
    idserver_record.append([i for i in range(1, S + 1)])       # idserver_record when the fist job comes in
    
    A = []          # arrival time for each job   
    Start = []      # starting time for each job     
    C = []          # completion time for each job
    W = []          # waiting time for each job
    server = []     # server index for each job
    temp = []       # temporary list to store idle server index for each job

    interarrival_time = [random.uniform(a, b) for i in range(n)]    # interarrival time for each job based on uniform distribution[a,b]
    service_time = [random.uniform(c, d) for i in range(n)]         # service time for each job based on uniform distribution[c,d]
    A = [sum(interarrival_time[:i+1]) for i in range(n)]            # arrival time for each job based on interarrival time


    for i in range(1, n+1):
        if i == 1:                  # for the first job, directly assign it to server 1                          
            Start.append(A[i-1])
            C.append(Start[i-1] + service_time[i-1])
            serverMS[0] = C[i-1]      
            W.append(0)
            server.append(1)              
        else:                        # for the rest of the jobs, check if there are idle servers first           
            for j in range(1, S+1):                  
                if A[i-1] >= serverMS[j-1]:
                    idserver += 1
                    temp.append(j)                                 
            idserver_record.append(temp)
            temp = []                           
            if idserver >= 1:                   # idle server exsiting case            
                Start.append(A[i-1])
                C.append(Start[i-1] + service_time[i-1])
                W.append(0)
                server.append(idserver_record[i-1][0])
                serverMS[idserver_record[i-1][0]-1] = C[i-1]  
            else:                                
                Start.append(min(serverMS))     # idle server not existing case(will have to wait)
                C.append(Start[i-1] + service_time[i-1])
                W.append(Start[i-1] - A[i-1])
                server.append(serverMS.index(min(serverMS))+1)
                serverMS[serverMS.index(min(serverMS))] = C[i-1]  


            idserver = 0


    total_wait = sum(W)
    print("Average waiting time:", round(total_wait/n, 4))
    # print("Makespan: ", round(max(serverMS), 4))

    repeat = input("Do you want to run the simulation again? (y/n): ").strip().lower()
    if repeat == "n":
        print("Exiting the program.")
        break
    elif repeat == "y":
        continue
    else:
        print("Invalid input. Please type 'y' or 'n'.")
