#EMI calculate
def calculate_emi(principal, annual_rate, time_in_months):
    # Convert annual interest rate to monthly rate
    monthly_rate = annual_rate / (12 * 100)

    #  formula
    emi = principal * monthly_rate * (1 + monthly_rate) ** time_in_months / ((1 + monthly_rate) ** time_in_months - 1)
    return emi

principal = float(input("Enter the principal loan amount: "))
annual_rate = float(input("Enter the annual interest rate (in %): "))
time_in_months = int(input("Enter the loan duration in months: "))


emi = calculate_emi(principal, annual_rate, time_in_months)
print(f"The EMI amount is: {emi:.2f}")
