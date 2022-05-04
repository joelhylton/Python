sales_person_number = int(input("Enter your sales person number: "))

sales_amount = int(input("Enter your sales amount: "))


commission1 = sales_amount * 0.06   # class1
commission2 = sales_amount * 0.07   # class1
commission3 = sales_amount * 0.1    # class1
commission4 = sales_amount * 0.04   # class2
commission5 = sales_amount * 0.06   # class2
commission6 = sales_amount * 0.045  # class3

Class = int(input("Enter class: "))


if Class == 1:
    if sales_amount <= 1000:
        commission1 = sales_amount * 0.06
        print(str(sales_person_number) + " commission is $" + str(commission1))
    elif sales_amount > 1000 and sales_amount < 2000:
        commission2 = sales_amount * 0.07
        print(str(sales_person_number) + " commission is $" + str(commission2))
    elif sales_amount >= 2000:
        commission3 = sales_amount * 0.1
        print(str(sales_person_number) + " commission is $" + str(commission3))

if Class == 2:
    if sales_amount < 1000:
        commission4 = sales_amount * 0.04
        print(str(sales_person_number) + " commission is $" + str(commission4))
    elif sales_amount >= 1000:
        commission5 = sales_amount * 0.06
        print(str(sales_person_number) + " commission is $" + str(commission5))

if Class == 3:
    commission6 = sales_amount * 0.045
    print(str(sales_person_number) + " commission is $" + str(commission6))

if Class < 1 or Class > 3:
    print("Please enter a valid class")



