
metin = input("Lütfen bir metin giriniz: ")
def kelime_sayaci(metin):
    kelimeler = metin.split()
    sayi = len(kelimeler)
    return sayi

print(f"Kelime sayısı: {kelime_sayaci(metin)}")

