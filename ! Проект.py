
import os
import sys

import tkinter as tk
import time
import random 
import pygame
import threading

from PIL import Image, ImageTk

from tkinter import scrolledtext, messagebox



# для экзешника

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)


# чтение статистики из файла

with open(resource_path('stati.txt')) as ff:
    pop = int(ff.readline())
    popv = float(ff.readline())
    popw = float(ff.readline())

    pop1 = int(ff.readline())
    popv1 = float(ff.readline())
    popw1 = float(ff.readline())

    pop2 = int(ff.readline())
    popw2 = float(ff.readline())

    ff.close()
 

#om1, om2, om3, ov1, ov2, ov3, ok1, ok2, ok3 = 0, 0, 0, 0, 0, 0, 0, 0, 0

user = ""
position = 0
mistakes = 0
glcon = ''
nn = 0
ww = 1
k = 0
useR = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
useA = []
klava = 0
user_texts = []
cont = ''
fla = 0
kol = 0



# чтение данных из файла для таблицы, для текста в одну строку

with open(resource_path('onee.txt')) as ff:
    om1 = float(ff.readline())
    om2 = float(ff.readline())
    om3 = float(ff.readline())
    ov1 = float(ff.readline())
    ov2 = float(ff.readline())
    ov3 = float(ff.readline())
    ok1 = int(ff.readline())
    ok2 = int(ff.readline())
    ok3 = int(ff.readline())
    ff.close()


# чтение данных из файла для таблицы, для полного текста

with open(resource_path('fulll.txt')) as ff:
    fm1 = float(ff.readline())
    fm2 = float(ff.readline())
    fm3 = float(ff.readline())
    fv1 = float(ff.readline())
    fv2 = float(ff.readline())
    fv3 = float(ff.readline())
    fk1 = int(ff.readline())
    fk2 = int(ff.readline())
    fk3 = int(ff.readline())
    ff.close()


# чтение списка выбранных жанров

with open('gerr.txt', 'r', encoding = 'utf-8') as file:
    geR = []
    lines = file.readlines()

    for line in lines:
        cl = line.strip()
        geR.append(cl)


# чтение состоняния клавиатуры

with open('klav.txt', 'r', encoding = 'utf-8') as file:
    klava = int(file.read().strip())


# отчистка экрана

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


# меню текста в ожну строчку

def one_text():
    global canvas, klava, btn

    root.geometry("1000x500")
    clear_window()

    canvas = tk.Canvas(root, width = 1000, height = 500, bg = "white")
    canvas.pack()

    canvas.configure(bg = "light blue")

    

    canvas.create_rectangle(400, 90, 650, 410, fill = 'CadetBlue3', outline = 'CadetBlue4')

    tk.Button(root, text = "Русский", command = firR).place(x = 450, y = 140, width = 150, height = 50)
    tk.Button(root, text = "Английский", command = firA).place(x = 450, y = 200, width = 150, height = 50)
    tk.Button(root, text = "Рандом", command = firAR).place(x = 450, y = 260, width = 150, height = 50)

    tk.Button(root, text = "Назад", command = show_main_menu).place(x = 20, y = 20, width = 50, height = 30)
    tk.Button(root, text = "Статистика", command = sta).place(x = 80, y = 20, width = 100, height = 30)

    #tk.Button(root, text = "Выбрать жанры", command = gen).place(x = 880, y = 20, width = 100, height = 30)
    tk.Button(root, text = "Выбрать жанры", command = back1).place(x = 450, y = 335, width = 150, height = 25) 

    btn = tk.Button(root, text = "Выключить клавиатуру" if klava == 1 else "Включить клавиатуру", command = kla)
    btn.place(x = 190, y = 20, width = 140, height = 30)


# состояние клавиатуры

def kla():
    global klava, btn

    if klava == 0:

        klava = 1
        btn.config(text = "Выключить клавиатуру")
    else:
        klava = 0
        btn.config(text = "Включить клавиатуру")

    with open('klav.txt', 'w', encoding = 'utf-8') as file:
        file.write(str(klava))


# меню полного текста

def full_text():
    global canvas, btn, klava

    root.geometry('1000x500')

    clear_window()

    canvas = tk.Canvas(root, width = 1000, height = 500, bg = "white")
    canvas.pack()

    canvas.configure(bg = "light blue")

    canvas.create_rectangle(400, 90, 650, 410, fill = 'CadetBlue3', outline = 'CadetBlue4')

    tk.Button(root, text = "Русский", command = secR).place(x = 450, y = 140, width = 150, height = 50)
    tk.Button(root, text = "Английский", command = secA).place(x = 450, y = 200, width = 150, height = 50)
    tk.Button(root, text = "Рандом", command = secAR).place(x = 450, y = 260, width = 150, height = 50)
    tk.Button(root, text = "Назад", command = show_main_menu).place(x = 20, y = 20, width = 50, height = 30)
    tk.Button(root, text = "Статистика", command = stat).place(x = 80, y = 20, width = 100, height = 30)

    btn = tk.Button(root, text = "Выключить клавиатуру" if klava == 1 else "Включить клавиатуру", command = kla)
    btn.place(x = 190, y = 20, width = 140, height = 30)

    #tk.Button(root, text = "Выбрать жанры", command = gen).place(x = 880, y = 20, width = 100, height = 30)
    tk.Button(root, text = "Выбрать жанр", command = back2).place(x = 450, y = 335, width = 150, height = 25) 


# сохранение выбранных жанров

def writ():
    with open('gerr.txt', 'w', encoding = 'utf-8') as file:
        for it in geR:
            file.write(it + '\n')


# возврат из "выбора жанров" в "текст в одну строчку"

def back1():
    global back
    back = 1
    gen()


# возврат из "выбора жанров" в "полного текста"

def back2():
    global back
    back = 2
    gen()

#=====================================================================================================================



#==========================================================================================================================
# выбор жанров

