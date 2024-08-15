from tkinter import *
from tkinter import messagebox
import random

def screen_avg(win, width, height):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    win.geometry(f"{width}x{height}+{x}+{y}")
def open_finding_prime_numbers_page():
    global current_x, current_y
    current_x, current_y = algorithm_app.winfo_x(), algorithm_app.winfo_y()
    algorithm_app.destroy()

    def is_this_number_prime():
        number = int(finding_prime_entry.get())

        if number < 2:
            messagebox.showinfo("Asal Değil", "Asal değildir. Bunun nedeni 2 sayısından küçük olmasıyla veya negatif sayı olmasıyla alakalı olabilir. (En küçük asal sayı 2'dir.)")
            return

        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                messagebox.showinfo("Asal Değil", "Asal değildir. Çünkü 1 ve kendisi haricinde başka sayılara bölünebilir.")
                return

        messagebox.showinfo("Asaldır", "Asaldır. Çünkü 1 ve kendisi haricinde başka bir sayıya bölünmez.")

    finding_prime_numbers_window = Tk()
    finding_prime_numbers_window.title("Algorithm - Finding Prime Numbers")
    finding_prime_numbers_window.geometry(f"325x250+{current_x}+{current_y}")
    finding_prime_numbers_window.resizable(False,False)

    tittle_label = Label(finding_prime_numbers_window, text="Asal Sayı Bulma", font=("Arial", 20))
    tittle_label.pack(pady=20)

    finding_prime_tittle_label = Label(finding_prime_numbers_window, text="Sayı Gir:", font=("Arial", 10))
    finding_prime_tittle_label.place(x=97, y=83)

    finding_prime_entry = Entry(finding_prime_numbers_window, width=20)
    finding_prime_entry.pack(pady=(25,0))

    finding_prime_button = Button(finding_prime_numbers_window, text="Çalıştır", command=is_this_number_prime)
    finding_prime_button.pack(pady=(5,10))

    back_button = Button(finding_prime_numbers_window, text="Ana Menüye Dön", command=lambda: reopen_main_page(finding_prime_numbers_window))
    back_button.pack(pady=20)

    finding_prime_numbers_window.mainloop()
def number_guessing_page():
    global current_x, current_y
    current_x, current_y = algorithm_app.winfo_x(), algorithm_app.winfo_y()
    algorithm_app.destroy()

    random_number = random.randint(1, 100)
    remaining_attempts = 5

    def update_attempts_label():
        attempts_label.config(text=f"Kalan Hak: {remaining_attempts}")

    def is_this_number_correct():
        nonlocal remaining_attempts
        try:
            user_number = int(number_guessing_entry.get())
            remaining_attempts -= 1
            update_attempts_label()

            if user_number < 1 or user_number > 100:
                messagebox.showwarning("Uyarı", "Lütfen 1 ile 100 arasında bir sayı girin.")
                remaining_attempts += 1  # Geçersiz tahmin için hak eksiltmiyoruz
                update_attempts_label()
            elif user_number < random_number:
                messagebox.showinfo("Sonuç", "Daha yüksek bir sayı deneyin.")
            elif user_number > random_number:
                messagebox.showinfo("Sonuç", "Daha düşük bir sayı deneyin.")
            else:
                messagebox.showinfo("Tebrikler!", f"Doğru tahmin! Sayı: {random_number}\nKullanılan hak: {5 - remaining_attempts}")
                reopen_main_page(number_guessing_window)
                return

            if remaining_attempts == 0:
                messagebox.showinfo("Oyun Bitti", f"Haklarınız bitti. Doğru sayı {random_number} idi.")
                reopen_main_page(number_guessing_window)

        except ValueError:
            messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin.")

    number_guessing_window = Tk()
    number_guessing_window.title("Algorithm - Number Guessing Game")
    number_guessing_window.geometry(f"325x250+{current_x}+{current_y}")
    number_guessing_window.resizable(False,False)

    tittle_label = Label(number_guessing_window, text="Sayı Tahmin Oyunu", font=("Arial", 20))
    tittle_label.pack(pady=20)

    number_guessing_tittle_label = Label(number_guessing_window, text="Sayı Gir (1-100):", font=("Arial", 10))
    number_guessing_tittle_label.place(x=97, y=83)

    number_guessing_entry = Entry(number_guessing_window, width=20)
    number_guessing_entry.pack(pady=(25,0))

    number_guessing_button = Button(number_guessing_window, text="Tahmin Et", command=is_this_number_correct)
    number_guessing_button.pack(pady=(5,10))

    attempts_label = Label(number_guessing_window, text=f"Kalan Hak: {remaining_attempts}", font=("Arial", 10))
    attempts_label.pack(pady=(5,0))

    back_button = Button(number_guessing_window, text="Ana Menüye Dön", command=lambda: reopen_main_page(number_guessing_window))
    back_button.pack(pady=10)

    number_guessing_window.mainloop()
