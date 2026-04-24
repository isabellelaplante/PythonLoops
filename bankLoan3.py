loan_amount = input("Enter the loan amount: ")
interest_rate = float(input("Enter your annual interest rate: "))
payment = input("Enter the monthly payment: ")

#turns annual interest rate into monthly rate
monthly_interest = (interest_rate / 100) / 12
balance = float(loan_amount)
month = 0

#while loop to calculate the remaining balance after each payment
while balance > 0:
    interest = balance * monthly_interest
    balance = balance + interest - float(payment)
    month += 1


if balance < 0:
    balance = 0
print(f"After {month} months, the loan will be paid off.")

