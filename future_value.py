def investment():
    monthly_invest = float(input("\nEnter monthly investment:\t\t\t"))
    year_rate = float(input("Enter yearly interest rate:\t\t"))
    years = int(input("Enter number of years:\t\t\t"))
    
    futurevalue = 0
    for month in range(1, (years * 12) + 1):
        futurevalue += monthly_invest
        futurevalue += ((futurevalue*(year_rate/12)/100))
        
    print("Future value:\t\t\t\t\t%.2f" % futurevalue)
    
while True:
    investment()
    if input("\nContinue? (y/n): ").lower() != "y":
        print("\nBye!")
        break