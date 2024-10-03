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

