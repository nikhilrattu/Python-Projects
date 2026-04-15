print("Welcome to the Tip Calculator\n")
bill=float(input("Enter the bill amount\n"))
persons=int(input("Enter the no. of people\n"))
tip=float(input("Enter the tip percentage\n"))
tip_final=float(0.12*bill)
total=(bill+tip_final)/persons
print(f"The total amount to be paid by each person is ${round(total,2)}")