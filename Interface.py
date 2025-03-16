from tkinter import *
from tkinter import ttk



#design:cxJealousy
#developer:Kingdom_Tiran

#сделать его более правильныйм

#выход -> ХУЙ

def sxc():
    import main
    main.start(ent.get())
    #return ent.get()

root = Tk()
root.title("Щегол Лаунчер")
root.geometry("640x480")
root.resizable(False, False)
#root.bg="white"
icon = PhotoImage(file = "shegol.png")#ico
#.grid(column=0, row=0)
Label(root, text="Server OGENH").pack()
Label(root, text="Ваш казуальный ник").pack()
img = PhotoImage(file='Pen2.png')
Label(root, text="",image=img,height=150,width=100).place(x=530-15, y=300)
ent = ttk.Entry()
ent.pack()
Button(text="Запуск чертолета)", command=sxc).pack()
Label(root, text="developer:Kingdom_Tiran").place(x=15, y=450)
Label(root, text="design:cxJealousy").place(x=530-15, y=450)
root.iconphoto(False, icon)
Label(root, text="полная установка займет минут 5-30 все зависит от вашего интернета)").pack()
Label(root, text="первый запуск долгкий последующие быстрей)").pack()
root.mainloop()
