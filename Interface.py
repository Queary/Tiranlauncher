from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json
import requests
from urllib.parse import urlencode
import patoolib
import os


#design:cxJealousy
#developer:Kingdom_Tiran

#сделать его более правильныйм

#выход -> ХУЙ

def sxc():
    
    if ent.get() != "":
        import main
        main.start(ent.get())
    else:
        messagebox.showinfo("Оповещение", "nick пустой")
    #return ent.get()

#загрузка JSON
setting = json.load(open("setting.json","r"))

#запуск проверки
YN = False
print("проверка на обновление")
version = setting["version"]
print(version)
base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
public_key = setting["S"]
final_url = base_url + urlencode(dict(public_key=public_key))
response = requests.get(final_url)
download_url = response.json()['href']
download_response = requests.get(download_url)
with open('load.json', 'wb') as f:
    f.write(download_response.content)
load = json.load(open("load.json","r"))
#отображает
if setting["version"] != load["version"]:
    print(setting["version"])
    print(">")
    print(load["version"])
    print("Y")
    YN = True
    result = messagebox.askquestion("Обновление", "вышло обновление лаунчера хотите обновиться?")
    print(result)#no #yes
    if result == "yes":
        base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
        public_key = setting["FS"]
        final_url = base_url + urlencode(dict(public_key=public_key))
        response = requests.get(final_url)
        download_url = response.json()['href']
        download_response = requests.get(download_url)
        try:
            os.remove("LOAD.zip")  # удаление старых
        except:
            pass
        with open('LOAD.zip', 'wb') as f:
            f.write(download_response.content)
        f.close()
        patoolib.extract_archive('LOAD.zip', outdir="./")
        os.remove("LOAD.zip")  # удаление новоспечённых
        os.replace("LOAD/Tiranlauncher.exe","Tiranlauncher.exe")
        #os.replace("LOAD/Interface.py","Interface.py")
        os.replace("LOAD/setting.json","setting.json")
        #os.remove("LOAD")  # удаление новоспечённых
        messagebox.showinfo("Оповещение", "Перезапустите программу!")
else:
    print("N")
    try:
        os.remove("load.json")
    except:
        print("delete load.json:error")
    YN = False

root = Tk()
root.title("Щегол Лаунчер5")
root.geometry("640x480")
root.resizable(False, False)
#root.bg="white"
try:    
    icon = PhotoImage(file = "shegol.png")#ico
except:
    print("shehol:error")
#.grid(column=0, row=0)
Label(root, text="Server OGENH").pack()
Label(root, text="Ваш казуальный ник").pack()
if setting["VG"] == 1:
    try:
        img = PhotoImage(file='Pen2.png')
        Label(root, text="", image=img, height=150, width=100).place(x=530 - 15, y=300)
        Label(root, text="design:cxJealousy").place(x=530 - 15, y=450)
    except:
        print("pen2:error")
ent = ttk.Entry()
#забираем ник
try:
    locale_nick = json.load(open("nick.json","r"))
    ent.insert(0,locale_nick["nick"])
    ent.pack()
except:
    ent.pack()
Button(text="Запуск чертолета)", command=sxc).pack()
Label(root, text="developer:Kingdom_Tiran").place(x=15, y=450)
try:
    root.iconphoto(False, icon)
except:
    print("icon_add:error")
Label(root, text="полная установка займет минут 5-30 все зависит от вашего интернета)").pack()
Label(root, text="первый запуск долгкий последующие быстрей)").pack()
root.mainloop()
