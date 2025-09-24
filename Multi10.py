import multiprocessing
import time
import os

def SumEven(no):
    print("PID of sumeven task is",os.getpid())  
    print("PPID of sumeven task is",os.getppid())  #101
    
    sum = 0
    for i in range(1,no+1,2):
        sum = sum+i
    print (sum)  

def SumOdd(no):
     print("PID of sumodd task is",os.getpid())
     print("PPID of sumodd task is",os.getppid())  #101
     sum = 0
     for i in range(2,no+1,2):
        sum = sum + i
     print (sum)  

def main():
    print("PID of main process is :",os.getpid())
    print("Demonstration of parallel execution")

    start_time = time.time()

    T1 = multiprocessing.Process(target = SumEven, args = (900000000,))
    T2 = multiprocessing.Process(target = SumOdd, args = (900000000,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    end_time = time.time()
    print("time required for execution is : ",end_time-start_time)

    
    print("End of main")


if __name__ == "__main__":
    main()    
       