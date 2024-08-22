#multithreading= running various trask at the same time concurrently
 #it is a way to run program faster like game and spotify example
 
import threading
import time
 
 #time in secs
def dog_walk():
    time.sleep(8)
    print("walk the dog in the morning")

def get_vegetbales():
    time.sleep(5)
    print(" get_vegetbales from walmart")  
    
def workout():
    time.sleep(2)
    print("working out")     
    
#in cases we have parameters in our function such as
def finish_lectures(lecture1, lecture2): #passed parameters
    time.sleep(7)
    print(f"you fnished your lectures such as {lecture1} {lecture2}") #printing parameters    
    #DONOT FORGET F FOR PRINTING PARAMETERS
   
    
#taskname=threading.Thread(target=functionname)   
#taskname.start() 
task1=threading.Thread(target=dog_walk)
task1.start()

task2=threading.Thread(target=get_vegetbales)
task2.start()

task3=threading.Thread(target=workout)
task3.start()
    
task4=threading.Thread(target=finish_lectures, args=("lecture1", "lecture2",))    #accepting parameters in thread # comma at the end make sure args are tuple an is mandatory
task4.start()

#to make sure all task is finished before moving further use taskname.join()
task1.join()
task2.join()
task3.join()
task4.join()

print("all task finished!")




    