def roman_numeral_converter_page():
    global current_x, current_y
    current_x, current_y = algorithm_app.winfo_x(), algorithm_app.winfo_y()
    algorithm_app.destroy()

    def decimal_to_roman(number):
        values = [1000, 500, 100, 50, 10, 5, 1]
        symbols = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        result = ''

        for i in range(len(values)):
            while number >= values[i]:
                result += symbols[i]
                number -= values[i]

        result = result.replace('DCCCC', 'CM').replace('CCCC', 'CD')
        result = result.replace('LXXXX', 'XC').replace('XXXX', 'XL')
        result = result.replace('VIIII', 'IX').replace('IIII', 'IV')

        return result

    def roman_to_decimal(roman):
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        decimal = 0
        previous_value = 0

        for char in reversed(roman):
            value = roman_values[char]
            if value < previous_value:
                decimal -= value
            else:
                decimal += value
            previous_value = value

        return decimal

    def convert_to_roman():
        user_input = number_to_roman_input_entry.get()
        if not user_input.isdigit():
            messagebox.showerror("Hata!", "Lütfen geçerli bir sayı giriniz.")
            return

        try:
            number = int(user_input)
            if 1 <= number <= 3999:
                roman_numeral = decimal_to_roman(number)
                number_to_roman_result_label.config(text=f"{roman_numeral}")
            else:
                messagebox.showerror("Hata!", "Lütfen 1 ile 3999 arasında bir sayı girin.")
        except ValueError:
            messagebox.showerror("Hata!", "Lütfen geçerli bir sayı giriniz.")

    def convert_to_number():
        roman_input = roman_to_number_input_entry.get().upper()
        try:
            decimal_number = roman_to_decimal(roman_input)
            roman_to_number_result_label.config(text=f"{decimal_number}")
        except KeyError:
            messagebox.showerror("Hata!", "Lütfen geçerli bir Roma rakamı giriniz.")

    roman_numeral_converter_window = Tk()
    roman_numeral_converter_window.title("Algorithm - Roman Numeral Converter")
    roman_numeral_converter_window.geometry(f"400x230+{current_x}+{current_y}")

    label = Label(roman_numeral_converter_window, text="Roman Rakamı Çevirici", font=("Arial", 20))
    label.pack(pady=(10,5))

    #### Sayı => Roman
    number_to_roman_out_frame = Frame(roman_numeral_converter_window, width=185, height=130, bg="black")
    number_to_roman_out_frame.place(x=10, y=90)

    number_to_roman_in_frame = Frame(number_to_roman_out_frame, width=175, height=120)
    number_to_roman_in_frame.pack(padx=5, pady=5)

    number_to_roman_tittle_label = Label(number_to_roman_in_frame, text="Sayıdan Roman Rakamına", font=("Arial", 10))
    number_to_roman_tittle_label.place(x=5, y=5)

    number_to_roman_input_entry = Entry(number_to_roman_in_frame, width=8, font=("Arial",10))
    number_to_roman_input_entry.place(x=10, y=50)

    number_to_roman_arrow_label = Label(number_to_roman_in_frame, text="=>", font=("Arial", 10))
    number_to_roman_arrow_label.place(x=80, y=50)

    number_to_roman_result_label = Label(number_to_roman_in_frame, text="Cevap", font=("Arial", 10))
    number_to_roman_result_label.place(x=110, y=50)

    number_to_roman_convert_button = Button(number_to_roman_in_frame, text="Roman'a Çevir", command=convert_to_roman, font=("Arial", 10))
    number_to_roman_convert_button.place(x=40, y=80)

    #### Roman => Sayı
    roman_to_number_out_frame = Frame(roman_numeral_converter_window, width=185, height=130, bg="black")
    roman_to_number_out_frame.place(x=205, y=90)

    roman_to_number_in_frame = Frame(roman_to_number_out_frame, width=175, height=120)
    roman_to_number_in_frame.pack(padx=5, pady=5)

    roman_to_number_tittle_label = Label(roman_to_number_in_frame, text="Roman Rakamından Sayıya", font=("Arial", 10))
    roman_to_number_tittle_label.place(x=1, y=5)

    roman_to_number_input_entry = Entry(roman_to_number_in_frame, width=8, font=("Arial",10))
    roman_to_number_input_entry.place(x=10, y=50)

    roman_to_number_arrow_label = Label(roman_to_number_in_frame, text="=>", font=("Arial", 10))
    roman_to_number_arrow_label.place(x=80, y=50)

    roman_to_number_result_label = Label(roman_to_number_in_frame, text="Cevap", font=("Arial", 10))
    roman_to_number_result_label.place(x=110, y=50)

    roman_to_number_convert_button = Button(roman_to_number_in_frame, text="Sayıya Çevir", command=convert_to_number, font=("Arial", 10))
    roman_to_number_convert_button.place(x=45, y=80)

    back_button = Button(roman_numeral_converter_window, text="Ana Menüye Dön", command=lambda: reopen_main_page(roman_numeral_converter_window))
    back_button.pack(pady=5)

    roman_numeral_converter_window.mainloop()
