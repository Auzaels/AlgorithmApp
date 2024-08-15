import random

rastgele_sayi = random.randint(1, 100)

tahmin_sayisi = 0

print("Sayı Tahmin Oyununa Hoşgeldiniz! (0-100 arası).")

while True:
    tahmin = int(input("Tahmininiz: "))
    tahmin_sayisi += 1

    if tahmin < rastgele_sayi:
        print("Daha büyük.")
    elif tahmin > rastgele_sayi:
        print("Daha küçük.")
    else:
        print(f"""Tebrikler! \nTahmin Sayısı: {tahmin_sayisi}""")
        break

print(f"Oyun bitti.")