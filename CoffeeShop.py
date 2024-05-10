sizeS= 9
sizeM= 12
sizeL= 15

costS = 1.75
costM = 1.90
costL = 2.00

def print_menu():
    print("1: Enter 1 to order coffee.")
    print("2: Enter 2 to check the total money made up to this time.")
    print("3: Enter 3 to check the total amount of coffee sold up to this time.")
    print("4: Enter 4 to check the number of cups of each size sold.")
    print("5: Enter 5 to print the data.")
    print("9: Enter 9 to exit the program.")

def order_coffee():
    cupS_sold = 0
    cupM_sold = 0
    cupL_sold = 0
    cupTotal_sold = 0
    moneyTotal_made = 0
    while True:
        print("1: Enter 1 to buy coffee in a small cup size (9 oz)")
        print("2: Enter 2 to buy coffee in a small cup size (12 oz)")
        print("3: Enter 3 to buy coffee in a small cup size (15 oz)")
        print("9: Enter 9 to exit.")
        num = input()
        if num == "1":
            cups = int(input("Enter the number of cups: "))
            cupS_sold += cups
            cupTotal_sold += cups
            moneyTotal_made += cups * costS
        elif num == "2":
            cups = int(input("Enter the number of cups: "))
            cupM_sold += cups
            cupTotal_sold += cups
            moneyTotal_made += cups * costM
        elif num == "3":
            cups = int(input("Enter the number of cups: "))
            cupL_sold += cups
            cupTotal_sold += cups
            moneyTotal_made += cups * costL
        elif num == "9":
            print(f"Please pay: ${moneyTotal_made:.2f}")
            break

def check_money_made():
    print(f"Total money made: ${moneyTotal_made:.2f}")

def check_coffee_sold():
    total_ounces = (cupS_sold* sizeS) + (cupM_sold*sizeM) + (cupL_sold* sizeL)
    print(f"Total amount of coffee sold: {total_ounces} oz")

def check_cups_sold():
    print(f"Small cups count: {cupS_sold}")
    print(f"Medium cups count: {cupsM_sold}")
    print(f"Large cups count: {cupL_sold}")

def print_data():
    check_cups_sold()
    check_coffee_sold()
    check_money_made()

def main():
    cupS_sold = 0
    cupM_sold = 0
    cupL_sold = 0
    cupTotal_sold = 0
    moneyTotal_made = 0
    while True:
        print_menu()
        choice = input()
        if choice == "9":
            print(f"Please pay: ${total_money_made:.2f}")
            break
        elif choice == "1":
            order_coffee()
        elif choice == "2":
            check_money_made()
        elif choice == "3":
            check_coffee_sold()
        elif choice == "4":
            check_cups_sold()
        elif choice == "5":
            print_data()
        else:
            break
main()
