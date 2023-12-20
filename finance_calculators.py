'''import math is used for methods and constants of the module.'''
import math       

#investment = "To calculate the amount of interest user can earn on the investment"

financial_calculator = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
invest = "investment"
bond = "bond"

#if user type investment.Next step user can check simple and compound interest of the amount

if invest == financial_calculator.lower():

    user_input = input("Do you want to calculate the simple or compound interest: ")
    original_amount = "simple"
    saving_amount = "compound"
  
    if original_amount == user_input.lower():
        P = float(input("Enter the deposit amount: "))
        t = float(input("Number of years the money invested: "))
        r = float(input("Enter the rate of interest: "))

        simple_interest = P *(1 + (r/100)*t) #formulae to calculate the simple interest
        print("Simple interest is: ", simple_interest)
      
    elif saving_amount == user_input.lower():                                             
        P = float(input("Enter the deposit amount: "))
        t = float(input("Number of years the money invested: "))
        r = float(input("Enter the rate of interest: "))

        compound_interest = P * math.pow((1+r/100),t)  #formulae to calculate the compound interest
        print("Compound interest is: ", compound_interest)
     
    else:         #if user press 'no' or any other credentials,else statement will be execute. 
        print("Invalid input")       
  
        #bond = "To calculate the amount you'll have to pay on a home loan" 

elif bond == financial_calculator.lower():  #if user type bond 
    value_repay = True    #if value_repay is True, check the repayment method
    if value_repay:
        P = float(input("Enter the present value of the house: "))
        i = float(input("Enter the monthly interest rate: "))
        n = float(input("Number of months to repay the bond: " ))
        repayment =(((i/100)/12) * P)/(1 - (1 + ((i/100)/12))**(-n)) #formulae to calculate the repayment of the home loan each month 
        print("Each month the user have to repay is: ", repayment)

else:   #if user press other than 'investment' or 'bond' else statement will execute.
    print("Invalid input")
