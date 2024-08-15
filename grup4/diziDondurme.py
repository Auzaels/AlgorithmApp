def dizi_dondur(dizi, pozisyon):
    pozisyon = pozisyon % len(dizi)
    return dizi[pozisyon:] + dizi[:pozisyon]

dizi_str = input("Diziyi gir (Boşluklu): ")
dizi = dizi_str.split()
dizi = [int(x) for x in dizi]

pozisyon = int(input("Döndürme Sayısı: "))

sonuc = dizi_dondur(dizi, pozisyon)
print("Döndürülmüş Dizi:", sonuc)