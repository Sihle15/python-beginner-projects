def main():
    print("This is a monthly payment loan calculator")
    print("")

    principal = float(input("Please enter loan amount: "))
    annual_interest_rate = float(input("Please enter interest rate: "))
    years = int(input("Please enter years: "))

    monthly_interest_rate = annual_interest_rate / 100
    amount_of_months = years * 12
    total_loan = principal + (principal * monthly_interest_rate * years)
    monthly_loan_payment = total_loan / amount_of_months

    print(f"Total loan: {total_loan}")
    print(f"Total monthly repayment: {monthly_loan_payment}")


main()
