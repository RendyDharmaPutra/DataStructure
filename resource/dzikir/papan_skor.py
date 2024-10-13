# class PapanSkor :
#     def __init__(self, tim1, tim2):
#         self.tim1 = tim1
#         self.tim2 = tim2
#         self._skor1 = 0
#         self._skor2 = 0
#
#     def up1(self):
#         self._skor1 += 1
#
#     def up2(self):
#         self._skor2 += 1
#
#     def down1(self):
#         self._skor1 -= 1
#
#     def down2(self):
#         self._skor2 -= 1
#
#     def peek1(self):
#         return self._skor1
#
#     def peek2(self):
#         return self._skor2
#
#     def reset(self):
#         self._skor1 = 0
#         self._skor2 = 0

class PapanSkor :
    def __init__(self, tim1, tim2):
        self._tim1 = {
            "nama": tim1,
            "skor": 0
        }

        self._tim2 = {
            "nama": tim2,
            "skor": 0
        }

    def up1(self):
        self._tim1["skor"] += 1

    def up2(self):
        self._tim2["skor"] += 1

    def down1(self):
        self._tim1["skor"] -= 1

    def down2(self):
        self._tim2["skor"] -= 1

    def peek1(self):
        return self._tim1["skor"]

    def peek2(self):
        return self._tim2["skor"]

    def reset(self):
        self._tim1["skor"] = 0
        self._tim2["skor"] = 0