def binary_base_converter_page():
    global current_x, current_y
    current_x, current_y = algorithm_app.winfo_x(), algorithm_app.winfo_y()
    algorithm_app.destroy()

    binary_base_converter_window = Tk()
    binary_base_converter_window.title("Algorithm - Binary Base Converter")
    binary_base_converter_window.geometry(f"400x230+{current_x}+{current_y}")

    label = Label(binary_base_converter_window, text="İkilik Taban Çevirici", font=("Arial", 20))
    label.pack(pady=(10,5))

    def decimal_to_binary():
        user_input_for_number_to_binary = int(number_to_binary_input_entry.get())
        binary_number = bin(user_input_for_number_to_binary)[2:]
        number_to_binary_result_label.config(text=f"{binary_number}")

    #### Sayıdan => İkiliğe
    number_to_binary_out_frame = Frame(binary_base_converter_window, width=185, height=130, bg="black")
    number_to_binary_out_frame.place(x=10, y=90)

    number_to_binary_in_frame = Frame(number_to_binary_out_frame, width=175, height=120)
    number_to_binary_in_frame.pack(padx=5, pady=5)

    number_to_binary_tittle_label = Label(number_to_binary_in_frame, text="Sayıdan İkilik Tabana", font=("Arial", 10))
    number_to_binary_tittle_label.place(x=20, y=5)

    number_to_binary_input_entry = Entry(number_to_binary_in_frame, width=8, font=("Arial",10))
    number_to_binary_input_entry.place(x=10, y=50)

    number_to_binary_arrow_label = Label(number_to_binary_in_frame, text="=>", font=("Arial", 10))
    number_to_binary_arrow_label.place(x=80, y=50)

    number_to_binary_result_label = Label(number_to_binary_in_frame, text="Cevap", font=("Arial", 10))
    number_to_binary_result_label.place(x=110, y=50)

    number_to_binary_convert_button = Button(number_to_binary_in_frame, text="İkiliğe Çevir", command=decimal_to_binary, font=("Arial", 10))
    number_to_binary_convert_button.place(x=45, y=80)

    def binary_to_decimal():
        user_input_for_binary_to_decimal = binary_to_number_input_entry.get()
        try:
            decimal_number = int(user_input_for_binary_to_decimal, 2)
            binary_to_number_result_label.config(text=f"{decimal_number}")
        except ValueError:
            messagebox.showerror("Hata!", "Geçersiz ikilik sayı girdiniz.")

    #### İkilikten => Sayıya
    binary_to_number_out_frame = Frame(binary_base_converter_window, width=185, height=130, bg="black")
    binary_to_number_out_frame.place(x=205, y=90)

    binary_to_number_in_frame = Frame(binary_to_number_out_frame, width=175, height=120)
    binary_to_number_in_frame.pack(padx=5, pady=5)

    binary_to_number_tittle_label = Label(binary_to_number_in_frame, text="İkilik Tabandan Sayıya", font=("Arial", 10))
    binary_to_number_tittle_label.place(x=20, y=5)

    binary_to_number_input_entry = Entry(binary_to_number_in_frame, width=8, font=("Arial",10))
    binary_to_number_input_entry.place(x=10, y=50)

    binary_to_number_arrow_label = Label(binary_to_number_in_frame, text="=>", font=("Arial", 10))
    binary_to_number_arrow_label.place(x=80, y=50)

    binary_to_number_result_label = Label(binary_to_number_in_frame, text="Cevap", font=("Arial", 10))
    binary_to_number_result_label.place(x=110, y=50)

    binary_to_number_convert_button = Button(binary_to_number_in_frame, text="Sayıya Çevir", command=binary_to_decimal, font=("Arial", 10))
    binary_to_number_convert_button.place(x=45, y=80)

    back_button = Button(binary_base_converter_window, text="Ana Menüye Dön", command=lambda: reopen_main_page(binary_base_converter_window))
    back_button.pack(pady=5)

    binary_base_converter_window.mainloop()
