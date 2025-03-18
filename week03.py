drinks = ["Ice Americano","Cafe Latte","watermelon Juice"]
prices = [2000, 3000, 4900]
amounts = [0] * len(drinks)

total_price = 0

#drinks = ["Ice Americano","Cafe Latte"]
#prices = [2000, 3000]
#amounts = [0,0]
#total_price = 0




def order_process(idx: int):
    global total_price
    print(f"{drinks[idx]} ordered. Price: {prices[idx]}won")
    total_price = total_price + prices[idx]
    amounts[idx] = amounts[idx] + 1


#list comprehension , string join 연산
menu_lists = " ".join([f" {k+1}) {drinks[k]} {prices[k]} won " for k in range(len(drinks))])
menu_lists = menu_lists + f" {len(drinks)+1}: EXIT: "

while True:
    #menu = input(f"1) {drinks[0]} {prices[0]}won "f" 2)Cafe Latte "f" 3)watermelon juice "f" 4) Exit: ")
    menu = int(input(menu_lists))

    if len(drinks) >= menu >= 1 :
       order_process(menu-1)
    elif menu == len(drinks)+1:
        print("Finish order~")
        break
    else:
        print(f"{menu} menu is not exist")

print("Product  Price   Amount  Subtotal")
for i in range (len(drinks)):
    if amounts[i] > 0:
        print(f"{drinks[i]} {prices[i]}X {amounts[i]}"
              f" {prices[i] * amounts[i]}")

print(f"total price : {total_price}")
