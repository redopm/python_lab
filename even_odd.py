b=input("Enter even/odd type such as you want to do 1- List, 2- check Number : ")
if "list" in b:
    a= input("Enter number type such as 1- Even, 2- Odd:  ")
    if 'odd' in a :
        num = int(input("Enter range of  number : "))
        for num in range(1, num+1):
            if (num%2!=0):
                print("{0}".format(num))
    elif 'even' in a:
        num = int(input("Enter range of number : "))
        for num in range(1, num+1):
            if (num%2==0):
                print("{0}".format(num))
    else:
        print("Please enter in lower case!")
elif "check number" in b:
    c=int(input("Enter your number to check: "))
    if (c%2==0):
        print("Even Number")
    else:
        print("Odd Number")
else:
    print("Please enter in lower case!")


