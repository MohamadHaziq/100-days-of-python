## Tip Calculator
print("Welcome to the Tip Calculator")

bill = input("What was the total bill? RM")
tip = input("What is the tip percentage to give? ")
people_sharing = input('How many people sharing ? ')

amount_to_pay = (int(bill) * float(int(tip) / 100 + 1)) / int(people_sharing)

print(f"Each person needs to pay: RM{round(amount_to_pay, 2)}")
