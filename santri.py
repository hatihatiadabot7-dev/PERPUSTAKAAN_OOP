from user import User

class Santri(User):
    def __init__(self, nama):
        super().__init__(nama)

    def pinjam_kitab(self, perpustakaan, judul):
        perpustakaan.pinjam_kitab(self.nama, judul)

    def kembalikan_kitab(self, perpustakaan, judul):
        perpustakaan.kembalikan_kitab(judul)
