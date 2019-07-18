a = input("Enter type to print  number such as odd/even: ")
if 'odd' in a:
    number_input = int(input("Enter Range to print number: "))
    for number in number_input:
        number = number%2!=0
        print(number)
