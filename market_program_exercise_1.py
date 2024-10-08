#market program 

apple_price = 10000 #price for each fruits 
orange_price = 15000
grape_price = 20000

amount_apple = int(input("Masukkan jumlah apel yang diinginkan"))   #fruit input columns
amount_orange = int(input("Masukkan jumlah jeruk yang diinginkan"))
amount_grape = int(input("Masukkan jumlah anggur yang diinginkan "))

total_apple_price = amount_apple * apple_price  #calculate the price 
total_orange_price = amount_orange * orange_price 
total_grape_price = amount_grape * grape_price 

total_price = total_apple_price + total_orange_price + total_grape_price

print("Detail Belanja")
print(f"Apel: {amount_apple} x Rp {apple_price} = Rp {total_apple_price}")
print(f"Jeruk: {amount_orange} x Rp {orange_price} = Rp  {total_orange_price}")
print(f"Anggur: {amount_grape} x Rp {grape_price} = Rp {total_grape_price}")


print(f"Total Belanja Anda Adalah: Rp {total_price}")


#exercise 2 

money = int(input("Masukkan jumlah uang"))

under_budget = total_price - money
over_budget = money - total_price

if money < total_price:         #conditions
    print(f"Transaksi Anda Dibatalkan, Uang Anda Kurang Sebesar Rp {under_budget} ")
elif money > total_price:
    print(f"Uang Kembali Anda Rp {over_budget}")
elif money == total_price:
    print("Transaksi Anda Berhasil Terima kasih")

exercise 4 

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


#task 6 

# Menu of fruits with stock and price
fruits = {
    "Apel": {"stock": 20, "harga": 10000},
    "Jeruk": {"stock": 15, "harga": 15000},
    "Anggur": {"stock": 25, "harga": 20000}
}

# Initialize an empty cart
cart = []

# Function to display menu
def get_menu_choice():
    """Displays the menu options."""
    print("Selamat Datang di Pasar Buah")
    print("1. Menampilkan Daftar Buah")
    print("2. Menambah Buah")
    print("3. Menghapus Buah")
    print("4. Membeli Buah")
    print("5. Exit Program")

    while True:   # Ask user for menu input
        try:
            menu = int(input("Input your menu choice (1-5): "))
            if 1 <= menu <= 5:
                return menu
            else:
                print("Please choose a number between 1-5")
        except ValueError:
            print("Invalid input, please enter a number.")

# Function to show the list of fruits with index
def show_fruits():
    print(" | Index | Nama  | Stock | Harga")
    for index, (fruit, details) in enumerate(fruits.items()):
        print(f"| {index:<6} | {fruit:<6} | {details['stock']:<5} | {details['harga']:<6} |")

# Function to add a fruit
def add_fruit():
    name = input("Enter fruit name: ")
    stock = int(input("Enter fruit stock: "))
    price = int(input("Enter fruit price: "))
    fruits[name] = {"stock": stock, "harga": price}
    print(f"{name} has been added to the list.")

# Function to remove a fruit by index
def remove_fruit():
    show_fruits()
    try:
        index = int(input("Enter the index of the fruit to remove: "))
        fruit_name = list(fruits.keys())[index]  # Get the fruit name based on the index
        del fruits[fruit_name]
        print(f"{fruit_name} has been removed from the list.")
    except (IndexError, ValueError):
        print("Invalid index. Please try again.")

# Function to display the cart
def show_cart():
    if not cart:
        print("\nYour cart is empty.")
    else:
        print("\nYour Cart:")
        print(" | Fruit Name | Quantity | Total Price |")
        total_cart_price = 0
        for item in cart:
            fruit_name = item['name']
            quantity = item['quantity']
            total_price = item['total_price']
            total_cart_price += total_price
            print(f"| {fruit_name:<12} | {quantity:<8} | {total_price:<11} |")
        print(f"Total Price in Cart: {total_cart_price}")

def buy_fruit():
    while True:
        show_fruits()
        try:
            index = int(input("Masukkan index buah yang ingin dibeli: "))
            fruit_name = list(fruits.keys())[index]  # Get the fruit name based on the index
            
            if fruit_name in fruits:
                quantity = int(input(f"Masukkan jumlah yang ingin dibeli: "))
                
                if quantity <= fruits[fruit_name]['stock']:
                    total_price = quantity * fruits[fruit_name]['harga']
                    print(f"Total harga untuk {quantity} {fruit_name}: {total_price}")
                    payment = int(input("Masukkan pembayaran Anda: "))
                    
                    if payment >= total_price:
                        fruits[fruit_name]['stock'] -= quantity
                        print(f"Pembelian berhasil. Kembalian: {payment - total_price}")
                        
                        # Add the purchase to the cart
                        cart.append({
                            'name': fruit_name,
                            'quantity': quantity,
                            'total_price': total_price
                        })
                    else:
                        print(f"Uang tidak cukup. Anda perlu {total_price - payment} lebih.")
                else:
                    print(f"Stok tidak cukup, stok {fruit_name} tinggal {fruits[fruit_name]['stock']}.")
                
                # Show the cart after every input attempt
                show_cart()  # Show cart after each input attempt
            else:
                print(f"{fruit_name} tidak tersedia.")
        except (IndexError, ValueError):
            print("Index tidak valid. Silakan coba lagi.")

        # Ask the user if they want to buy other fruits
        buy_more = input("Mau beli yang lain? (ya/tidak): ").strip().lower()
        if buy_more != 'ya':
            print("Terima kasih atas pembelian Anda!")
            break

# Main program loop
while True:
    menu_choice = get_menu_choice()

    if menu_choice == 1:
        show_fruits()
    elif menu_choice == 2:
        add_fruit()
    elif menu_choice == 3:
        remove_fruit()
    elif menu_choice == 4:
        buy_fruit()
    elif menu_choice == 5:
        print("Exiting program. Goodbye!")
        break


