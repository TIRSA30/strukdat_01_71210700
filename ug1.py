print("Ketik Q jika sudah selesai.")
print("PILIH MENU")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

while True:
    pilihan = input("Masukkan Piliahan Anda: ")
    if pilihan == "Q":
        break

    a = int(input("Bilangan Pertama : "))
    b = int(input("Bilangan Kedua : "))


    if pilihan == "1":
        tambah = a+b
        print(a+b)

    elif pilihan == "2":
        kurang = a-b
        print(a-b)

    elif pilihan == "3":
        kali = a*b
        print(a*b)

    elif pilihan == "4":
        bagi = a/b
        print(a/b)

