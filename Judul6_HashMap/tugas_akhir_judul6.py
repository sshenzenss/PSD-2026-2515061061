class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2

class Entry:
    def __init__(self):
        self.key = None
        self.value = None
        self.state = SlotState.EMPTY

class HashMapOpenAddressing:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, key):
        return key % self.SIZE

    def insert(self, key, value):
        idx = self.hash_function(key)
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state != SlotState.OCCUPIED:
                self.table[i].key = key
                self.table[i].value = value
                self.table[i].state = SlotState.OCCUPIED
                return True
            if self.table[i].key == key:
                self.table[i].value = value
                return True
        return False

    def search(self, key):
        idx = self.hash_function(key)
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.EMPTY:
                return None
            if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == key:
                return self.table[i]
        return None

    def remove_key(self, key):
        data = self.search(key)
        if data is None:
            return False
        data.state = SlotState.DELETED
        return True

    def display(self):
        print("\nData Minuman:")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            if self.table[i].state == SlotState.EMPTY:
                print("EMPTY")
            elif self.table[i].state == SlotState.DELETED:
                print("DELETED")
            else:
                print(f"({self.table[i].key}, {self.table[i].value})")

def main():
    hashmap = HashMapOpenAddressing()
    while True:
        print("\n=== STOK MINUMAN ===")
        print("1. Tambah Minuman")
        print("2. Cari Minuman")
        print("3. Hapus Minuman")
        print("4. Tampilkan Semua Minuman")
        print("5. Keluar")
        pilih = input("Pilih menu: ")
        if pilih == "1":
            kode = int(input("Kode Minuman: "))
            nama = input("Nama Minuman: ")
            if hashmap.insert(kode, nama):
                print("Minuman berhasil ditambahkan")
            else:
                print("Hash Table penuh")
        elif pilih == "2":
            kode = int(input("Masukkan kode minuman: "))
            hasil = hashmap.search(kode)
            if hasil:
                print(f"Minuman ditemukan: {hasil.value}")
            else:
                print("Minuman tidak ditemukan")
        elif pilih == "3":
            kode = int(input("Masukkan kode minuman: "))
            if hashmap.remove_key(kode):
                print("Minuman berhasil dihapus")
            else:
                print("Minuman tidak ditemukan")
        elif pilih == "4":
            hashmap.display()
        elif pilih == "5":
            print("Program selesai")
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
