yaricap = int(input("Dairenin yarıçapını gir: "))
pi = int(input("Pi sayısını gir:"))

# Alan ve çevreyi hesapla
alan = pi * (yaricap ** 2)
cevre = 2 * pi * yaricap

# Sonuçları yazdır
print(f"Dairenin Alanı: {alan}")
print(f"Dairenin Çevresi: {cevre}")