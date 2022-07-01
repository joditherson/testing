def hitung_kecepatan():
    print("Ready!")
    jarak = float(input("Masukkan jarak: "))
    waktu = float(input("Masukkan waktu: "))
    kecepatan = jarak * waktu
    print("Kecepatan: ", kecepatan, "\n")

def luas_segitiga():
    print("Ready!")
    alas = float(input("Masukkan Alas: "))
    tinggi = float(input("Masukkan Tinggi: "))
    luas = 0.5 * (alas * tinggi)
    print("Luas Segitiga: ", luas, "\n")

def luas_balok():
    print("Ready!")
    panjang = float(input("Masukkan Panjang: "))
    lebar = float(input("Masukkan Lebar: "))
    tinggi = float(input("Masukkan Tinggi: "))
    luas = (2 * panjang * lebar) + (2 * panjang * tinggi) + (2 * lebar * tinggi)
    print("Luas Permukaan Balok: ", luas, "\n")

def luas_bola():
    print("Ready!")
    r = float(input("Masukkan Jari-Jari: "))
    luas = 4 * 3.14 * r**2
    print("Luas Permukaan Bola: ", luas, "\n")

while True:
    userInput = int(input("Pilih rumus yang mau dipakai: \n\nKeluar (0) \nKecepatan (1) \nLuas Segitiga (2) \nLuas Balok (3) \nLuas Bola (4)  \n\n"))

    if userInput == 1:
        hitung_kecepatan()
    elif userInput == 2:
        luas_segitiga()
    elif userInput == 3:
        luas_balok()
    elif userInput == 4:
        luas_bola()
    else:
        break