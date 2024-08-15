def asalKontrol(deger):
    if deger < 2:
        return False
    for i in range(2, int(deger**0.5) + 1):
        if deger % i == 0:
            return False
    return True

sayi = int(input("Sayı Girin: "))

if asalKontrol(sayi):
    print(f"{sayi} asal.")
else:
    print(f"{sayi} asal değil.")