def gen():
    global canvas, geR, back, cont, kol
    clear_window()

    canvas = tk.Canvas(root, width = 1000, height = 500, bg = "white")
    canvas.pack()

    canvas.configure(bg = "light blue")

    if back == 1:
        tk.Button(root, text = "Назад", command = one_text).place(x = 20, y = 20, width = 50, height = 30)
    else:
        tk.Button(root, text = "Назад", command = full_text).place(x = 20, y = 20, width = 50, height = 30)


    # басни

    def gen1():
        global geR

        if 'bas1.txt' not in geR: 
            geR.extend(['bas1.txt', 'bas2.txt', 'bas3.txt', 'bas4.txt', 'bas5.txt', 'bas6.txt']) 
            button1.config(bg = 'light green')
        else:
            geR.remove('bas1.txt')
            geR.remove('bas2.txt')
            geR.remove('bas3.txt')
            geR.remove('bas4.txt')
            geR.remove('bas5.txt')
            geR.remove('bas6.txt')
            button1.config(bg = 'white')
        writ()

    button1 = tk.Button(root, text = "Басня", command = gen1, font = ("Arial", 14))
    button1.place(x = 180, y = 140, width = 200, height = 100)

    # цвет кнопки
    if 'bas1.txt' in geR: button1.config(bg = 'light green')
    else: button1.config(bg = 'white')


    # пословицы

    def gen2():
        global geR

        if 'pos1.txt' not in geR: 
            geR.extend(['pos1.txt', 'pos2.txt', 'pos3.txt', 'pos4.txt', 'pos5.txt', 'pos6.txt']) 
            button2.config(bg = 'light green')
        else:
            geR.remove('pos1.txt')
            geR.remove('pos2.txt')
            geR.remove('pos3.txt')
            geR.remove('pos4.txt')
            geR.remove('pos5.txt')
            geR.remove('pos6.txt')
            button2.config(bg = 'white')
        writ()

    button2 = tk.Button(root, text = "Пословица", command = gen2, font = ("Arial", 14))
    button2.place(x = 400, y = 140, width = 200, height = 100)

    # цвет кнопки
    if 'pos1.txt' in geR: button2.config(bg = 'light green')
    else: button2.config(bg = 'white')


    # скороговорки

    def gen3():
        global geR

        if 'sk1.txt' not in geR: 
            geR.extend(['sk1.txt', 'sk2.txt', 'sk3.txt', 'sk4.txt', 'sk5.txt', 'sk6.txt']) 
            button3.config(bg = 'light green')
        else:
            geR.remove('sk1.txt')
            geR.remove('sk2.txt')
            geR.remove('sk3.txt')
            geR.remove('sk4.txt')
            geR.remove('sk5.txt')
            geR.remove('sk6.txt')
            button3.config(bg = 'white')
        writ()

    button3 = tk.Button(root, text = "Скороговорка", command = gen3, font = ("Arial", 14))
    button3.place(x = 620, y = 140, width = 200, height = 100)

    # цвет кнопки
    if 'sk1.txt' in geR: button3.config(bg = 'light green')
    else: button3.config(bg = 'white')


    # считалки

    def gen4():
        global geR

        if 'sch1.txt' not in geR: 
            geR.extend(['sch1.txt', 'sch2.txt', 'sch3.txt', 'sch4.txt', 'sch5.txt', 'sch6.txt']) 
            button4.config(bg = 'light green')
        else:
            geR.remove('sch1.txt')
            geR.remove('sch2.txt')
            geR.remove('sch3.txt')
            geR.remove('sch4.txt')
            geR.remove('sch5.txt')
            geR.remove('sch6.txt')
            button4.config(bg = 'white')
        writ()

    button4 = tk.Button(root, text = "Считалочка", command = gen4, font = ("Arial", 14))
    button4.place(x = 180, y = 260, width = 200, height = 100)

    # цвет кнопки
    if 'sch1.txt' in geR: button4.config(bg = 'light green')
    else: button4.config(bg = 'white')


    # загадки

    def gen5():
        global geR

        if 'zag1.txt' not in geR: 
            geR.extend(['zag1.txt', 'zag2.txt', 'zag3.txt', 'zag4.txt', 'zag5.txt', 'zag6.txt']) 
            button5.config(bg = 'light green')
        else:
            geR.remove('zag1.txt')
            geR.remove('zag2.txt')
            geR.remove('zag3.txt')
            geR.remove('zag4.txt')
            geR.remove('zag5.txt')
            geR.remove('zag6.txt')
            button5.config(bg = 'white')
        writ()

    button5 = tk.Button(root, text = "Загадка", command = gen5, font = ("Arial", 14))
    button5.place(x = 400, y = 260, width = 200, height = 100)

    # цвет кнопки
    if 'zag1.txt' in geR: button5.config(bg = 'light green')
    else: button5.config(bg = 'white')


    # рассказы

    def gen6():
        global geR

        if 'ras1.txt' not in geR: 
            geR.extend(['ras1.txt', 'ras2.txt', 'ras3.txt', 'ras4.txt', 'ras5.txt', 'ras6.txt']) 
            button6.config(bg = 'light green')
        else:
            geR.remove('ras1.txt')
            geR.remove('ras2.txt')
            geR.remove('ras3.txt')
            geR.remove('ras4.txt')
            geR.remove('ras5.txt')
            geR.remove('ras6.txt')
            button6.config(bg = 'white')
        writ()

    button6 = tk.Button(root, text = "Рассказ", command = gen6, font = ("Arial", 14))
    button6.place(x = 620, y = 260, width = 200, height = 100)

    # цвет кнопки
    if 'ras1.txt' in geR: button6.config(bg = 'light green')
    else: button6.config(bg = 'white')


    button7 = tk.Button(root, text = "Дoбавить текст", command = main, font = ("Arial", 14), bg = 'light blue')
    button7.place(x = 620, y = 380, width = 200, height = 100)


    def gen8():
        global geR, user_text_added
        
        # добавлен ли текст в список
        if 'user.txt' not in geR:
            # Существует ли файл
            try:
                with open('user.txt', 'r', encoding='utf-8') as file:
                    content = file.read()

                    if len(content.strip()) > 0:  # Проверяет пустой ли файл
                        geR.append('user.txt')
                        button8.config(bg = 'light green')
                        user_text_added = True
                    else:
                        messagebox.showinfo("Информация", "Сначала добавьте текст через кнопку 'Добавить текст'")
            except FileNotFoundError:
                messagebox.showinfo("Информация", "Сначала добавьте текст через кнопку 'Добавить текст'")
        else:
            geR.remove('user.txt')
            button8.config(bg = 'white')
            user_text_added = False
        
        writ()

    button8 = tk.Button(root, text = "Мой текст", command = gen8, font=("Arial", 14))
    button8.place(x = 400, y = 380, width = 200, height = 100)

    if 'user.txt' in geR:
        button8.config(bg = 'light green')
    else:
        button8.config(bg = 'white')

#====================================================================================================================
#=====================================================================================================================
# для добавления текста
def main():
    global cont, kol, geR
    
    # сохранение текста
    def save_text():
        global cont, kol
        cont = text_area.get("1.0", tk.END).strip()  # убирает лишние пробелы и переносы
        
        if cont:  # проверяет пустой ли текст
            kol += 1
            # сохраняет текст в файл user.txt
            with open('user.txt', 'w', encoding='utf-8') as file:
                # сохраняет номер записи
                file.write(f"Запись #{kol}\n")
                file.write(cont)
            
            messagebox.showinfo("Успех", "Текст успешно сохранен!")
            root_save.destroy()
        else:
            messagebox.showwarning("Предупреждение", "Текст не может быть пустым!")

    root_save = tk.Tk()
    root_save.title("Текст")
    root_save.geometry("500x400")
    
    label = tk.Label(root_save, text = "Введите ваш текст:", font = ("Arial", 12))
    label.pack(pady = 10)
    
    # текстовое поле, которое можно крутить вниз
    text_area = scrolledtext.ScrolledText(root_save, wrap = tk.WORD, width = 50, height = 15, font = ("Arial", 10))
    text_area.pack(pady = 10, padx = 10, fill = tk.BOTH, expand=True)
    
    btn_save = tk.Button(root_save, text = "Сохранить текст", command = save_text, font = ("Arial", 10), bg = "lightblue")
    btn_save.pack(pady = 10)
    
    root_save.mainloop()
#===========================================================================================================================
        
# меню тетриса

def tet():
    global canvas

    clear_window()

    canvas = tk.Canvas(root, width = 1000, height = 500, bg = "white")
    canvas.pack()

    canvas.configure(bg = "light blue")

    canvas.create_rectangle(400, 120, 640, 380, fill = 'CadetBlue3', outline = 'CadetBlue4')

    tk.Button(root, text = "Русский", command = tR).place(x = 450, y = 170, width = 150, height = 50)
    tk.Button(root, text = "Английский", command = tE).place(x = 450, y = 230, width = 150, height = 50)

    tk.Button(root, text = "Выбрать букву", command = cho).place(x = 450, y = 305, width = 150, height = 25) 

    tk.Button(root, text = "Назад", command = show_main_menu).place(x = 20, y = 20, width = 50, height = 30)
    tk.Button(root, text = "Статистика", command = stati).place(x = 80, y = 20, width = 100, height = 30)


# выбор букв для тетриса

