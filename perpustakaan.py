from kitab import Kitab

class Perpustakaan:
    def __init__(self):
        self.daftar_kitab = [
            Kitab("Kitab Nahwu", 3),
            Kitab("Kitab Shorof", 2),
            Kitab("Kitab Injil", 1)
        ]

    def tampilkan_kitab(self):
        print("\n📚 DAFTAR KITAB")
        nomor = 1
        for kitab in self.daftar_kitab:
            print(
                str(nomor) + ". " +
                kitab.judul +
                " | Stok: " +
                str(kitab.get_stok()) +
                "/" +
                str(kitab.get_stok_maksimal())
            )
            nomor += 1

    def get_kitab(self, nomor):
        if nomor < 1 or nomor > len(self.daftar_kitab):
            return None
        return self.daftar_kitab[nomor - 1]

    def pinjam_kitab(self, nama, judul):
        for kitab in self.daftar_kitab:
            if kitab.judul == judul:
                if kitab.pinjam():
                    print("\n✅ PEMINJAMAN BERHASIL")
                    print("Nama  :", nama)
                    print("Kitab :", judul)
                else:
                    print("❌ Stok kitab habis")
                return
        print("❌ Kitab tidak ditemukan")

    def kembalikan_kitab(self, judul):
        for kitab in self.daftar_kitab:
            if kitab.judul == judul:
                if kitab.kembalikan():
                    print("✅ Kitab berhasil dikembalikan")
                else:
                    print("❌ Stok sudah penuh")
                return
        print("❌ Kitab tidak ditemukan")
