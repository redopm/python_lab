num = int(input("Enter your choice number: "))
i=17

for choice in range(5):
    if i==num:
        print("Well Done! \n Your attempt is "+str(choice)+" out of 5")
        break
    elif i>num:
        print("Oops! increase your number. \n Your attempt is "+str(choice)+" out of 5")
        num = int(input("Enter your choice number: "))
    else:
        print("Oops! decrease your number. \n Your attempt is "+str(choice)+" out of 5")
        num = int(input("Enter your choice number: "))