def cho():
    global canvas, dicti, useR, useA
    xx = 100
    yy = 100
    
    clear_window()
    
    canvas = tk.Canvas(root, width = 1000, height = 500, bg = "white")
    canvas.pack()
    canvas.configure(bg = "light blue")
    
    # use = ['a', 'b']
    dicti = {}

    # чтение всех русских букв
    with open('maR.txt', 'r', encoding = 'utf-8') as file:
        mas_letterR = []
        lines = file.readlines()

        for line in lines:
            cl = line.strip()
            mas_letterR.append(cl)

    # чтение всех английских букв
    with open('maE.txt', 'r', encoding = 'utf-8') as file:
        mas_letterA = []
        lines = file.readlines()

        for line in lines:
            cl = line.strip()
            mas_letterA.append(cl)


    #mas_letterR = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    #mas_letterA = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # разные пальцы
    index_right = ['н', 'г', 'р', 'о', 'т', 'ь', 'y', 'u', 'h', 'j', 'n', 'm']
    index_left = ['к', 'е', 'а', 'п', 'м', 'и', 'r', 't', 'f', 'g', 'v', 'b']

    middle_right = ['ш', 'л', 'б', 'i', 'k']
    middle_left = ['у', 'в', 'с', 'e', 'd', 'c']

    ring_right = ['щ', 'д', 'ю', 'o', 'l']
    ring_left = ['ц', 'ы', 'ч', 'w', 's', 'x']

    little_right = ['з', 'ж', 'х', 'э', 'ъ', 'p']
    little_left = ['й', 'ф', 'я', 'ё', 'q', 'a', 'z']

    tk.Button(root, text = "Назад", command = tet).place(x = 20, y = 20, width = 50, height = 30)

    # меняет цвет кнопки
    def update(letterR):
        if letterR in useR:
            useR.remove(letterR)
            dicti[letterR].config(bg = 'white')
        else:
            useR.append(letterR)
            dicti[letterR].config(bg = 'light green')

    # выбор всеха букв
    def select_all():
        for letter in mas_letterR + mas_letterA:
            if letter not in useR:
                useR.append(letter)
                if letter in dicti:
                    dicti[letter].config(bg = 'light green')

    # удаление всех букв
    def deselect_all():
        useR.clear()
        for letter in dicti:
            dicti[letter].config(bg = 'white')

    # выбор букв для конкретного пальца
    def select_letters(finger_letters):
        all_selected = all(letter in useR for letter in finger_letters)
    
        # если выбраны все буквы пальца, то все удаляются
        if all_selected:
            for letter in finger_letters:
                if letter in useR:
                    useR.remove(letter)
                if letter in dicti:
                    dicti[letter].config(bg = 'white')
                     
        # иначе оставшиеся становятся зелеными
        else:
            for letter in finger_letters:
                if letter not in useR:
                    useR.append(letter)
                if letter in dicti:
                    dicti[letter].config(bg = 'light green')

    tk.Button(root, text = "Выделить все", command = select_all, font = ("Arial", 10), bg = "light blue").place(x = 850, y = 60, width = 140, height = 30)
    tk.Button(root, text = "Удалить все", command = deselect_all, font = ("Arial", 10), bg = "light blue").place(x = 850, y = 100, width = 140, height = 30)

    tk.Button(root, text = "Правый указательный", command = lambda: select_letters(index_right),font = ("Arial", 10), bg="light blue").place(x = 850, y = 150, width = 140, height = 30)
    tk.Button(root, text = "Правый средний", command = lambda: select_letters(middle_right),font = ("Arial", 10), bg = "light blue").place(x = 850, y = 190, width = 140, height = 30)
    tk.Button(root, text = "Правый безымянный", command = lambda: select_letters(ring_right),font = ("Arial", 10), bg = "light blue").place(x = 850, y = 230, width = 140, height = 30)
    tk.Button(root, text = "Правый мизинец", command = lambda: select_letters(little_right),font = ("Arial", 10), bg = "light blue").place(x = 850, y = 270, width = 140, height = 30)

    tk.Button(root, text = "Левый указательный", command = lambda: select_letters(index_left),font = ("Arial", 10), bg = "light blue").place(x = 850, y = 320, width = 140, height = 30)
    tk.Button(root, text = "Левый средний", command = lambda: select_letters(middle_left),font = ("Arial", 10), bg = "light blue").place(x = 850, y = 360, width = 140, height = 30)
    tk.Button(root, text = "Левый безымянный", command = lambda: select_letters(ring_left),font = ("Arial", 10), bg = "light blue").place(x = 850, y = 400, width = 140, height = 30)
    tk.Button(root, text = "Левый мизинец", command = lambda: select_letters(little_left),font = ("Arial", 10), bg = "light blue").place(x = 850, y = 440, width = 140, height = 30)

    # кнопки дял русских букв
    for letterR in mas_letterR:
        # определение начального цвета кнопки
        if letterR in useR:
            btn = tk.Button(root, text = letterR, font = ("Arial", 14), bg = 'light green')#.place(x = xx, y = yy, width = 30, height = 30)
        else:
            btn = tk.Button(root, text = letterR, font = ("Arial", 14), bg = 'white')#.place(x = xx, y = yy, width = 30, height = 30)

        btn.config(command = lambda l = letterR: update(l))

        btn.place(x = xx, y = yy, width = 30, height = 30)

        # ссылка на кнопку в словаре
        dicti[letterR] = btn


        if xx >= 700:
            xx = 100
            yy += 40
        else:
            xx += 40

    xx = 100
    yy = 300

    # меняет цвет английских букв

    def update2(letterA):
        if letterA in useR:
            useR.remove(letterA)
            dicti[letterA].config(bg = 'white')
        else:
            useR.append(letterA)
            dicti[letterA].config(bg = 'light green')

    # кнопки для английских букв
    for letterA in mas_letterA:
        if letterA in useR:
            btn = tk.Button(root, text = letterA, font = ("Arial", 14), bg = 'light green')#.place(x = xx, y = yy, width = 30, height = 30)
        else:
            btn = tk.Button(root, text = letterA, font = ("Arial", 14), bg = 'white')#.place(x = xx, y = yy, width = 30, height = 30)

        btn.config(command = lambda l = letterA: update2(l))

        btn.place(x = xx, y = yy, width = 30, height = 30)

        dicti[letterA] = btn


        if xx >= 700:
            xx = 100
            yy += 40
        else:
            xx += 40

#=====================================================================================================================================================================================

# показывает меню

def show_main_menu():
    global canvas
    root.geometry("1000x500")
    clear_window()
    root.configure(bg = 'light blue')

    tk.Button(root, text = "Текст в одну строчку", command = one_text).place(x = 400, y = 60, width = 200, height = 50)
    tk.Button(root, text = "Полный текст", command = full_text).place(x = 400, y = 170, width = 200, height = 50)

    tk.Button(root, text = "Тетрис", command = tet).place(x = 400, y = 280, width = 200, height = 50)
    tk.Button(root, text = "Общая статистика", command = statt).place(x = 400, y = 390, width = 200, height = 50)

    tk.Button(root, text = "Сбросить статистику", command = bye).place(x = 855, y = 450, width = 125, height = 30)


#==========================================================================================================================

