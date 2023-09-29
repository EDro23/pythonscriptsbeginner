def main():
  print("Shipping Calculator")
  subtotal = calc_subtotal()
  shipping = calc_shipping(subtotal)
  calc_total(subtotal,shipping)

def calc_subtotal():
    subtotal = float(input("Cost of Items Ordered: $"))
    while subtotal <= 0:
        print("You must enter a positive number. Please try again.")
        subtotal = float(input("Cost of Items Ordered: $"))
    return subtotal

def calc_shipping(subtotal):
    if subtotal >= 1 and subtotal <= 29.99:
        shipping = 5.95
        print("Shipping Cost: $5.95")
    if subtotal >= 30 and subtotal <= 49.99:
        shipping = 7.95
        print("Shipping Cost: $7.95")
    if subtotal >= 50 and subtotal <= 74.99:
        shipping = 9.95
        print("Shipping Cost: $9.95")
    if subtotal >= 75:
        shipping = 0
        print("Shipping Cost: Free")
    return shipping

def calc_total(subtotal,shipping):
    total = subtotal + shipping
    print("Total Cost: $" + str(round(total,2)))
    print("Thank you for using our shipping calculator!")

main()