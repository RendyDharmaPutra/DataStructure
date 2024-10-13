class PenghitungDzikir :
    def __init__(self) :
        self.hitungan = 0

    def tekan(self) :
        self.hitungan += 1

        if (self.hitungan % 33 == 0) :
            print(f"Anda telah berdzikir sebanyak {self.hitungan}")

    def reset(self) :
        self.hitungan = 0