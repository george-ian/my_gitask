import math
# variable 'total' is the total return on investment
# variable 'repayment' is the monthly repayment on a home bond 
total = 0
repayment = 0
print("investment - to calculate the amount of interest you will earn on "
                                                        "your investment")
print('*'*82)
print("bond - to calculate the monthly amount that you will have to "
                                                "pay on a home loan")
print('*'*82)

def fintech():
    user_sel = input("Enter either 'investment' or 'bond' from the menu "
                                                    "above to proceed:\n")

    try:
        # The user can choose one of two options
        if user_sel.casefold() == "bond" or user_sel.casefold() =="investment":
            print("OK. Request received.")
            # if investment is selected I'm asking user for input and storing 
            # it in variables
            
            if user_sel.casefold() =="investment":
                deposit = int(input("Enter the amount of money "
                                    "that you are depositing: "))
                int_rate = int(input("Enter the number of the interest rate: "))
                number_years = int(input("Enter for how many years "
                                        "you are depositing: "))
                interest = (input("Choose simple or compound interest: \n")).casefold()
                if interest =="compound":
                    # If compound interest selected I'm using this formula to
                    # calculate the total amount
                    total = deposit* math.pow((1+ int_rate/100), number_years)
                elif interest =="simple":

                    total = ((int_rate/100)*number_years + 1)*deposit
                else:

                    print("Invalid user selection! Enter simple or compound:\n")

                print(f"The total amount you'll get back is: \n{round(total)}")
                
            # if user selects 'bond' I'm asking user for input and storing
            # it in variables
            else:
                present_value = int(input("Enter the present value of the house: "))
                int_rate = int(input("Enter the number of the interest rate: "))
                n = int(input("Enter for how many months you are planning "
                                                    "to repay the bond: "))
    
                repayment = (int_rate/1200 * present_value)/(1 - (1 + int_rate/1200)**(-n))
        
                print(f"You will have to repay each month: \n{round(repayment)}") 
            
        else:
            print("Invalid selection! Enter either 'investment' or 'bond' from "
                                                    "the menu above to proceed:")

    except ValueError:
        print("Invalid input from user! Please enter a number!")  
        
fintech()
        