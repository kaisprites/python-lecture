from pythoncode.python08.mysql_db import *
from pythoncode.pack01.scrapper import crawl
from tkinter import *
from tkinter import messagebox


def service_search():
    code = code_entry.get()
    find = ['h2 a', 'p.no_today em span.blind', 'span.sp_txt4+em span.blind', 'span.sp_txt5+em span.blind']
    result = crawl(f'https://finance.naver.com/item/main.nhn?code={code}', find)
    name_entry.delete(0, 'end')
    now_entry.delete(0, 'end')
    high_entry.delete(0, 'end')
    low_entry.delete(0, 'end')
    name_entry.insert(0, result[0])
    now_entry.insert(0, result[1])
    high_entry.insert(0, result[2])
    low_entry.insert(0, result[3])
    print(result)


def service_create():
    code = code_entry.get()
    name = name_entry.get()
    now = now_entry.get().replace(',','')
    high = high_entry.get().replace(',','')
    low = low_entry.get().replace(',','')
    if code == '' or name == '' or now == '' or high == '' or low == '':
        messagebox.showinfo('내용 확인', '입력되지 않은 값 있음')
        return
    check = len(read(code))
    if check == 1:
        update(code, name, int(now), int(high), int(low))
    else:
        create(code, name, int(now), int(high), int(low))


def service_read():
    code = code_entry.get()
    result = read(code)
    if len(result) == 0:
        messagebox.showinfo('내용 확인', '등록되지 않은 레코드')
        return
    name_entry.delete(0, 'end')
    now_entry.delete(0, 'end')
    high_entry.delete(0, 'end')
    low_entry.delete(0, 'end')
    name_entry.insert(0, result[0][1])
    now_entry.insert(0, result[0][2])
    high_entry.insert(0, result[0][3])
    low_entry.insert(0, result[0][4])


def service_delete():
    code = code_entry.get()
    if len(read(code)) == 0:
        messagebox.showinfo('내용 확인', '등록되지 않은 레코드')
        return
    delete(code)
    name_entry.delete(0, 'end')
    now_entry.delete(0, 'end')
    high_entry.delete(0, 'end')
    low_entry.delete(0, 'end')


def clear():
    code_entry.delete(0, 'end')
    name_entry.delete(0, 'end')
    now_entry.delete(0, 'end')
    high_entry.delete(0, 'end')
    low_entry.delete(0, 'end')


if __name__ == '__main__':
    w = Tk()
    w.geometry('500x500')

    code_label = Label(w, text='코드', font=('바탕', 30))
    name_label = Label(w, text='이름', font=('바탕', 30))
    now_label = Label(w, text='현재가', font=('바탕', 30))
    high_label = Label(w, text='최고가', font=('바탕', 30))
    low_label = Label(w, text='최저가', font=('바탕', 30))

    code_entry = Entry(w, font=('바탕', 30))
    name_entry = Entry(w, font=('바탕', 30))
    now_entry = Entry(w, font=('바탕', 30))
    high_entry = Entry(w, font=('바탕', 30))
    low_entry = Entry(w, font=('바탕', 30))

    code_label.grid(row=0, column=0)
    name_label.grid(row=1, column=0)
    now_label.grid(row=2, column=0)
    high_label.grid(row=3, column=0)
    low_label.grid(row=4, column=0)

    code_entry.grid(row=0, column=1)
    name_entry.grid(row=1, column=1)
    now_entry.grid(row=2, column=1)
    high_entry.grid(row=3, column=1)
    low_entry.grid(row=4, column=1)

    search_button = Button(w, text='search', command=service_search, width=50)
    create_button = Button(w, text='create/update', command=service_create, width=50)
    read_button = Button(w, text='read', command=service_read, width=50)
    delete_button = Button(w, text='delete', command=service_delete, width=50)
    clear_button = Button(w, text='clear', command=clear, width=50)

    search_button.grid(row=5, column=0, columnspan=2)
    create_button.grid(row=6, column=0, columnspan=2)
    read_button.grid(row=7, column=0, columnspan=2)
    delete_button.grid(row=8, column=0, columnspan=2)
    clear_button.grid(row=9, column=0, columnspan=2)

    w.mainloop()