def square_and_cube_calculation_page():
    global current_x, current_y
    current_x, current_y = algorithm_app.winfo_x(), algorithm_app.winfo_y()
    algorithm_app.destroy()

    square_and_cube_calculation_window = Tk()
    square_and_cube_calculation_window.title("Algorithm - Square And Cube Calculation")
    square_and_cube_calculation_window.geometry(f"400x225+{current_x}+{current_y}")
    square_and_cube_calculation_window.resizable(False,False)

    def square_and_cube_calculate():
        user_value_for_square_and_cube_calculate = int(square_and_cube_entry.get())
        square_value = user_value_for_square_and_cube_calculate ** 2
        cube_value = user_value_for_square_and_cube_calculate ** 3

        square_of_number_label.config(text=f"Karesi: {square_value}")
        cube_of_number_label.config(text=f"Küpü: {cube_value}")

    label = Label(square_and_cube_calculation_window, text="Kare ve Küp Hesaplama", font=("Arial", 20))
    label.pack(pady=20)

    square_and_cube_entry = Entry(square_and_cube_calculation_window, width=10, font=("Arial", 10))
    square_and_cube_entry.place(x=85, y=85)

    square_and_cube_calculate_button = Button(square_and_cube_calculation_window, text="Hesapla", command=square_and_cube_calculate)
    square_and_cube_calculate_button.place(x=85, y=115)

    square_of_number_label = Label(square_and_cube_calculation_window, text="Karesi: ", font=("Arial", 10))
    square_of_number_label.place(x=225, y=85)

    cube_of_number_label = Label(square_and_cube_calculation_window, text="Küpü: ", font=("Arial", 10))
    cube_of_number_label.place(x=225, y=115)


    back_button = Button(square_and_cube_calculation_window, text="Ana Menüye Dön", command=lambda: reopen_main_page(square_and_cube_calculation_window))
    back_button.place(x=150, y=175)

    square_and_cube_calculation_window.mainloop()
