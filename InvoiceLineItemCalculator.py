#Marty Wallace CIS261 Invoice Line Item Calculator

print("The Invoice Line Item Calculator")
print()

def enter_price():
    try:
        global price
        price = float(input("Enter Price: "))
        if price >= 0:
            return price
        else:
            print("Invalid decimal number. Please try again.")
            enter_price()
    except:
        print("Invalid decimal number. Please try again.")
        enter_price()
        
def enter_quantity():
    try:
        global quantity
        quantity = int(input("Enter Quantity: "))
        if quantity >= 0:
            return quantity
        else:
            print("Invalid integer. Please try again.")
            enter_quantity()
    except:
        print("Invalid integer. Please try again.")
        enter_quantity()

def calc_total():
    global total
    total = round(price * quantity, 2)
    print(f"Price:     {price}")
    print(f"Quantity:     {quantity}")
    print(f"Total:     {total}")
    
def main():
    while True:
        enter_price()
        enter_quantity()
        calc_total()
        quitOrCont = input("Enter another line item? (y/n)")
        if quitOrCont.lower() == "n":
            print("Bye!")
            break
        elif quitOrCont.lower() == "y":
            main()
            
        
if __name__ == "__main__":
    main()
        