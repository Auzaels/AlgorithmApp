def eleman_tekrar_sayilari(dizi):
    eleman_sayilari = {}

    for eleman in dizi:
        if eleman in eleman_sayilari:
            eleman_sayilari[eleman] += 1
        else:
            eleman_sayilari[eleman] = 1

    print("Eleman Tekrar Sayıları:")
    for eleman, sayi in eleman_sayilari.items():
        print(f"{eleman}: x{sayi} kez")

dizi = input("Dizi gir (Boşluklu. ONR:1 2 3 4 5 6): ").split()

eleman_tekrar_sayilari(dizi)