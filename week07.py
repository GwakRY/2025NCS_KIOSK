import kiosk

if __name__ == "__main__":
    menu_drinks = ["Ice Americano", "Cafe Latte"]
    menu_prices = [2000, 3000]

    menu = kiosk.Menu(menu_drinks, menu_prices)
    order_processor = kiosk.OrderProcessor(menu) #<has a> relation,aggregation
    order_processor.run()

