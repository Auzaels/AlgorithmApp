"""
def faktoriyelAl(deger):
    sonuc = 1

    for i in range(deger, 0, -1):
        sonuc *= i

    print(f"{deger}! = {sonuc}")
"""

def faktoriyelAl(deger): #Gelişmiş Metod
    sonuc = 1
    faktoriyelAcilim = f"{deger}! = "

    for i in range(deger, 0, -1):
        sonuc *= i
        faktoriyelAcilim += str(i)
        if i != 1:
            faktoriyelAcilim += " x "

    print(faktoriyelAcilim)
    print(f"{deger}! = {sonuc}")

sayi = int(input("Sayı Girin: "))

faktoriyelAl(sayi)


