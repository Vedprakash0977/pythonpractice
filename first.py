# INPUT SECTION
total_rent = int(input("Enter your hostel/flat rent: "))
food = int(input("Enter your mess food charges: "))
electricity_spend = int(input("Enter the total electricity units used: "))
charge_per_unit = int(input("Enter the charge per unit: "))
gym_fees = int(input("Enter monthly gym charges: "))
additional_expenses = int(input("Enter total additional expenses: "))
persons = int(input("Enter total number of persons: "))

# CALCULATIONS
electricity_bill =(electricity_spend * charge_per_unit)

total_expense = (total_rent + food + electricity_bill + gym_fees + additional_expenses)

rent_per_person = total_rent / persons
food_per_person = food / persons
electricity_per_person = electricity_bill / persons
gym_per_person = gym_fees / persons
additional_per_person = additional_expenses / persons

amount_per_person = total_expense / persons

# OUTPUT (DETAILED BILL FORMAT)
print("\n----------------------------------------------------------------------")
print("                      MONTHLY EXPENSE BILL")
print("----------------------------------------------------------------------")

print(f" Hostel/Flat Rent          : ₹{total_rent}  ->  Per Person: ₹{rent_per_person:.2f}")
print(f" Mess Food Charges         : ₹{food}        ->  Per Person: ₹{food_per_person:.2f}")
print(f" Electricity Units ({electricity_spend} units @ ₹{charge_per_unit}/unit)")
print(f" Total Electricity Bill    : ₹{electricity_bill} ->  Per Person: ₹{electricity_per_person:.2f}")
print(f" Gym Fees                  : ₹{gym_fees}     ->  Per Person: ₹{gym_per_person:.2f}")
print(f" Additional Expenses       : ₹{additional_expenses} ->  Per Person: ₹{additional_per_person:.2f}")

print("----------------------------------------------------------------------")
print(f" TOTAL EXPENSE              : ₹{total_expense}")
print(f" AMOUNT PER PERSON          : ₹{amount_per_person:.2f}")
print("----------------------------------------------------------------------")
