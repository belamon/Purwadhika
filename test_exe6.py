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
