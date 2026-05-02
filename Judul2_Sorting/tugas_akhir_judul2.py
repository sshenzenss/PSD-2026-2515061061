# PROGRAM MENGURUTKAN NILAI IPK MAHASISWA

def tukar(dataMahasiswa, i, j):
    temp = dataMahasiswa[i]
    dataMahasiswa[i] = dataMahasiswa[j]
    dataMahasiswa[j] = temp

def exchange_sort(dataMahasiswa, n):
    for i in range(n - 1):
        for j in range(i + 1, n):
            if dataMahasiswa[i][1] < dataMahasiswa[j][1]:
                tukar(dataMahasiswa, i, j)

def main():
    try:
        n = int(input("Masukkan jumlah mahasiswa: "))
    except ValueError:
        print("Input tidak valid, silakan masukkan angka!")
        return
    dataMahasiswa = []
    for i in range(n):
        while True:
            try:
                nama = input("Masukkan nama mahasiswa: ")
                ipk = float(input("Masukkan IPK mahasiswa (ex: 3.7): "))
                if ipk < 0 or ipk > 4:
                    print("IPK harus antara 0 dan 4!")
                    continue  
                dataMahasiswa.append((nama, ipk))
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")
                continue
    print(f"Data sebelum diurutkan menurut IPK: {dataMahasiswa}")
    exchange_sort(dataMahasiswa, n)
    print("Data setelah diurutkan dari IPK yang terbesar hingga terkecil (Exchange Sort):", end=" ")
    for i, (nama, ipk) in enumerate(dataMahasiswa):
        print(f"\n{i + 1}. {nama}: {ipk}", end=" ")

if __name__ == "__main__":
    main()
