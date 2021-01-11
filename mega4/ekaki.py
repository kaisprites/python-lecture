from tkinter import *
from tkinter.messagebox import *


def check():
    get_id = id_text.get()
    get_pw = pw_text.get()
    if get_id == 'root' and get_pw == '1234':
        showinfo('내용 확인', '로그인 성공')
    else:
        showinfo('내용 확인', '로그인 실패')


def check2():
    get_id = id_text.get()
    get_pw = pw_text.get()
    if get_id == get_pw:
        showinfo('내용 확인', '같은 값')
    else:
        showinfo('내용 확인', '다른 값')


w = Tk()
w.geometry("500x400")

id_label = Label(w, text="사용자ID입력", font='궁서, 30', bg='lime', fg='blue')
id_text = Entry(w, font='궁서, 30', bg='yellow', fg='red')
pw_label = Label(w, text="사용자PW입력", font='궁서, 30', bg='lime', fg='blue')
pw_text = Entry(w, font='궁서, 30', bg='yellow', fg='red')
button = Button(w, text='로그인처리', font='궁서, 30', bg='lime', fg='black', command=check)
button2 = Button(w, text='동일값?', font='궁서, 30', bg='lime', fg='black', command=check2)

id_label.pack()
id_text.pack()
pw_label.pack()
pw_text.pack()
button.pack()
button2.pack()

w.mainloop()