def area_and_premeter_of_the_circle_calculation_page():
    global current_x, current_y
    current_x, current_y = algorithm_app.winfo_x(), algorithm_app.winfo_y()
    algorithm_app.destroy()

    area_and_premeter_of_the_circle_calculation_window = Tk()
    area_and_premeter_of_the_circle_calculation_window.title("Algorithm - Square And Cube Calculation")
    area_and_premeter_of_the_circle_calculation_window.geometry(f"400x225+{current_x}+{current_y}")
    area_and_premeter_of_the_circle_calculation_window.resizable(False,False)

    def area_and_premeter_calculate():
        user_radius_value_for_area_and_premeter_calculate = int(input_radius_entry.get())
        user_pi_number_value_for_area_and_premeter_calculate = int(input_pi_number_entry.get())

        premeter_value = 2 * user_pi_number_value_for_area_and_premeter_calculate * user_radius_value_for_area_and_premeter_calculate
        area_value = user_pi_number_value_for_area_and_premeter_calculate * (user_radius_value_for_area_and_premeter_calculate ** 2)

        area_label.config(text=f"Alanı: {area_value}")
        premeter_label.config(text=f"Çevresi: {premeter_value}")

    label = Label(area_and_premeter_of_the_circle_calculation_window, text="Kare ve Küp Hesaplama", font=("Arial", 20))
    label.pack(pady=20)

    radius_label = Label(area_and_premeter_of_the_circle_calculation_window, text="Yarıçapı:", font=("Arial", 8))
    radius_label.place(x=35, y=85)

    input_radius_entry = Entry(area_and_premeter_of_the_circle_calculation_window, width=10, font=("Arial", 10))
    input_radius_entry.place(x=85, y=85)

    pi_number_label = Label(area_and_premeter_of_the_circle_calculation_window, text="Pi Sayısı:", font=("Arial", 8))
    pi_number_label.place(x=34, y=115)

    input_pi_number_entry = Entry(area_and_premeter_of_the_circle_calculation_window, width=10, font=("Arial", 10))
    input_pi_number_entry.place(x=85, y=115)

    area_and_premeter_calculate_button = Button(area_and_premeter_of_the_circle_calculation_window, text="Hesapla", command=area_and_premeter_calculate)
    area_and_premeter_calculate_button.place(x=75, y=150)

    premeter_label = Label(area_and_premeter_of_the_circle_calculation_window, text="Alanı: ", font=("Arial", 10))
    premeter_label.place(x=225, y=85)

    area_label = Label(area_and_premeter_of_the_circle_calculation_window, text="Çevresi: ", font=("Arial", 10))
    area_label.place(x=225, y=115)


    back_button = Button(area_and_premeter_of_the_circle_calculation_window, text="Ana Menüye Dön", command=lambda: reopen_main_page(area_and_premeter_of_the_circle_calculation_window))
    back_button.place(x=200, y=150)

    area_and_premeter_of_the_circle_calculation_window.mainloop()
def array_rotation_page():
    global current_x, current_y
    current_x, current_y = algorithm_app.winfo_x(), algorithm_app.winfo_y()
    algorithm_app.destroy()

    array_rotation_window = Tk()
    array_rotation_window.title("Algorthm - Array Rotation")
    array_rotation_window.geometry(f"325x300+{current_x}+{current_y}")
    array_rotation_window.resizable(False,False)

    label = Label(array_rotation_window, text="Dizi Döndürme", font=("Arial", 20))
    label.pack(pady=20)

    def rotate_array():
        try:
            user_array = input_array_list_entry.get()
            rotate_number = int(input_rotate_number_entry.get())

            array = list(map(int, user_array.split()))

            rotate = len(array)
            rotated_array = array[rotate_number:] + array[:rotate_number]

            rotated_array_label.config(text=f"Döndürülmüş dizi: {rotated_array}")
        except ValueError:
            messagebox.showerror("Hata!","Lütfen geçerli bir dizi veya döndürme sayısı giriniz.")



    array_list_label = Label(array_rotation_window, text="Diziyi Gir (Örn: 1 2 3 4 5):")
    array_list_label.pack()

    input_array_list_entry = Entry(array_rotation_window, width=25)
    input_array_list_entry.pack()

    rotate_number_label = Label(array_rotation_window, text="Döndürme Sayısı Gir:")
    rotate_number_label.pack()

    input_rotate_number_entry = Entry(array_rotation_window, width=10)
    input_rotate_number_entry.pack()

    rotate_button = Button(array_rotation_window, text="Döndür", command=rotate_array)
    rotate_button.pack(pady=10)

    rotated_array_label = Label(array_rotation_window, text="Dönmüş Dizi: ")
    rotated_array_label.pack()

    back_button = Button(array_rotation_window, text="Ana Menüye Dön", command=lambda: reopen_main_page(array_rotation_window))
    back_button.pack(pady=20)

    array_rotation_window.mainloop()
