from tkinter import *


def fileout():
    date = entry1.get().replace('\n', '')
    title = entry2.get().replace('\n', '')
    content = entry3.get().replace('\n', '')
    f = open("fileio.txt", 'w')
    f.write(f"{date}\n{title}\n{content}\n")
    f.close()


def filein():
    f = open("fileio.txt", 'r')
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    data = f.readlines()
    print(data)
    entry1.insert(0, data[0])
    entry2.insert(0, data[1])
    entry3.insert(0, data[2])
    f.close()


w = Tk()
w.geometry('500x500')

label1 = Label(w, text='날짜', font=('궁서', 36))
label2 = Label(w, text='제목', font=('궁서', 36))
label3 = Label(w, text='내용', font=('궁서', 36))

entry1 = Entry(w, font=('궁서', 36))
entry2 = Entry(w, font=('궁서', 36))
entry3 = Entry(w, font=('궁서', 36))

button1 = Button(w, text='파일로 저장', font=('궁서', 36), command=fileout)
button2 = Button(w, text='파일로 읽기', font=('궁서', 36), command=filein)

label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
label3.pack()
entry3.pack()
button1.pack()
button2.pack()

w.mainloop()