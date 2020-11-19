while True:
    try:
        angka = int(input("Masukkan Angka : "))
        a = 1
        b = 1
        while a <= angka:
            print (b)
            b += 1
            if b == 10:
                b -= 9
            a += 1
        break
    except ValueError:
        print("Coba Lagi")