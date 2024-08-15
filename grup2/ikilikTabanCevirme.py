def onlugu_ikiliye_cevir(sayi):
  ikilik_sayi = bin(sayi)[2:]
  return ikilik_sayi

sayi = int(input("Bir sayı gir: "))
sonuc = onlugu_ikiliye_cevir(sayi)
print(f"{sayi}'nın ikiliği:", sonuc)