# выбор текста в одну строчку на русском
def firR():
    global glcon, p, k, geR
    
    fi = ['bas1.txt', 'bas2.txt', 'bas3.txt', 'pos1.txt', 'pos2.txt', 'pos3.txt', 'ras1.txt', 'ras2.txt', 'ras3.txt', 'sch1.txt', 'sch2.txt', 'sch3.txt', 'sk1.txt', 'sk2.txt', 'sk3.txt', 'zag1.txt', 'zag2.txt', 'zag3.txt']
    
    if 'user.txt' in geR:
        fi.append('user.txt')
    
    fil = list(set(fi) & set(geR))

    if not fil:  # пустой ли список
        messagebox.showwarning("Не выбран ни один жанр")
        return

    fill = random.choice(fil)

    if fill == 'user.txt':
        # чтение текста
        try:
            with open('user.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()
                # пропуск первой строки
                if len(lines) > 1:
                    glcon = ''.join(lines[1:]).strip()
                else:
                    glcon = ''.join(lines).strip()
        except FileNotFoundError:
            messagebox.showwarning("Предупреждение", "Файл с пользовательским текстом не найден!")
            return
    else:
        # чтение обычного текста
        try:
            with open(resource_path(fill), 'r', encoding='utf-8') as file:
                glcon = file.read().strip()
        except:
            messagebox.showwarning("Ошибка", f"Не удалось загрузить файл {fill}")
            return

    k = 0
    p = 1

    first()

#====================

# выбор текста в одну строчку на английском
def firA():
    global glcon, p, k, geR

    fi = ['bas4.txt', 'bas5.txt', 'bas6.txt', 'pos4.txt', 'pos5.txt', 'pos6.txt', 'ras4.txt', 'ras5.txt', 'ras6.txt', 'sch4.txt', 'sch5.txt', 'sch6.txt', 'sk4.txt', 'sk5.txt', 'sk6.txt', 'zag4.txt', 'zag5.txt', 'zag6.txt']
    
    if 'user.txt' in geR:
        fi.append('user.txt')
    
    fil = list(set(fi) & set(geR))

    if not fil:  # пустой ли список
        messagebox.showwarning("Предупреждение", "Не выбран ни один жанр! Выберите хотя бы один жанр.")
        return

    fill = random.choice(fil)

    if fill == 'user.txt':
        # чтение текста
        try:
            with open('user.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()
                # пропуск первой строки
                if len(lines) > 1:
                    glcon = ''.join(lines[1:]).strip()
                else:
                    glcon = ''.join(lines).strip()
        except FileNotFoundError:
            messagebox.showwarning("Предупреждение", "Файл с пользовательским текстом не найден!")
            return
    else:
        # чтение обычного текста
        try:
            with open(resource_path(fill), 'r', encoding='utf-8') as file:
                glcon = file.read().strip()
        except:
            messagebox.showwarning("Ошибка", f"Не удалось загрузить файл {fill}")
            return

    p = 2
    k = 0

    first()


#=====================

# выбор текста в одну строчку на рандомномязыке
def firAR():
    global glcon, p, k, geR

    fi = ['bas4.txt', 'bas5.txt', 'bas6.txt', 'pos4.txt', 'pos5.txt', 'pos6.txt', 'ras4.txt', 'ras5.txt', 'ras6.txt', 'sch4.txt', 'sch5.txt', 'sch6.txt', 'sk4.txt', 'sk5.txt', 'sk6.txt', 'zag4.txt', 'zag5.txt', 'zag6.txt', 'bas1.txt', 'bas2.txt', 'bas3.txt', 'pos1.txt', 'pos2.txt', 'pos3.txt', 'ras1.txt', 'ras2.txt', 'ras3.txt', 'sch1.txt', 'sch2.txt', 'sch3.txt', 'sk1.txt', 'sk2.txt', 'sk3.txt', 'zag1.txt', 'zag2.txt', 'zag3.txt']
    
    if 'user.txt' in geR:
        fi.append('user.txt')
    
    fil = list(set(fi) & set(geR))

    if not fil:  # пустой ли список
        messagebox.showwarning("Предупреждение", "Не выбран ни один жанр! Выберите хотя бы один жанр.")
        return

    fill = random.choice(fil)

    if fill == 'user.txt':
        # чтение текста
        try:
            with open('user.txt', 'r', encoding = 'utf-8') as file:
                lines = file.readlines()
                # пропуск первой строки
                if len(lines) > 1:
                    glcon = ''.join(lines[1:]).strip()
                else:
                    glcon = ''.join(lines).strip()
        except FileNotFoundError:
            messagebox.showwarning("Файл с пользовательским текстом не найден!")
            return
    else:
        # чтение обычного текста
        try:
            with open(resource_path(fill), 'r', encoding = 'utf-8') as file:
                glcon = file.read().strip()
        except:
            messagebox.showwarning(f"Не удалось загрузить файл {fill}")
            return

    p = 3
    k = 0

    first()


#==========================================================================================================================


# текст в одну строчку 
def first():
    global seconds, user, position, mistakes, glcon, canvas, pop, popv, popw, pop1, popv1, popw1, pop2, popw2, p, k, klava, om1, om2, om3, ov1, ov2, ov3, ok1, ok2, ok3

    clear_window()
    root.configure(bg = "light blue")

    user = ""
    position = 0
    mistakes = 0
    seconds = 0
    run = False

    # увеличение экрана под клавиатуру
    if klava == 1:
        root.geometry("1000x700")
    else:
        root.geometry("1000x500")


    canvas = tk.Canvas(root, width = 1000, height = 500, bg = "light blue")
    canvas.pack()

    canvas.configure(bg = "light blue")

    # картинка клавиатуры
    if klava == 1:
        try:
            image = Image.open(resource_path("pechat.png"))
            image.thumbnail((700, 700))
            tk_image = ImageTk.PhotoImage(image)
            
            img_label = tk.Label(root, image = tk_image, bg = "light blue")
            img_label.image = tk_image
            img_label.place(x = 150, y = 400)
            
        except Exception as e:
            print(f"Ошибка загрузки изображения: {e}")
            tk.Label(root, text = "Изображение не найдено", bg = "light blue").place(x = 150, y = 300)
            tk_image = None

    tk.Button(root, text = "Назад", command = one_text).place(x = 20, y = 20, width = 50, height = 30)

#--------------------------

    content = glcon

    canvas.create_rectangle(230, 230, 1000, 270, fill = "white", outline = "black", tags = "rec")
    canvas.create_text(250, 250, text = content, font = ("Arial", 20), fill = "grey35", anchor = 'w', tags = "current_text")


    # выделение нужной букввы
    canvas.create_text(250, 250, text = content[0], font = ("Arial", 20), fill = "black", anchor = 'w', tags = "one")
    canvas.create_text(249, 249, text = content[0], font = ("Arial", 20), fill = "black", anchor = 'w', tags = "one1")
    canvas.create_text(250, 249, text = content[0], font = ("Arial", 20), fill = "black", anchor = 'w', tags = "one2")
    canvas.create_text(249, 250, text = content[0], font = ("Arial", 20), fill = "black", anchor = 'w', tags = "one3")


#=====================================================

    # вывод звука
    pygame.mixer.init()
    orig = content


    time_label = tk.Label(root, text = f"t = {seconds} сек", font = ("Arial", 14), bg = "light blue")
    time_label.place(x = 850, y = 20)

    canvas.create_text(890, 60, text = f'v = {0} зн/с', font = ("Arial", 14), fill = "black", tags = "sp")

#=====================================================
    # вывод звукв
    def play_sound():
        sounds = ['sound 1.mp3', 'sound 2.mp3', 'sound 3.mp3']
        sou = random.choice(sounds)

        try:
            pygame.mixer.music.load(resource_path(sou))
            pygame.mixer.music.play()
        
            threading.Thread(target = lambda: (time.sleep(0.5), pygame.mixer.music.stop()), daemon = True).start()
        
        except Exception as e:
            print(f"Ошибка: {e}")
#======================================================

    # начало секундомера
    def start_timer():
        nonlocal run
        if not run: 
            run = True
            add_every_second()

    # секундомер
    def add_every_second():
        global seconds, position
        nonlocal run
        if run:
            seconds += 1
            # вывод на экран
            time_label.place(x = 850, y = 20)
            time_label.config(text = f"t = {seconds} с.")

            root.after(1000, add_every_second)
#======================================================
    orig = content
#======================================================

    # функция для проверки букв
    def on_key_press(event):
        global user, position, mistakes, seconds, pop, popv, popw, pop1, popv1, popw1, pop2, popw2, p, k, om1, om2, om3, ov1, ov2, ov3, ok1, ok2, ok3
        nonlocal run, content

        if k == 10:
            return

        if not run and position == 0:
            start_timer()

        if event.keysym == 'Escape':
            show_main_menu()
            return

        elif event.keysym == 'Return':
            if position < len(orig) and orig[position] == '\n':
                position += 1
                content = orig[position:]
            else:
                mistakes += 1
                play_sound()

        elif event.keysym == 'space':
            if position < len(orig) and orig[position] == ' ':
                position += 1
                content = orig[position:] 
            else:
                mistakes += 1
                play_sound()

        # проверка буквы        
        elif event.char and event.char != '' and k != 10:
            if position < len(orig) and orig[position] == event.char:
                position += 1
                content = orig[position:] # обновление видимого текста
            else:
                mistakes += 1
                play_sound()

        # после нажатия буквы, переменные перезаписываются
        canvas.delete("user")
        canvas.delete("cursor")
        canvas.delete("current_text")
        canvas.delete("end_text")
        canvas.delete("sp")
        canvas.delete("ti")
        canvas.delete('one')
        canvas.delete('one1')
        canvas.delete('one2')
        canvas.delete('one3')

        
        # уловие конца программы

        if position >= len(orig):

            root.geometry("1000x500")

            if klava == 1:
                try:
                    img_label.place_forget()
                except:
                    pass

            # удаление всего с экрана
            canvas.delete('sta')
            canvas.delete('usert')
            run = False
            canvas.configure(bg = "light blue")
            canvas.delete('rec')

            # рассчет скорости
            if seconds > 0 and position > 0:
                speed = position / (seconds / 60)
            else:
                speed = 0


            tk.Button(root, text = "Назад", command = one_text).place(x = 20, y = 20, width = 50, height = 30)

            time_label.place_forget() # удаление таймера
            
            pop += 1 # кол-во напечатаных текстов
            if pop == 1:
                kolvo = 1
            else:
                kolvo = 2
            popv = (popv * (pop - 1) + speed) / kolvo # средняя скорость
            popw = (popw * (pop - 1) + (mistakes * 100) / position) / kolvo # средний процент ошибок

            #om1, om2, om3, ov1, ov2, ov3, ok1, ok2, ok3 = om2, om3, (mistakes * 100) / position, ov2, ov3, speed, ok2, ok3, mistakes

            # перезапись статистики
            with open(resource_path("stati.txt"), "w") as file:
                file.write(str(pop) + "\n")
                file.write(str(popv) + "\n")
                file.write(str(popw) + "\n")
                file.write(str(pop1) + "\n")
                file.write(str(popv1) + "\n")
                file.write(str(popw1) + "\n")
                file.write(str(pop2) + "\n")
                file.write(str(popw2) + "\n")
                file.close()

            
            # сохранение последних трех результатов
            with open(resource_path("onee.txt"), "w") as file:
                file.write(str(om1) + "\n")
                file.write(str(om2) + "\n")
                file.write(str(om3) + "\n")
                file.write(str(ov1) + "\n")
                file.write(str(ov2) + "\n")
                file.write(str(ov3) + "\n")
                file.write(str(ok1) + "\n")
                file.write(str(ok2) + "\n")
                file.write(str(ok3) + "\n")
                file.close()


            canvas.create_text(500, 60, text = f"Время игры: {seconds} сек ({seconds / 60:.2f} мин)", font = ("Arial", 14), fill = "black")

            # таблица с результатами
            head = ["", "Текущая игра", "Прошлая игра", "Две игры назад", "Три игры назад", "Среднее"]
            heady = 120
            wid = 150
            stax = 50

            canvas.create_rectangle(stax - 10, heady - 30, stax + len(head) * wid + 10, heady + 160,  fill = "white", outline = "CadetBlue4", width = 2)

            for i, header in enumerate(head): # написание заголовков
                x = stax + i * wid + wid // 2
                canvas.create_text(x, heady + 5, text = header, font = ("Arial", 12), fill = "black")

                if i > 0:
                    canvas.create_line(stax + i * wid, heady - 20, stax + i * wid, heady + 140, fill = "CadetBlue3") # вертикальные линии

            for i in range(4):
                y = heady + 35 + i * 35
                canvas.create_line(stax, y, stax + len(head) * wid, y, fill = "CadetBlue3") # горизонтальные линии

            # данные для следующей таблицы
            rows = [("Скорость (зн/мин)", f"{speed:.2f}", f"{ov3:.2f}", f"{ov2:.2f}", f"{ov1:.2f}", f"{popv:.2f}"), 
                    ("Ошибки (%)", f"{(mistakes * 100) / position:.2f}%", f"{om3:.2f}%", f"{om2:.2f}%", f"{om1:.2f}%", f"{popw:.2f}%"), 
                    ("Кол-во ошибок", str(mistakes), str(ok3), str(ok2), str(ok1), f"{(popw * position / 100) if position > 0 else 0:.1f}")]
            
            # вывод остального
            for row_i, row_d in enumerate(rows):
                row_y = heady + 35 + row_i * 35
                for col_idx, cell in enumerate(row_d):
                    x = stax + col_idx * wid + wid // 2       
                    canvas.create_text(x, row_y + 18, text = cell, font = ("Arial", 11), fill = "black")

            om1, om2, om3, ov1, ov2, ov3, ok1, ok2, ok3 = om2, om3, (mistakes * 100) / position, ov2, ov3, speed, ok2, ok3, mistakes


            if p == 1:
                tk.Button(root, text = "Заново", command = firR).place(x = 450, y = 350, width = 100, height = 40)
            if p == 2:
                tk.Button(root, text = "Заново", command = firA).place(x = 450, y = 350, width = 100, height = 40)
            if p == 3:
                tk.Button(root, text = "Заново", command = firAR).place(x = 450, y = 350, width = 100, height = 40)

            tk.Button(root, text = "В меню", command = show_main_menu).place(x = 450, y = 400, width = 100, height = 40)

            k = 10

            return

        else:

            canvas.create_text(250, 250, text = content, font = ("Arial", 20), fill = "grey35", anchor = 'w', tags = "current_text")

            #canvas.create_text(900, 70, text = f'v = {position / (seconds / 60):.2f} зн/мин', font = ("Arial", 14), fill = "black", tags = "sp")
            canvas.create_text(850, 60, text = f'v = {(position / seconds):.2f} зн/мин', font = ("Arial", 14), fill = "black", tags = "sp", anchor = 'w')

            canvas.create_text(250, 250, text = content[0], font = ("Arial", 20), fill = "black", anchor = 'w', tags = "one")
            canvas.create_text(249, 249, text = content[0], font = ("Arial", 20), fill = "black", anchor = 'w', tags = "one1")
            canvas.create_text(250, 249, text = content[0], font = ("Arial", 20), fill = "black", anchor = 'w', tags = "one2")
            canvas.create_text(249, 250, text = content[0], font = ("Arial", 20), fill = "black", anchor = 'w', tags = "one3")

        return "break"
    

    add_every_second()
    root.bind('<KeyPress>', on_key_press)
    root.focus_set()
#=====================================================================================================================
# выбор полного текста на русском
def secR():
    global glcon, o, l, geR

    fi = ['bas1.txt', 'bas2.txt', 'bas3.txt', 'pos1.txt', 'pos2.txt', 'pos3.txt', 'ras1.txt', 'ras2.txt', 'ras3.txt', 'sch1.txt', 'sch2.txt', 'sch3.txt', 'sk1.txt', 'sk2.txt', 'sk3.txt', 'zag1.txt', 'zag2.txt', 'zag3.txt']
    
    if 'user.txt' in geR:
        fi.append('user.txt')
    
    fil = list(set(fi) & set(geR))

    if not fil:
        messagebox.showwarning("Предупреждение", "Не выбран ни один жанр! Выберите хотя бы один жанр.")
        return

    fill = random.choice(fil)

    if fill == 'user.txt':
        try:
            with open('user.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if len(lines) > 1:
                    glcon = ''.join(lines[1:]).strip()
                else:
                    glcon = ''.join(lines).strip()
        except FileNotFoundError:
            messagebox.showwarning("Предупреждение", "Файл с пользовательским текстом не найден!")
            return
    else:
        try:
            with open(resource_path(fill), 'r', encoding='utf-8') as file:
                glcon = file.read().strip()
        except:
            messagebox.showwarning("Ошибка", f"Не удалось загрузить файл {fill}")
            return

    o = 1
    l = 0

    secound()

#====================
# выбор полного текста на английском
def secA():
    global glcon, o, l, geR

    fi = ['bas4.txt', 'bas5.txt', 'bas6.txt', 'pos4.txt', 'pos5.txt', 'pos6.txt', 'ras4.txt', 'ras5.txt', 'ras6.txt', 'sch4.txt', 'sch5.txt', 'sch6.txt', 'sk4.txt', 'sk5.txt', 'sk6.txt', 'zag4.txt', 'zag5.txt', 'zag6.txt']
    
    if 'user.txt' in geR:
        fi.append('user.txt')
    
    fil = list(set(fi) & set(geR))

    if not fil:
        messagebox.showwarning("Предупреждение", "Не выбран ни один жанр! Выберите хотя бы один жанр.")
        return

    fill = random.choice(fil)

    if fill == 'user.txt':
        try:
            with open('user.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if len(lines) > 1:
                    glcon = ''.join(lines[1:]).strip()
                else:
                    glcon = ''.join(lines).strip()
        except FileNotFoundError:
            messagebox.showwarning("Предупреждение", "Файл с пользовательским текстом не найден!")
            return
    else:
        try:
            with open(resource_path(fill), 'r', encoding='utf-8') as file:
                glcon = file.read().strip()
        except:
            messagebox.showwarning("Ошибка", f"Не удалось загрузить файл {fill}")
            return

    o = 2
    l = 0

    secound()

#=====================
# выбор полного текста на рандомном
def secAR():
    global glcon, o, l, geR

    fi = ['bas4.txt', 'bas5.txt', 'bas6.txt', 'pos4.txt', 'pos5.txt', 'pos6.txt', 'ras4.txt', 'ras5.txt', 'ras6.txt', 'sch4.txt', 'sch5.txt', 'sch6.txt', 'sk4.txt', 'sk5.txt', 'sk6.txt', 'zag4.txt', 'zag5.txt', 'zag6.txt', 'bas1.txt', 'bas2.txt', 'bas3.txt', 'pos1.txt', 'pos2.txt', 'pos3.txt', 'ras1.txt', 'ras2.txt', 'ras3.txt', 'sch1.txt', 'sch2.txt', 'sch3.txt', 'sk1.txt', 'sk2.txt', 'sk3.txt', 'zag1.txt', 'zag2.txt', 'zag3.txt']
    
    if 'user.txt' in geR:
        fi.append('user.txt')
    
    fil = list(set(fi) & set(geR))

    if not fil:
        messagebox.showwarning("Предупреждение", "Не выбран ни один жанр! Выберите хотя бы один жанр.")
        return

    fill = random.choice(fil)

    if fill == 'user.txt':
        try:
            with open('user.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if len(lines) > 1:
                    glcon = ''.join(lines[1:]).strip()
                else:
                    glcon = ''.join(lines).strip()

        except FileNotFoundError:
            messagebox.showwarning("Предупреждение", "Файл с пользовательским текстом не найден!")
            return
    else:
        try:
            with open(resource_path(fill), 'r', encoding='utf-8') as file:
                glcon = file.read().strip()
        except:
            messagebox.showwarning("Ошибка", f"Не удалось загрузить файл {fill}")
            return

    o = 3
    l = 0

    secound()

#=====================================================================================================================
# полный текст
def secound():
    global seconds, user, position, mistakes, glcon, canvas, pop1, popv1, popw1, pop, popv, popw, pop2, popw2, o, l, klava, fm1, fm2, fm3, fv1, fv2, fv3, fk1, fk2, fk3
    clear_window()
    root.configure(bg = "light blue")

    user = ""
    position = 0
    mistakes = 0
    seconds = 0
    run = False

    canvas = tk.Canvas(root, width = 1000, height = 500, bg = "white")
    canvas.pack()

    canvas.configure(bg = "light blue")

    if klava == 1:
        root.geometry("1000x700")
    else:
        root.geometry("1000x500")

    if klava == 1:
        try:
            image = Image.open(resource_path("pechat.png"))
            image.thumbnail((700, 700))
            tk_image = ImageTk.PhotoImage(image)
            
            img_label = tk.Label(root, image = tk_image, bg = "light blue")
            img_label.image = tk_image
            img_label.place(x = 150, y = 400)
            
        except Exception as e:
            print(f"Ошибка загрузки изображения: {e}")
            tk.Label(root, text="Изображение не найдено", bg = "light blue").place(x = 150, y = 300)
            tk_image = None

    tk.Button(root, text = "Назад", command = full_text).place(x = 20, y = 20, width = 50, height = 30)
#--------------------------

    content = glcon
    canvas.create_text(100, 50, text = content, font = ("Arial", 18), fill = "dark gray", width = 700, anchor = 'nw', tags = 'sta')

#=====================================================
    pygame.mixer.init()
    orig = content

    time_label = tk.Label(root, text = f"t = {seconds} сек", font = ("Arial", 14), bg = "light blue")
    time_label.place(x = 850, y = 20)

    canvas.create_text(890, 60, text = f'v = {0} зн/с', font = ("Arial", 14), fill = "black", tags = "sp")
#=====================================================
    def play_sound():
        sounds = ['sound 1.mp3', 'sound 2.mp3', 'sound 3.mp3']
        sou = random.choice(sounds)

        try:
            pygame.mixer.music.load(resource_path(sou))
            pygame.mixer.music.play()
        
            threading.Thread(target = lambda: (time.sleep(0.5), pygame.mixer.music.stop()), daemon = True).start()
        
        except Exception as e:
            print(f"Ошибка: {e}")
#======================================================
    def start_timer():
        nonlocal run
        if not run: 
            run = True
            add_every_second()

    def add_every_second():
        global seconds, position
        nonlocal run
        if run:
            seconds += 1
            time_label.place(x = 850, y = 20)
            time_label.config(text = f"t = {seconds} с.")
            root.after(1000, add_every_second)

#======================================================
    orig = content
#======================================================
    def on_key_press(event):
        global user, position, mistakes, seconds, pop1, popv1, popw1, pop, popv, popw, pop2, popw2, o, l, fm1, fm2, fm3, fv1, fv2, fv3, fk1, fk2, fk3
        nonlocal content, run

        if l == 10:
            return

        if not run and position == 0:
            start_timer()

        if event.keysym == 'Escape':
            show_main_menu()
            return

        elif event.keysym == 'Return':
            if position < len(orig) and orig[position] == '\n':
                user += '\n'
                position += 1
                #content = orig[position:]
            else:
                mistakes += 1
                play_sound()

        elif event.keysym == 'space':
            if position < len(orig) and orig[position] == ' ':
                user += ' '
                position += 1
                #content = orig[position:]
            else:
                mistakes += 1
                play_sound()

        elif event.char and event.char != '':
            if position < len(orig) and orig[position] == event.char:
                user += event.char
                position += 1
                #content = orig[position:]
            else:
                mistakes += 1
                play_sound()


        canvas.delete("user")
        canvas.delete("cursor")
        canvas.delete("current_text")
        canvas.delete("end_text")
        canvas.delete("sp")
        canvas.delete('mis')

        if position >= len(orig):

            root.geometry("1000x500")

            if klava == 1:
                try:
                    img_label.place_forget()
                except:
                    pass

            canvas.delete('sta')
            canvas.delete('usert')
            run = False
            canvas.configure(bg = "light blue")
            canvas.delete('rec')
            canvas.delete('sp')
            canvas.delete('mis')


            if seconds > 0 and position > 0:
                speed = position / (seconds / 60)
            else:
                speed = 0

            tk.Button(root, text = "Назад", command = full_text).place(x = 20, y = 20, width = 50, height = 30)

            time_label.place_forget()

            pop1 += 1
            popv1 = (popv1 * (pop1 - 1) + speed) / pop1
            popw1 = (popw1 * (pop1 - 1) + (mistakes * 100) / position) / pop1

            l = 10

            with open(resource_path("stati.txt"), "w") as file:
                file.write(str(pop) + "\n")
                file.write(str(popv) + "\n")
                file.write(str(popw) + "\n")
                file.write(str(pop1) + "\n")
                file.write(str(popv1) + "\n")
                file.write(str(popw1) + "\n")
                file.write(str(pop2) + "\n")
                file.write(str(popw2) + "\n")
                file.close()

            

            
            canvas.create_text(500, 60, text = f"Время игры: {seconds} сек ({seconds / 60:.2f} мин)", font = ("Arial", 14), fill = "black")

            head = ["", "Текущая игра", "Прошлая игра", "Две игры назад", "Три игры назад", "Среднее"]
            heady = 120
            wid = 150
            stax = 50

            canvas.create_rectangle(stax - 10, heady - 30, stax + len(head) * wid + 10, heady + 160,  fill = "white", outline = "CadetBlue4", width = 2)

            for i, header in enumerate(head):
                x = stax + i * wid + wid // 2
                canvas.create_text(x, heady + 5, text = header, font = ("Arial", 12), fill = "black")

                if i > 0:
                    canvas.create_line(stax + i * wid, heady - 20, stax + i * wid, heady + 140, fill = "CadetBlue3")

            for i in range(4):
                y = heady + 35 + i * 35
                canvas.create_line(stax, y, stax + len(head) * wid, y, fill = "CadetBlue3")

            
            rows = [("Скорость (зн/мин)", f"{speed:.2f}", f"{fv3:.2f}", f"{fv2:.2f}", f"{fv1:.2f}", f"{popv1:.2f}"), 
                    ("Ошибки (%)", f"{(mistakes * 100) / position:.2f}%", f"{fm3:.2f}%", f"{fm2:.2f}%", f"{fm1:.2f}%", f"{popw1:.2f}%"), 
                    ("Кол-во ошибок", str(mistakes), str(fk3), str(fk2), str(fk1), f"{(popw1 * position / 100) if position > 0 else 0:.1f}")]
            

            for row_i, row_d in enumerate(rows):
                row_y = heady + 35 + row_i * 35
                for col_idx, cell in enumerate(row_d):
                    x = stax + col_idx * wid + wid // 2       
                    canvas.create_text(x, row_y + 18, text = cell, font = ("Arial", 11), fill = "black")


            if o == 1:
                tk.Button(root, text = "Заново", command = secR).place(x = 450, y = 350, width = 100, height = 40)
            elif o == 2:
                tk.Button(root, text = "Заново", command = secA).place(x = 450, y = 350, width = 100, height = 40)
            elif o == 3:
                tk.Button(root, text = "Заново", command = secAR).place(x = 450, y = 350, width = 100, height = 40)

            #tk.Button(root, text = "Заново", command = secound).place(x = 450, y = 350, width = 100, height = 40)

            tk.Button(root, text = "В меню", command = show_main_menu).place(x = 450, y = 400, width = 100, height = 40)



            fm1, fm2, fm3, fv1, fv2, fv3, fk1, fk2, fk3 = fm2, fm3, (mistakes * 100) / position, fv2, fv3, speed, fk2, fk3, mistakes

            with open(resource_path("fulll.txt"), "w") as file:
                file.write(str(fm1) + "\n")
                file.write(str(fm2) + "\n")
                file.write(str(fm3) + "\n")
                file.write(str(fv1) + "\n")
                file.write(str(fv2) + "\n")
                file.write(str(fv3) + "\n")
                file.write(str(fk1) + "\n")
                file.write(str(fk2) + "\n")
                file.write(str(fk3) + "\n")
                file.close()

        else:

            canvas.create_text(100, 50, text = user, font = ("Arial", 18), fill = "black", anchor = 'nw', width = 700, tags = 'usert')
            canvas.create_text(850, 60, text = f'v = {(position / seconds):.2f} зн/мин', font = ("Arial", 14), fill = "black", tags = "sp", anchor = 'w')
            #canvas.create_text(900, 90, text = f'кол-во ошибок = {mistakes}', font = ("Arial", 14), fill = "black", tags = "mis")

        return "break"
    

    add_every_second()
    root.bind('<KeyPress>', on_key_press)
    root.focus_set()


#=====================================================================================================================
#=====================================================================================================================
# буквы на английском
def tE():
    global let, useR
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    let = list(set(useR) & set(letters)) # выбор букв, которые выбрал пользователь

    tetris()
#=======================
# выбор букв на русском
def tR():
    global let, useR

    
    letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

    let = list(set(useR) & set(letters)) # выбор из тех букв, которые выбрал пользователь

    tetris()
#=======================

def tetris():
    global canvas, xx, lett, nn, yy, sec, qq, ww, al, let, run, pop2, popw2, pop, popv, popw, pop1, popv1, popw1
    
    clear_window()
    
    canvas = tk.Canvas(root, width = 1000, height = 500, bg = "white")
    canvas.pack()
    canvas.configure(bg = "light blue")
    
    tk.Button(root, text = "Назад", command = show_main_menu).place(x = 20, y = 20, width = 50, height = 30)
    
    
    xx = 0
    lett = ''
    nn = 0
    yy = 0
    sec = 0
    qq = 0
    ww = 0
    al = []
    run = True
    
    # игровая статистика
    canvas.create_text(920, 50, text = f'Счет: {nn}', font = ("Arial", 14), fill = "black", tags = "score")
    canvas.create_text(920, 70, text = f'Время: {sec}c.', font=("Arial", 14), fill="black", tags = "timer")
    canvas.create_text(920, 110, text = f'Скорость: 0.0 зн/с.', font = ("Arial", 14), fill = "black", tags = "speed")
    
    # создание буквы
    def spawn_letter():
        global ww, al, let, run
        
        lett = random.choice(let)
        xx = random.randint(100, 800)
        yy = 50
        
        # уникальный тег
        tag = f"letter_{ww}"
        ww += 1
        
        canvas.create_text(xx, yy, text = lett, font = ("Arial", 20), fill = "black", tags = tag)

        # каждая буква - словарь с тегом, символом и координатами
        al.append({'tag': tag, 'lett': lett, 'xx': xx, 'yy': yy})
        
        canvas.delete("letter")
        canvas.create_text(900, 90, text = f'Букв на экране: {len(al)}', font = ("Arial", 14), fill = "black", tags = "letter")
    
    # двигает все буквы вниз
    def move_letters():
        global al, run, pop2, popw2, pop, popv, popw, pop1, popv1, popw1

        if run == False:
            return
        
        ga = False # отслеживание проигрыша
        
        for info in al:
            # буква двигается вниз
            info['yy'] += 3
            
            # изменение координат
            canvas.coords(info['tag'], info['xx'], info['yy'])
            
            # условик конца игры
            if info['yy'] > 480:
                run = False
                ga = True
        
        if ga:
            end_game()
            return
        
        # движение каждые 30 миллисекунд
        root.after(30, move_letters)##########################################################################################################################################
    
    # секундомер
    def timer():
        global sec, qq, run

        if run == False:
            return
        
        sec += 1
        qq += 1
        
        canvas.delete("timer")
        canvas.create_text(920, 70, text = f'Время: {sec}c', font = ("Arial", 14), fill = "black", tags = "timer")
        
        canvas.delete("speed")
        speed = nn / max(sec, 1)
        
        # каждые 5 секунд создается новая буква
        if qq >= 5:
            spawn_letter()
            qq = 0
        
        root.after(1000, timer)#################################################################################################################################################
    
    def on_key_press(event):
        global nn, al, run

        if run == False:
            return


        if event.char:
            # если буква есть в словаре
            for i, info in enumerate(al):
                if event.char and event.char.lower() == info['lett']:
                    # если это нужная буква


                    canvas.delete(info['tag']) # удаляет букву с конца
                    
                    al.pop(i) # удадяет  букву из списка
                    nn += 1 # увеличивает счет

                    spawn_letter() # создаем новую букву
                    
                    canvas.delete("score")
                    canvas.create_text(920, 50, text=f'Счет: {nn}', font = ("Arial", 14), fill = "black", tags = "score")
                    
                    canvas.delete("letter")
                    canvas.create_text(920, 90, text = f'Букв на экране: {len(al)}', font = ("Arial", 14), fill = "black", tags = "letter")

                    break
        
    
    def end_game():
        global pop2, popw2

        clear_window()

        canvas = tk.Canvas(root, width = 1000, height = 500, bg = "white")
        canvas.pack()

        canvas.configure(bg = "light blue")

        canvas.delete("all")

        tk.Button(root, text = "Заново", command = tetris).place(x = 450, y = 350, width = 100, height = 40)
        tk.Button(root, text = "В меню", command = show_main_menu).place(x = 450, y = 400, width = 100, height = 40)

        tk.Button(root, text = "Назад", command = tet).place(x = 20, y = 20, width = 50, height = 30)

        # Параметры таблицы
        head = ["", "Текущая игра", "Среднее"]
        heady = 120
        wid = 200
        table_width = len(head) * wid
        stax = (1000 - table_width) // 2
        table_height = 100

        canvas.create_rectangle(stax - 10, heady - 30, stax + table_width + 10, heady + table_height + 20, fill = "white", outline = "CadetBlue4", width = 2)

        # Заголовки таблицы
        for i, header in enumerate(head):
            x = stax + i * wid + wid // 2
            canvas.create_text(x, heady + 5, text = header, font = ("Arial", 12), fill = "black")

            if i > 0:
                canvas.create_line(stax + i * wid, heady - 20, stax + i * wid, heady + table_height + 5, fill = "CadetBlue3")

        # Горизонтальные линии
        canvas.create_line(stax, heady + 35, stax + table_width, heady + 35, fill = "CadetBlue3")
        canvas.create_line(stax, heady + 70, stax + table_width, heady + 70, fill = "CadetBlue3")
        canvas.create_line(stax, heady + 105, stax + table_width, heady + 105, fill = "CadetBlue3")

        # Данные для таблицы
        rows = [("Счет", str(nn), f"{pop2:.1f}"),
                ("Время (сек)", str(sec), f"{popw2:.1f}")]
        

        for row_i, row_d in enumerate(rows):
            row_y = heady + 35 + row_i * 35
            for col_idx, cell in enumerate(row_d):
                x = stax + col_idx * wid + wid // 2       
                canvas.create_text(x, row_y + 18, text = cell, font = ("Arial", 11), fill = "black")

        # Обновление статистики
        pop2 += 1 

        if pop2 == 1:
            popw2 = sec
        else:
            popw2 = (popw2 * (pop2 - 1) + sec) / pop2

        with open(resource_path("stati.txt"), "w") as file:
                file.write(str(pop) + "\n")
                file.write(str(popv) + "\n")
                file.write(str(popw) + "\n")
                file.write(str(pop1) + "\n")
                file.write(str(popv1) + "\n")
                file.write(str(popw1) + "\n")
                file.write(str(pop2) + "\n")
                file.write(str(popw2) + "\n")
                file.close()
    

    spawn_letter()
    move_letters()
    timer()
    
    root.bind('<KeyPress>', on_key_press)
    root.focus_set()

#=====================================================================================================================

def window1():
    clear_window()
    tk.Button(root, text = "Назад", command = show_main_menu).place(x = 20, y = 20, width = 50, height = 30)

def window2():
    clear_window()
    tk.Button(root, text = "Назад", command = show_main_menu).place(x = 20, y = 20, width = 50, height = 30)

def window3():
    clear_window()
    tk.Button(root, text = "Назад", command = show_main_menu).place(x = 20, y = 20, width = 50, height = 30)

def window4():
    clear_window()
    tk.Button(root, text = "Назад", command = show_main_menu).place(x = 20, y = 20, width = 50, height = 30)

# статистика текста в одну строчку
def sta():
    global canvas, pop, popv, popw
    clear_window()
    tk.Button(root, text = "В меню", command = one_text).place(x = 20, y = 20, width = 50, height = 30)

    tk.Label(root, text = f'количество напечатанных текстов: {pop}',  font = ("Arial", 20), bg = "light blue").place(x = 50, y = 100)
    tk.Label(root, text = f'cредняя скорость печати: {popv:.2f} зн/м',  font = ("Arial", 20), bg = "light blue").place(x = 50, y = 150)
    tk.Label(root, text = f'cредний процент ошибок: {popw:.2f}%',  font = ("Arial", 20), bg = "light blue").place(x = 50, y = 200)

# статистика текста в одну строчку
def stat():
    global canvas, pop1, popv1, popw1
    clear_window()
    tk.Button(root, text = "Назад", command = full_text).place(x = 20, y = 20, width = 50, height = 30)

    tk.Label(root, text = f'количество напечатанных текстов: {pop1}',  font = ("Arial", 20), bg = "light blue").place(x = 50, y = 100)
    tk.Label(root, text = f'cредняя скорость печати: {popv1:.2f} зн/м',  font = ("Arial", 20), bg = "light blue").place(x = 50, y = 150)
    tk.Label(root, text = f'cредний процент ошибок: {popw1:.2f}%',  font = ("Arial", 20), bg = "light blue").place(x = 50, y = 200)

# статистика тетриса
def stati():
    global canvas, pop2, popw2
    clear_window()

    tk.Button(root, text = "Назад", command = tet).place(x = 20, y = 20, width = 50, height = 30)

    tk.Label(root, text = f'количество игр: {pop2}',  font = ("Arial", 20), bg = "light blue").place(x = 50, y = 100)
    tk.Label(root, text = f'среднее время игры: {popw2:.2f} сек',  font = ("Arial", 20), bg = "light blue").place(x = 50, y = 150)

# общая статистика
def statt():
    global canvas, pop1, popv1, popw1, pop, popv, popw
    clear_window()
    tk.Button(root, text = "Назад", command = show_main_menu).place(x = 20, y = 20, width = 50, height = 30)

    tk.Label(root, text = f'количество напечатанных текстов: {(pop1 + pop)}',  font = ("Arial", 20), bg = "light blue").place(x = 50, y = 100)

    if popv == 0:
        tk.Label(root, text = f'cредняя скорость печати: {popv1:.2f} зн/м',  font = ("Arial", 20), bg = "light blue").place(x = 50, y = 150)
    elif popv1 == 0:
        tk.Label(root, text = f'cредняя скорость печати: {popv:.2f} зн/м',  font = ("Arial", 20), bg = "light blue").place(x = 50, y = 150)
    else:
        tk.Label(root, text = f'cредняя скорость печати: {(popv1 + popv) / 2:.2f} зн/м',  font = ("Arial", 20), bg = "light blue").place(x = 50, y = 150)

    if popw == 0:
        tk.Label(root, text = f'cреднее количество ошибок: {popw1:.2f}',  font = ("Arial", 20), bg = "light blue").place(x = 50, y = 200)
    elif popw1 == 0:
        tk.Label(root, text = f'cреднее количество ошибок: {popw:.2f}',  font = ("Arial", 20), bg = "light blue").place(x = 50, y = 200)
    else:
        tk.Label(root, text = f'cредней процент ошибок: {(popw1 + popw) / 2:.2f}%',  font = ("Arial", 20), bg = "light blue").place(x = 50, y = 200)

# отчистка статистики
def bye():
    global pop1, popv1, popw1, pop, popv, popw, pop2, popw2, om1, om2, om3, ov1, ov2, ov3, ok1, ok2, ok3, fm1, fm2, fm3, fv1, fv2, fv3, fk1, fk2, fk3

    pop1, popv1, popw1, pop, popv, popw, pop2, popw2 = 0, 0, 0, 0, 0, 0, 0, 0
    om1, om2, om3, ov1, ov2, ov3, ok1, ok2, ok3 = 0, 0, 0, 0, 0, 0, 0, 0, 0
    fm1, fm2, fm3, fv1, fv2, fv3, fk1, fk2, fk3 = 0, 0, 0, 0, 0, 0, 0, 0, 0
    

    with open(resource_path("stati.txt"), "w") as file:
        file.write(str(pop) + "\n")
        file.write(str(popv) + "\n")
        file.write(str(popw) + "\n")
        file.write(str(pop1) + "\n")
        file.write(str(popv1) + "\n")
        file.write(str(popw1) + "\n")
        file.write(str(pop2) + "\n")
        file.write(str(popw2) + "\n")
        file.close()

    with open(resource_path("onee.txt"), "w") as file:
        file.write(str(om1) + "\n")
        file.write(str(om2) + "\n")
        file.write(str(om3) + "\n")
        file.write(str(ov1) + "\n")
        file.write(str(ov2) + "\n")
        file.write(str(ov3) + "\n")
        file.write(str(ok1) + "\n")
        file.write(str(ok2) + "\n")
        file.write(str(ok3) + "\n")
        file.close()

    with open(resource_path("fulll.txt"), "w") as file:
        file.write(str(fm1) + "\n")
        file.write(str(fm2) + "\n")
        file.write(str(fm3) + "\n")
        file.write(str(fv1) + "\n")
        file.write(str(fv2) + "\n")
        file.write(str(fv3) + "\n")
        file.write(str(fk1) + "\n")
        file.write(str(fk2) + "\n")
        file.write(str(fk3) + "\n")
        file.close()

#==============================================================================================================================================================



root = tk.Tk()
root.geometry("1000x500")
show_main_menu()
root.mainloop()