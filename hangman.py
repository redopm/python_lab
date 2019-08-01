import time 

name = input("Enter your name :")
print ("Hello "+name," Time for play hangman game.")

print ("")

time.sleep(0.5)

print("Start Gussing word...")
time.sleep(0.5)

word="programming"

gusses=" "

turns=10

while turns>0:
    failed=0
    for char in word :
        if char in gusses:
            print(char, end="")
        else:
            print("_", end="")
            failed+=1
    if failed==0:
        print ("You Won")
    break

print()

guess=input("guess a character:")

gusses+=guess

if guess not in word:
    turns -= 1
    print ("Wrong")

print("You have ", turns," more guesses")

if turns==0:
    print ("You Loose")