def repeating_elements_in_the_array_page():
    global current_x, current_y
    current_x, current_y = algorithm_app.winfo_x(), algorithm_app.winfo_y()
    algorithm_app.destroy()

    repeating_elements_in_the_array_window = Tk()
    repeating_elements_in_the_array_window.title("Algorthm - Repeating Elements")
    repeating_elements_in_the_array_window.geometry(f"325x300+{current_x}+{current_y}")
    repeating_elements_in_the_array_window.resizable(False,False)

    label = Label(repeating_elements_in_the_array_window, text="Dizide Tekrar Edenler", font=("Arial", 20))
    label.pack(pady=(20,5))

    back_button = Button(repeating_elements_in_the_array_window, text="Ana Menüye Dön", command=lambda: reopen_main_page(repeating_elements_in_the_array_window))
    back_button.pack(pady=(5,15))

    def repeating_elements():
        repeating_elements_in_the_array_result_listbox.delete(0, END)

        repeating_elements_array = repeating_elements_in_the_array_entry.get().split()
        elements_numbers = {}

        for e in repeating_elements_array:
            if e in elements_numbers:
                elements_numbers[e] += 1
            else:
                elements_numbers[e] = 1

        for e, number in elements_numbers.items():
            repeating_elements_in_the_array_result_listbox.insert(END, f"{e} sayısı x{number} kez")

    repeating_elements_in_the_array_label = Label(repeating_elements_in_the_array_window, text="Diziyi Gir (Örn: 1 2 3 4 5):")
    repeating_elements_in_the_array_label.pack()

    repeating_elements_in_the_array_entry = Entry(repeating_elements_in_the_array_window, width=25)
    repeating_elements_in_the_array_entry.pack()

    repeating_elements_in_the_array_button = Button(repeating_elements_in_the_array_window, text="Hesapla", command=repeating_elements)
    repeating_elements_in_the_array_button.pack(pady=10)

    repeating_elements_in_the_array_result_listbox = Listbox(repeating_elements_in_the_array_window, height=5, width=25)
    repeating_elements_in_the_array_result_listbox.pack()

    repeating_elements_in_the_array_window.mainloop()
def reopen_main_page(current_window):
    global current_x, current_y
    current_x, current_y = current_window.winfo_x(), current_window.winfo_y()
    current_window.destroy()
    main()
def main():
    global algorithm_app, current_x, current_y
    algorithm_app = Tk()
    algorithm_app.title("Algorithm - Menu")
    algorithm_app.resizable(False, False)

    if 'current_x' not in globals() and 'current_y' not in globals():
        screen_avg(algorithm_app, 400, 500)
    else:
        algorithm_app.geometry(f"400x500+{current_x}+{current_y}")

    header_label = Label(algorithm_app, text="Algorithm App", font=("Arial", 25, "bold"))
    header_label.pack(pady=(25, 0))

    group1_button = Button(algorithm_app, command=open_finding_prime_numbers_page, text="Asal Sayı Bulma", height=5, width=25)
    group1_button.place(x=10, y=100)

    group2_button = Button(algorithm_app, command=number_guessing_page, text="Sayı Tahmin Oyunu", height=5, width=25)
    group2_button.place(x=205, y=100)

    group3_button = Button(algorithm_app, command=roman_numeral_converter_page, text="Roman Rakamı Çevirici", height=5, width=25)
    group3_button.place(x=10, y=200)

    group4_button = Button(algorithm_app, command=binary_base_converter_page, text="İkilik Taban Çevirici", height=5, width=25)
    group4_button.place(x=205, y=200)

    group5_button = Button(algorithm_app, command=square_and_cube_calculation_page, text="Kare ve Küp Hesaplama", height=5, width=25)
    group5_button.place(x=10, y=300)

    group6_button = Button(algorithm_app, command=area_and_premeter_of_the_circle_calculation_page, text="Dairenin Alanı ve Çevresi", height=5, width=25)
    group6_button.place(x=205, y=300)

    group7_button = Button(algorithm_app, command=array_rotation_page, text="Dizi Döndürme", height=5, width=25)
    group7_button.place(x=10, y=400)

    group8_button = Button(algorithm_app, command=repeating_elements_in_the_array_page, text="Dizide Tekrar Edenler", height=5, width=25)
    group8_button.place(x=205, y=400)

    algorithm_app.mainloop()

if __name__ == "__main__":
    main()