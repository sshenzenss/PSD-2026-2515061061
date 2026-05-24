class Node:
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None 


class BSTDasar:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key: 
            root.left = self.insert_node(root.left, key)
        elif key > root.key:
            root.right = self.insert_node(root.right, key)
        return root

    def insert(self, key):
        self.root = self.insert_node(self.root, key)

    def search_node(self, root, key):
        if root is None:
            return False 
        if root.key == key:
            return True
        if key < root.key:
            return self.search_node(root.left, key)
        return self.search_node(root.right, key)

    def search(self, key):
        return self.search_node(self.root, key)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.key, end=" ")
        self.inorder(root.right)

    def find_min(self, root):
        if root is None:
            return -1
        current = root
        while current.left is not None:
            current = current.left
        return current.key

    def find_max(self, root):
        if root is None:
            return -1
        current = root
        while current.right is not None:
            current = current.right
        return current.key

    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

def main():
    bst = BSTDasar()
    pilih = 0
    while pilih != 7:
        print("\n=== DATA UMUR PASIEN KLINIK ===")
        print("1. Masukkan umur pasien")
        print("2. Cari umur pasien")
        print("3. Urutkan umur pasien dari termuda ke tertua")
        print("4. Tampilkan umur pasien termuda")
        print("5. Tampilkan umur pasien tertua")
        print("6. Hitung jumlah pasien")
        print("7. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            try:
                x = int(input("Masukkan umur pasien: "))
                bst.insert(x)
                print(f"Data berhasil dimasukkan")
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 2:
            try:
                x = int(input("Cari pasien dengan umur: "))
                if bst.search(x):
                    print("Pasien ditemukan")
                else:
                    print("Pasien tidak ditemukan")
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 3:
            print("Urutan umur pasien dari termuda ke tertua: ", end="")
            bst.inorder(bst.root)
            print()
        elif pilih == 4:
            print(f"Umur pasien termuda adalah: {bst.find_min(bst.root)}")
        elif pilih == 5:
            print(f"Umur pasien tertua adalah: {bst.find_max(bst.root)}")
        elif pilih == 6:
            print(f"Jumlah data pasien: {bst.count_nodes(bst.root)}")    
        elif pilih == 7:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
