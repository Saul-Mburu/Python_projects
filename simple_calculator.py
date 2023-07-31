def option():
    num1= float(input("Enter the first number: "))
    function =  input(
        "What function would tou like to perform To ADD, SUBTRACT, "
        "DIVIDE or TIMES enter(+,-,/,*): "
        )
    num2= float(input("Enter the first number: "))
    print("\n")
    return function, num1, num2 

def try_again():
    user_input = int(input("Enter 1 to use calculator again. \n"
                       "Enter 2 to end: "))
    print("\n")
    if user_input == 1:
        calc()
    elif user_input == 2:
        print("Thank you for using the simple calculator")
    else:
        print("Please enter a valid key")
        try_again()

def calc():
    print("----Simple calculator---- \n")
    function, num1 , num2 = option()
    if function == "+":
        print("{}".format(num1+num2))
    elif function == "-":
        print("{}".format(num1-num2))
    elif function == "*":
        print("{}".format(num1*num2))
    elif function == "/":
        try:
            print("{}".format(num1/num2))
        except ZeroDivisionError:
            print("Sorry but you can't divide by zero")
            print("\n")
    else:
        print("Please enter a valid key")
    try_again()

calc()























