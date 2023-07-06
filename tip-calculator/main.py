total = float(input("Enter total bill : $"))
tip = int(input("How much tip do you want to give- 10,12,15?: "))
people = int(input("How many people are paying ? : "))
bill_with_tip = total * (1 + (tip / 100))
split = bill_with_tip / people
result = "{:.2f}".format(split)

print(f"You should pay {result} dollars")
