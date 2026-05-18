# PROGRAM ANTRIAN NASABAH BANK

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front_ptr = None
        self.rear_ptr = None
        self.next_no = 1

    def is_empty(self):
        return self.front_ptr is None

    def enqueue(self, x):
        new_node = Node(x)
        if self.is_empty():
            self.front_ptr = new_node
            self.rear_ptr = new_node
        else:
            self.rear_ptr.next = new_node
            self.rear_ptr = new_node
        no_antrian, nama = x
        print(f"Berhasil menambahkan antrian ke-{no_antrian}: {nama}")

    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong")
            return
        temp = self.front_ptr
        no_antrian, nama = temp.data
        print(f"Antrian ke-{no_antrian}: {nama} berhasil dipanggil")
        self.front_ptr = self.front_ptr.next
        if self.front_ptr is None:
            self.rear_ptr = None

    def peek(self):
        if self.is_empty():
            print("Antrian kosong")
            return
        no_antrian, nama = self.front_ptr.data
        print(f"Antrian paling depan: {no_antrian}. {nama}")

    def display(self):
        if self.is_empty():
            print("Antrian kosong")
            return
        print("Urutan Antrian: ", end="")
        current = self.front_ptr
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

def main():
    queue = QueueLinkedList()
    pilih = 0
    while pilih != 5:
        print("\n=== ANTRIAN NASABAH BANK ===")
        print("1. Tambahkan ke Antrian")
        print("2. Panggil dari Antrian")
        print("3. Lihat Antrian Paling Depan")
        print("4. Tampilkan Antrian")
        print("5. Kosongkan Antrian dan Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            nama = input("Nama: ")
            no_antrian = queue.next_no
            queue.next_no += 1
            queue.enqueue((no_antrian, nama))
        elif pilih == 2:
            queue.dequeue()
        elif pilih == 3:
            queue.peek()
        elif pilih == 4:
            queue.display()
        elif pilih == 5:
            while not queue.is_empty():
                queue.dequeue()
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
