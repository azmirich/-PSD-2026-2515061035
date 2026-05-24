#BSTDASARKAMARKOS
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

    def preorder(self, root):
        if root is None:
            return
        print(root.key, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.key, end=" ")

    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)


def main():
    bst = BSTDasar()
    pilih = 0
    while pilih != 7:
        print("\nManajemen Kamar Kosan")
        print("1. Masukkan Kamar Kos yang Tersedia")
        print("2. Cek Ketersediaan Kamar")
        print("3. Daftar Kamar (Inorder)")
        print("4. Daftar Kamar (Preorder)")
        print("5. Daftar Kamar (Postorder)")
        print("6. Total Jumlah Kamar di Kosan")
        print("7. Keluar")
        
        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid! Masukkan angka.")
            continue
            
        if pilih == 1:
            try:
                x = int(input("Masukkan Nomor Kamar yang Tersedia: "))
                bst.insert(x)
                print(f"Kamar nomor {x} berhasil didaftarkan ke sistem!")
            except ValueError:
                print("Input tidak valid! Masukkan angka.")
                
        elif pilih == 2:
            try:
                x = int(input("Cari Nomor Kamar: "))
                if bst.search(x):
                    print(f"Kamar No {x} Tersedia.")
                else:
                    print(f"Kamar No {x} Tidak Tersedia.")
            except ValueError:
                print("Input tidak valid!")
                
        elif pilih == 3:
            print("Daftar Kamar (Inorder): ", end="")
            bst.inorder(bst.root)
            print()
            
        elif pilih == 4:
            print("Daftar Kamar (Preorder): ", end="")
            bst.preorder(bst.root)
            print()
            
        elif pilih == 5:
            print("Daftar Kamar (Postorder): ", end="")
            bst.postorder(bst.root)
            print()
                
        elif pilih == 6:
            print(f"Total ada {bst.count_nodes(bst.root)} kamar di kosan ini.")
            
        elif pilih == 7:
            print("Sistem Selesai")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()