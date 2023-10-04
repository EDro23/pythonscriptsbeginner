def header():
    print("BLACKJACK!\n")
    print("Blackjack payout is 3:2")
    print("Enter 'x' for bet to exit\n")
    
def odds():
    program = True
    start_bal = float(input("Starting Money: "))
    while program:
        import random
        
        bet_amount = (input("Bet amount: "))

        if bet_amount == 'x':
            break
        num = random.randint(1,100)
        if num > 95:
            start_bal = start_bal + (1.5*float(bet_amount))
            print("You got blackjack!")
            print("Money:  {}\n".format(start_bal))
        elif num > 55 and num < 95:
            start_bal = start_bal + (float(bet_amount))
            print("You got a win!")
            print("Money:  {}\n".format(start_bal))
        elif num < 55 and num > 49:
            start_bal = start_bal
            print("You pushed")
            print("Money:  {}\n".format(start_bal))
        else:
            start_bal = start_bal - (float(bet_amount))
            print("You lost :(")
            print("Money:  {}\n".format(start_bal))
        
header()
odds()
print("Bye!")