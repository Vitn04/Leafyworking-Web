import eel  # библиотека для вывода html страницы в окно приложения
import os # библиотека для отчистки консоли
import sys # библиотека системы

try:
    os.system("cls") # отчистка консоли
    print("\033[32m {}" .format("Браузер Chrome - Присуцтвует! Успешный запуск программы!"))
    eel.init("web")  # выбор папки с файлом html-страницы
    eel.start("1st.html", mode="chrome", size=(1100,900))  # выбор файла на открытие в программе 
    sys.exit()
    

except FileNotFoundError:
    os.system("cls") # отчистка консоли
    print("\033[33m {}" .format("Браузер Chrome - Отсуцтвует! Запуск Web-версии в Браузере по умолчанию."))
    eel.init("web")  # выбор папки с файлом html-страницы
    eel.start("1st.html", mode="default", size=(1100,900))  # выбор файла на открытие в программе (при отсуцтвии Браузера Chrome)
    
finally:
    print("\033[0m {}" .format("Конец программы!"))
    sys.exit()                        