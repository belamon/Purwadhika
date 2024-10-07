# #market program 

# apple_price = 10000 #price for each fruits 
# orange_price = 15000
# grape_price = 20000

# amount_apple = int(input("Masukkan jumlah apel yang diinginkan"))   #fruit input columns
# amount_orange = int(input("Masukkan jumlah jeruk yang diinginkan"))
# amount_grape = int(input("Masukkan jumlah anggur yang diinginkan "))

# total_apple_price = amount_apple * apple_price  #calculate the price 
# total_orange_price = amount_orange * orange_price 
# total_grape_price = amount_grape * grape_price 

# total_price = total_apple_price + total_orange_price + total_grape_price

# print("Detail Belanja")
# print(f"Apel: {amount_apple} x Rp {apple_price} = Rp {total_apple_price}")
# print(f"Jeruk: {amount_orange} x Rp {orange_price} = Rp  {total_orange_price}")
# print(f"Anggur: {amount_grape} x Rp {grape_price} = Rp {total_grape_price}")


# print(f"Total Belanja Anda Adalah: Rp {total_price}")


# #exercise 2 

# money = int(input("Masukkan jumlah uang"))

# under_budget = total_price - money
# over_budget = money - total_price

# if money < total_price:         #conditions
#     print(f"Transaksi Anda Dibatalkan, Uang Anda Kurang Sebesar Rp {under_budget} ")
# elif money > total_price:
#     print(f"Uang Kembali Anda Rp {over_budget}")
# elif money == total_price:
#     print("Transaksi Anda Berhasil Terima kasih")

#exercise 4 

# Fruit prices
fruit_prices = { 
    'Apple': 10000,
    'Orange': 15000,
    'Grapes': 20000
}

# Fruit stock
fruit_stock = {
    'Apple': 10,
    'Orange': 12,
    'Grapes': 20 
}

# Get the amount of apples
while True:
    try:
        amount_of_apple = int(input("Enter the amount of apples you want to buy: "))
        if amount_of_apple <= fruit_stock['Apple']:
            break
        else:
            print(f"The amount of apples you entered exceeds stock. Available stock: {fruit_stock['Apple']}. Please enter again.")
    except ValueError:
        print("Please enter a valid number.")

# Get the amount of oranges
while True:
    try:
        amount_of_orange = int(input("Enter the amount of oranges you want to buy: "))
        if amount_of_orange <= fruit_stock['Orange']:
            break
        else:
            print(f"The amount of oranges you entered exceeds stock. Available stock: {fruit_stock['Orange']}. Please enter again.")
    except ValueError:
        print("Please enter a valid number.")

# Get the amount of grapes
while True:
    try:
        amount_of_grapes = int(input("Enter the amount of grapes you want to buy: "))
        if amount_of_grapes <= fruit_stock['Grapes']:
            break
        else:
            print(f"The amount of grapes you entered exceeds stock. Available stock: {fruit_stock['Grapes']}. Please enter again.")
    except ValueError:
        print("Please enter a valid number.")

# Calculate total price
total_apple_price = amount_of_apple * fruit_prices['Apple']
total_orange_price = amount_of_orange * fruit_prices['Orange']
total_grape_price = amount_of_grapes * fruit_prices['Grapes']

total_price = total_apple_price + total_orange_price + total_grape_price

# Payment process
while True:
    try:
        money = int(input(f"The total price is {total_price}. Enter the amount of money you have: "))
        if money < total_price:
            under_budget = total_price - money
            print(f"Transaction cancelled. You need {under_budget} more.")
            break
        elif money > total_price:
            change = money - total_price
            print(f"Your change is {change}. Transaction successful, thank you!")
            break
        else:
            print("Transaction successful, thank you!")
            break
    except ValueError:
        print("Please enter a valid amount of money.")