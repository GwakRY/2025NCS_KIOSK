drinks=["ice americano","cafe latte","Watermelon juice"]
prices=[2000,3000,4900]
total_price=0
amounts=[0]*len(drinks)

DISCOUNT_THRESHOLD = 10000
DISCOUNT_RATE = 0.1

def apply_discount(price: int):
    """
    If the total amount exceeds a certain threshold, the discount rate is reflected
    :param price: price before discount
    :return: price after discount
    """
    if price >= DISCOUNT_THRESHOLD:
        discount = price * DISCOUNT_RATE
        return price - discount
    return price


def order_process(idx: int):
    """
    Functions that address the beverage order display function,
    the total cumulative amount ajjeogu
    :param idx: list's index number
    """
    global total_price
    print(f"{drinks[idx]} ordered. Price: {prices[idx]} won")
    total_price += prices[idx]
    amounts[idx] += 1


menu_lists="".join(f"{k+1}) {drinks[k]} {prices[k]}won  " for k in range(len(drinks)))
menu_lists+=f"{len(drinks)+1}) Exit: "

help(order_process)
while True:
    try:
        menu = int(input(menu_lists))
        if 1<=menu<=len(drinks):
            order_process(menu-1)
        elif menu==len(drinks)+1:
            print("finish order~")
            break
        else:
            print(f"{menu} menu is invalid. pleas choose from above menu.")
    except ValueError as err:
        print(f"You cannot enter characters. Please enter a valid number.\n{err}")

print("Product  Price  Amount  Total")
for i in range(len(drinks)):
    if amounts[i]>0:
        print(f"{drinks[i]} {prices[i]} x{amounts[i]} {prices[i] * amounts[i]}")

discounted_price = apply_discount(total_price)
discount_amount = total_price - discounted_price

print(f"Total Original price: {total_price}won")

if discount_amount >0:
    print(f"Discount amount: {total_price}won :{discount_amount}won ")
    print(f"Total price after discount {discounted_price}won")
else:
    print("Discount not applied")
    print(f"Total price discount {total_price}won")
