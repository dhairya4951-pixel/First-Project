#Name:- Dhairya Sharma
#Enrolment NUmber:- 2502140023
inventory = {'A': {
        'Rice': {'qty': 50, 'price': 60},
        'Sugar': {'qty': 40, 'price': 45},
        'Milk': {'qty': 30, 'price': 25},
        'Bread': {'qty': 20, 'price': 30},
        'Butter': {'qty': 20, 'price': 120}
        },
    'B': {
        'Rice': {'qty': 35, 'price': 62},
        'Sugar': {'qty': 50, 'price': 44},
        'Milk': {'qty': 25, 'price': 27},
        'Eggs': {'qty': 60, 'price': 6},
        'Cheese': {'qty': 15, 'price': 150}
    }}
dayTotal = {'A':0,'B':0}
currentBill = []
def sell(store,item,qty):
    print("---------------- SELL ITEM ----------------")
    price = inventory[store][item]['price']
    if qty<=0:
        print("Invalid Quantity.")
        return
    if inventory[store][item]['qty']<qty:
        available = inventory[store][item]['qty']
        bill = inventory[store][item]['qty']*price
        remaining = qty-inventory[store][item]['qty']
        inventory[store][item]['qty'] = 0
        dayTotal[store]+=bill
        print(f"Sold {available} {item}(s) for {bill} and could not provide {remaining} items.")
        currentBill.append((item, qty-remaining, price, qty * price))
    elif inventory[store][item]['qty']==qty:
        bill = qty*price
        inventory[store][item]['qty'] = 0
        dayTotal[store]+=bill
        print(f"Sold {qty} {item}(s) for {bill}.")
    elif inventory[store][item]['qty'] >= qty:
        bill = qty*price
        inventory[store][item]['qty']-=qty
        dayTotal[store] += bill
        print(f"Sold {qty} {item}(s) for {bill}.")
        currentBill.append((item, qty, price, bill))
    print("------------------------------------------")
    return
def returnItem(store,item,qty):
    print("---------------- RETURN ITEM ----------------")
    if item not in inventory[store]:
        print(f"{item} does not exist in {store} store.")
    inventory[store][item]['qty'] += qty
    returnBill = inventory[store][item]['price'] * qty
    dayTotal[store] -= returnBill
    print(f"Returned {qty} item(s) to {store} for {returnBill}")
    print("------------------------------------------")
    return
def transfer(store,target,item,qty):
    print("---------------- STOCK TRANSFER ----------------")
    if item not in inventory[store]:
        print(f"The item does not exist in {inventory[store]} store")
        return
    if inventory[store][item]['qty']<qty:
        available = inventory[store][item]['qty']
        remaining = qty-inventory[store][item]['qty']
        inventory[store][item]['qty'] = 0
        print(f"Transfered {available} item(s) could not provide {remaining} item(s).")
    else:
        inventory[store][item]['qty']-=qty
        print(f"Transfered {qty} items(s).")
    if item not in inventory[target]:
        price = inventory[store][item]['price']
        inventory[target][item] = {'qty':0 , "price":price}
        inventory[target][item]['qty']+=qty
        inventory[store][item]['qty'] -= qty
    print(f"Transfered {item}(s) from {store} to {target}")
    print("------------------------------------------")
    return
def report():
    print("================= INVENTORY REPORT =================")
    for store in inventory:
        print(f"Store: {store}")
        for item in inventory[store]:
            qty = inventory[store][item]['qty']
            price = inventory[store][item]['price']
            print(f"Item name: {item} has {qty} quantity and its price is {price}")
    print("====================================================")
    return
def delete(store,item):
    print("---------------- DELETE ITEM ----------------")
    if item not in inventory[store]:
        print(f"{item} does not exixt in the store.")
        return
    inventory[store].pop(item)
    print(f"Removed {item} from the store.")
    print("------------------------------------------")
    return
def add(store,item,qty,price):
    print("---------------- ADD ITEM ----------------")
    inventory[store][item]= {'qty': qty, 'price': price}
    print(f"Added new item '{item}' to store {store} with {qty} units at ₹{price} each.")
    print("------------------------------------------")
    return
def modify(store, item,qty,price):
    print("---------------- MODIFY ITEM ----------------")
    if item not in inventory[store]:
        print(f"The {item} does not exist in store.")
        print("Do you want to add the item anyway?....")
        decision = input("Yes('Y') or NO ('N'): ").upper()
        if decision=='Y':
            inventory[store][item]={'qty':qty,'price':price}
        elif decision=="N":
            print("Item not added to the store.")
            return
        else:
            print("Wrong Input.")
        return
    inventory[store][item]['qty']=qty
    inventory[store][item]['price'] = price
    print("------------------------------------------")
    return
