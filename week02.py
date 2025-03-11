# 1) Ice Americano : 2000 2) Cafe Latte : 3000

drinks = ["Ice Americano","",""]
prices = [2000, 3000]
total_price = 0
order_list =''
while True:
    menu = input(f"1) {drinks[0]}{prices[0]}won "
                 f" 2)Cafe Latte "
                 f" 3) Exit: ")
    if menu == "1":
        print(f"{drinks[0]} ordered. Price: {prices[0]}won")
        total_price = total_price + prices[0]
        order_list = order_list + drinks[0]+'\n'
    elif menu == "2":
        print("Cafe Latte ordered. Price: 3000won")
        total_price = total_price + prices[1]
        order_list = order_list + drinks[1] + '\n'
    elif menu == "3":
        print("Finish order~")
        break
    else:
        print(f"{menu} menu is not exist")

print(f"total pricee : {total_price}")
print(order_list)