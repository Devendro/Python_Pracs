principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (as a decimal): "))
time = float(input("Enter the time (in years): "))
compound_interest = principal * (1 + rate/100)**time - principal
print("The compound interest is ", compound_interest)
