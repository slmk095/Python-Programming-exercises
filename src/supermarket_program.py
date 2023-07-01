ch = True
total_prices = []

while ch:
    product = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    prices = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]
    opt = int(input("Please select product (1-10) 0 to Quit:"))
    print(opt)
    if opt == 0:
        print("Total:", sum(total_prices))
        sum_of_total = sum(total_prices)
        payment = int(input(""))
        print("Payment:",payment)
        change = payment - sum_of_total
        print("Change:", change)
        ch = False
    else:
        print("Product:",opt,"Price:", prices[opt - 1])
        total_prices.append(prices[opt - 1])

