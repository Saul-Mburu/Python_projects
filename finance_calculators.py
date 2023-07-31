import math
print("investment - to calculate the amount of interest you'll earn on your investment ")
print("bond - to calculate the amount you'll have to pay on a home loan")
print('\n')
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if user_choice == 'investment':
    in_amount = int(input("Please enter the amount of money you are depositing: "))
    in_interest = int(input("Please enter the interest rate.(Only the number): "))
    in_years = int(input("please enter the number of years you plan to invest: "))
    in_choice = input("Would you want 'simple' or 'compound' interest?:  ").lower()
   
    interest = in_choice
    r = in_interest / 100

    if interest == 'simple':
        print("This would amount to: ", in_amount*(1+r*in_years) )
    elif interest == 'compound':
        print("This would amount to: ", in_amount*math.pow((1+r),in_years))
    else:
        print("Error! Please enter an option")
    
elif user_choice == 'bond':
   value = int(input("Please enter the present value of your house: "))
   b_interest = int(input("Please enter the interest rate.(Only the number): "))
   months = int(input("Please enter the number of months do you plan to repay the bond?: "))
   annual = b_interest / 100
   i = annual / 12
   print("The amount that will need to be repaid each month is: ", (i*value)/(1-(1+i)**(-months)) )
else:
    print('Error!!! Please enter one of the options from above. ')

