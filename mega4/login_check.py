from tkinter import *
from tkinter.messagebox import *


def login():
    id = id_entry.get()
    pw = pw_entry.get()
    if id == 'root' and pw == '1234':
        showinfo('내용 확인', '로그인 성공')
    else:
        showinfo('내용 확인', '로그인 실패')


def reset():
    id_entry.delete(0, "end")
    pw_entry.delete(0, "end")


w = Tk()
w.geometry('500x300')

id_label = Label(w, text='id', font='굴림, 36', width=5)
pw_label = Label(w, text='pw', font='굴림, 36', width=5)

id_entry = Entry(w, font='굴림, 36', width=7)
pw_entry = Entry(w, font='굴림, 36', width=7)

button = Button(w, text='로그인', font='굴림, 36', width=7, command=login)
clear = Button(w, text='초기화', font='굴림, 36', width=7, command=reset)

id_label.grid(row=0, column=0)
id_entry.grid(row=0, column=1)
pw_label.grid(row=1, column=0)
pw_entry.grid(row=1, column=1)
button.grid(row=2, column=0)
clear.grid(row=2, column=1)


w.mainloop()