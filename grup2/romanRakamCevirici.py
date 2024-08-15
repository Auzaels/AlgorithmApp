def decimal_to_roman(number):
    values = [1000, 500, 100, 50, 10, 5, 1]
    symbols = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    result = ''

    for i in range(len(values)):
        while number >= values[i]:
            result += symbols[i]
            number -= values[i]

    return result

sayi = int(input("Sayı gir"))

roma_rakami = decimal_to_roman(sayi)
print(f"{sayi} => {roma_rakami}")