def sales(store):
    print("--------Daily Report---------")
    totalValue = 0
    for store in inventory:
        print(f"Store {store}:")
        for item in inventory[store]:
            qty = inventory[store][item]['qty']
            price = inventory[store][item]['price']
            value = qty * price
            totalValue += value
            print(f"{item}: qty={qty} , price = {price}, total={value}")
        print(f"Day total({store}): {dayTotal[store]}")
    print("-----------------------------")
    return
def search(item):
    print("---------------- SEARCH ITEM ----------------")
    for store in inventory:
        if item not in inventory[store]:
            print(f"The {item} does not exits in the store.")
        else :
            print(f"The quantity of {item} in {store} is: {inventory[store][item]['qty']}")
            print(f"The price of {item} in {store} is: {inventory[store][item]['price']}")
    print("------------------------------------------")
    return
def lowStock(store):
    print("---------------- LOW STOCK ITEMS ----------------")
    low = False
    for item in inventory[store]:
        qty = inventory[store][item]['qty']
        if qty<10:
            print(f"{item} is has low stock in the inventory.")
            low = True
    if not low:
        print("There is not item in the store that has quantity less than 10.")
    print("------------------------------------------")
    return
def totalBill():
    total = 0
    print("================ CUSTOMER BILL ================")
    for item, qty, price, subtotal in currentBill:
        print(f"{item} {qty} {price}: {subtotal}")
        total += subtotal
    print()
    print(f"The total bill is {total}")
    print("------------------------------------------")
    return
def itemsInStore(store):
    a =1
    print("---------- Items in Store ----------")
    for items in inventory[store]:
        print(f"{a}. {items}")
        a+=1
    print("------------------------------------------")
    return
def userInput():
    item = input("Enter the name of the item: ").strip()
    qty = int(input("Enter the quantity of the item: ").strip())
    return item,qty
def ownerInput1():
    target = input("Enter the store name to which you would like to transfer stock to: ")
    item = input("Which item do you want to transfer: ")
    qty = int(input("Enter the quantity of the item: "))
    return target,item,qty
def ownerInput2():
    item = input("Enter the item name: ")
    qty = int(input("Enter the quantity of the item: "))
    price = int(input("Enter the new price: "))
    return item,qty,price
attempt = 5 #This is a counter for the password attempts for the owner

print()
print("============Multi-Store Inventory & Billing (with Stock Transfer) System============")
print()

store = input("Which store do you want to perform operations in 'A' or 'B': ").upper().strip()
typeOfUser = input("Are you the Owner('O') or Customer('C'): ").upper().strip()
print()
while True:
    print()
    print("-----------------------------------------------")
    if typeOfUser=="O":
        enterPassword = input("Enter your password: ")
        password = "password"#This is the password for the owner
        if enterPassword==password:
            print("========= OWNER MENU =========")
            print("What do you want to do:- ")
            print("1.Transfer Stock across stores")
            print("2.Detail of the all the items across all the stores")
            print("3.Add new item in the store")
            print("4.Modify the product details")
            print("5.Remove item from the store.")
            print("6.Sales Report")
            print("7.Search detail of a specific item across all stores.")
            print("8.See items with low stock in inventory.")
            print("9.Exit the program")
            print("==============================")
            print()
            choice = int(input("Enter your choice [1-9]: "))
            if choice==1:
                target,item,qty = ownerInput1()
                transfer(store,target,item,qty)
            elif choice==2:
                report()
            elif choice==3:
                item,qty,price=ownerInput2()
                add(store,item,qty,price)
            elif choice ==4:
                item,qty,price=ownerInput2()
                modify(store,item,qty,price)
            elif choice ==5:
                item = input("Enter the item you would like to delete: ")
                delete(store,item)
            elif choice ==6:
                sales(store)
            elif choice ==7:
                item = input("Enter the name of item you would like to search: ")
                search(item)
            elif choice==8:
                lowStock(store)
            elif choice==9:
                print()
                print("Exiting the Multi-Store Inventory & Billing (with Stock Transfer) system.....")
                break
            else:
                print("Invalid choice")
        else:
            print("Wrong Password.")
            if attempt ==1:
                print("Exiting the program......")
                break
            attempt -= 1
            print("Attempts remaining:",attempt)
    elif typeOfUser=="C":
        print("========= CUSTOMER MENU =========")
        print("What do you want to do:- ")
        print("1.Buy items from the store")
        print("2.Return item to the store")
        print("3.Name of items in the store")
        print("4.Total Bill")
        print("5.Exit the program")
        print("=================================")
        print()
        choice = int(input("Enter your choice [1-5]: "))
        if choice==1:
            item,qty = userInput()
            sell(store,item,qty)
        elif choice==2:
            item,qty = userInput()
            returnItem(store,item,qty)
        elif choice==3:
            print()
            itemsInStore(store)
        elif choice==4:
            totalBill()
        elif choice==5:
            print()
            print("Exiting the Multi-Store Inventory & Billing (with Stock Transfer) system.....")
            break
        else :
            print("Invalid choice")
    else :
        print("Invalid Choice")
        break



