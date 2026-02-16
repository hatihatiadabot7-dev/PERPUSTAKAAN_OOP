from santri import Santri
from perpustakaan import Perpustakaan

def main():
    perpustakaan = Perpustakaan()

    print("=== SISTEM PERPUSTAKAAN KITAB ===")
    nama = input("Masukkan nama santri: ")
    santri = Santri(nama)

    while True:
        print("\nMENU:")
        print("1. Pinjam Kitab")
        print("2. Kembalikan Kitab")
        print("3. Keluar")

        perpustakaan.tampilkan_kitab()
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            try:
                nomor = int(input("Pilih nomor kitab: "))
            except:
                print("❌ Harus angka")
                continue

            kitab = perpustakaan.get_kitab(nomor)
            if kitab is None:
                print("❌ Nomor tidak valid")
                continue

            santri.pinjam_kitab(perpustakaan, kitab.judul)

        elif pilihan == "2":
            try:
                nomor = int(input("Pilih nomor kitab: "))
            except:
                print("❌ Harus angka")
                continue

            kitab = perpustakaan.get_kitab(nomor)
            if kitab is None:
                print("❌ Nomor tidak valid")
                continue

            santri.kembalikan_kitab(perpustakaan, kitab.judul)

        elif pilihan == "3":
            print("👋 Program selesai")
            break

        else:
            print("❌ Menu tidak valid")

main()
