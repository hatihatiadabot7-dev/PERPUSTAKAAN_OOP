class Kitab:
    def __init__(self, judul, stok_maksimal):
        self.judul = judul
        self.__stok = stok_maksimal          # ENCAPSULATION
        self.__stok_maksimal = stok_maksimal

    def get_stok(self):
        return self.__stok

    def get_stok_maksimal(self):
        return self.__stok_maksimal

    def pinjam(self):
        if self.__stok <= 0:
            return False
        self.__stok -= 1
        return True

    def kembalikan(self):
        if self.__stok >= self.__stok_maksimal:
            return False
        self.__stok += 1
        return True
