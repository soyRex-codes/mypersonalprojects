import time
#lower() must use () these bracets or the result of lower will not be stored

print("Hi, do you want to play a fun quiz game?, enter yes/no ")
player_response = input().lower() # assign the result to player_response

if  player_response == "yes":
    print("welcome to the game: lets get the fun begin")
else:
    print("okay, bye")
    #exit() #quit the game
#Ctrl+C quits the terminal
score=0

print("Enter your name?")
name=input()
print("select any Level, 1 to 100")
LEVEL=input()
print("GAME MODE: EASY, MEDIUM, HARD")
Mode=input()
print("GAME STARTS IN ....")
for i in range (5, 0, -1):
    print(i)
    time.sleep(1) #wait 1 sec
    print(name+ "Lets GO! , LEVEL: "+ str(LEVEL) + ", Mode: " + str(Mode))
    print("\n")

#Q1
print("Q1:who is Tom cruis, actor/politician")
player_response = input().lower()
if player_response == "actor":
    print("correct")
    score +=1
else:
    print("incorrect")
#Q2
print("Q2:is green mango sweet or tangy")
player_response=input().lower()
if player_response =="tangy":
    print("correct")
    score +=1
else:
    print("incorrect")

#Q3
print("Q3:who is Elon Musk, influencer or Businessman")
player_response=input().lower()
if player_response =="Businessman":
    print("correct")
    score +=1
else:
    print("incorrect")

print("final Score loading.......")

time.sleep(5) #wait for 3seconds
print(name +" scored " + str(score) +" points")

  

