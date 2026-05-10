# PROGRAM PENGECEKAN KAMAR PENGINAPAN

def sequential_search(data, n, target):
    i = 0
    while i < n:
        if data[i] == target:
            print("Kamar tersedia")
            print(f"Kamar {target} berada pada indeks ke-{data.index(target)} dalam data kamar.")
        i += 1
    if target not in data:
        print("Kamar tidak tersedia, silakan pilih kamar lain")
        main()

def main():
    data = [105, 110, 201, 207, 301, 109, 206, 108, 209, 304]
    n = len(data)
    print(f"Data Kamar: {data}")
    while True:
        try:
            target = int(input("Masukkan nomor kamar yang diinginkan: "))
            break
        except ValueError:
            print("Input tidak valid, silakan masukkan angka!")
    sequential_search(data, n, target)

if __name__ == "__main__":
    main()
