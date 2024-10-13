from resource.dzikir import papan_skor


def script() :
    # penghitung1 = dzikir.PenghitungDzikir()
    #
    # for i in range(99) :
    #     penghitung1.tekan()
    #     print(penghitung1.hitungan)
    #
    # penghitung1.reset()

    papanSkor = papan_skor.PapanSkor(tim1="Garuda", tim2="Elang")

    papanSkor.up1()
    papanSkor.up1()
    papanSkor.up2()

    print(papanSkor.peek1())
    print(papanSkor.peek2())