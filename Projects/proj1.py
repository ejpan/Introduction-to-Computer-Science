##Monthly Mortgage Calculator##
##Demili Pichay and Eric Pan##
##February 12, 2021##

outstanding_balance=float(input("Enter the outstanding balance of the account:"))
monthly_payment=float(input("Enter the month's payment:"))


annual_interest_rate=0.0625
monthly_interest_rate= annual_interest_rate / 12

interest_paid=outstanding_balance * monthly_interest_rate


amount_applied_to_principal= monthly_payment - interest_paid


new_outstanding_balance=outstanding_balance - amount_applied_to_principal


print("Here is the breakdown of the payment:")
print("interest paid:")
print("$",format(interest_paid,".2f"))
print("Amount applied to principal:")
print("$",format(amount_applied_to_principal,".2f"))
print("After the payment, the account balance is:")
print("$",format(new_outstanding_balance,".2f"))



