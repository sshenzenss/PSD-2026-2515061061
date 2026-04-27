# PROGRAM MANAJEMEN STOK MAKANAN

def menu():
    print("1. Masukkan nama dan stok makanan")
    print("2. Tampilkan stok makanan")
    print("3. Edit nama dan stok makanan")
    print("4. Keluar")

def main():
    makanan = []
    running = True
    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid.")
            continue
        if choice == 1:
            nama = input("Nama makanan: ")
            while True:
                try:
                    stok = int(input("Stok makanan: "))
                    break
                except ValueError:
                    print("Input tidak valid, silakan masukkan angka!")
            makanan.append((nama, stok))
        elif choice == 2:
            if not makanan:
                print("Belum ada data makanan, silakan input terlebih dahulu.")
            else:
                print("Menampilkan Stok Makanan:")
                print("-------------------------")
                for i, (nama, stok) in enumerate(makanan):
                    print(f"{i + 1}. {nama}: {stok}")
                print("-------------------------")
        elif choice == 3:
            if not makanan:
                print("Belum ada data makanan, silakan input terlebih dahulu")
            else:
                try:
                    index = int(input("Masukkan nomor makanan yang ingin diedit: ")) - 1
                    if 0 <= index < len(makanan):
                        nama_baru = input("Nama baru: ")
                        while True:
                            try:
                                stok_baru = int(input("Stok baru: "))
                                break
                            except ValueError:
                                print("Input tidak valid, silakan masukkan angka!")
                        makanan[index] = (nama_baru, stok_baru)
                    else:
                        print("Nomor makanan tidak valid.")
                except ValueError:
                    print("Input tidak valid, silakan masukkan angka!")
        elif choice == 4:
            running = False
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
