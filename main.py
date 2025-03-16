import requests
import minecraft_launcher_lib
import subprocess
import os
from tqdm import tqdm
import sys
import shutil
from urllib.parse import urlencode
import patoolib
import json

#START MAIN
import Interface

#переделать MOGL на аргумент ссылки
#0.3 save nick + upd programs
#0.3.1 убрать пустой ввод сделать предупреждение + убрать nick с setting.json
#0.3.2
#0.3.3 убрать load.json если выбор no(а то остается)
#0.3.5 убрать папку LOAD - это баг или фича ?
#может перед удалением f.close()  использовать
#0.4 переделать MOGL на аргумент ссылки + ещё что не будь чтобы бы видно работу + отображать версию
#0.5 при недостоющих файлов png(скачать)или без них,setting.json(создать) чтобы приложение могло запускаться при любых случаях


#проверить с установкой и сразу запуском лаунчера"
#сделать полную проверку модов перед скачиванием
#Setup(rar) который будет устанавливать main...
#после открытые майна скрывать или закрытвать прогу
#отображение версии

#берём setting
setting = json.load(open("setting.json","r"))

status = 0
nick   = setting["nick"]
mll    = minecraft_launcher_lib
mine_path = ""
gmc    = minecraft_launcher_lib.command.get_minecraft_command
#version="1.12.2-forge-14.23.5.2859"
callback = {
        "setStatus": lambda text: print(text, end='r'),
        "setProgress": lambda value: printProgressBar(value, max_value[0]),
        "setMax": lambda value: maximum(max_value, value)
}
callback_setup = {
    "setStatus": lambda text: print(text)
}




def start(nick):
    print("run main.py")
    options ={
        'username':nick,
    }
    data = {"nick":nick}
    with open('nick.json', 'w') as file:
        json.dump(data, file, indent=3)
    status = 1
    print("запуск программы")
    print('░█████╗░░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗███╗░░██╗░█████╗░██╗░░██╗███████╗██████╗░░')
    print('██║░░░██╗██╔═══╝░██║░░░░░██╔══██╗██║░░░██║████╗░██║██╔══██╗██║░░██║██╔════╝██╔══██╗░')
    print('██║░░░██║██║░░░░░██║░░░░░███████║██║░░░██║██╔██╗██║██║░░╚═╝███████║█████╗░░██████╔╝░')
    print('██║░░░██║██║░░██╗██║░░░░░██╔══██║██║░░░██║██║╚████║██║░░██╗██╔══██║██╔══╝░░██╔══██╗░')
    print('╚██████╔╝╚█████╔╝███████╗██║░░██║╚██████╔╝██║░╚███║╚█████╔╝██║░░██║███████╗██║░░██║░')
    print('░╚═════╝░░╚════╝░╚══════╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░')
    print('made by: Tiran')
    path = minecraft_launcher_lib.utils.get_minecraft_directory().replace('minecraft', 'A')
    print("установлена ли версия 1.12.2-14.23.5.2859")
    #for version in ....:version[id]
    if(os.path.exists("versions\\1.12.2-forge-14.23.5.2859") == False):
        print("не установлена")
        print("запуск установщика")
        minecraft_launcher_lib.forge.install_forge_version("1.12.2-14.23.5.2859",path, callback=callback_setup)
        print("установка завершена")
    else:
        print("установлена")

    print("поиск подуля MOGL3_UPD")
    print("активация MOGL3_UPD с main.py")
    print("проверка модов")
    #проверка модов
    if(os.path.exists("mods\\appliedenergistics2-rv6-stable-7.jar") == False):
        print("скачиваем моды")
        import MOGL3
        MOGL3.DownMods(2) #2-тест 1-полная
        print("удаляем __pycache__")
        try:
            MOGL3.Delete("__pycache__")
            print("удалил __pycache__")
        except:
            print("не удалил __pycache__")
    else:
        print("mods установлен")

    #print("запускаем лаунчер")
    '''
    import MOGL3
    MOGL3.DownMods(2)
    MOGL3.Delete("__pycache__")'''
    #print(minecraft_launcher_lib.forge.is_forge_version_valid("1.12.2-14.23.5.2859"))
    #subprocess.call(gmc(version="1.12.2-forge-14.23.5.2859", minecraft_directory=mine_path, options=options))
    #запуск лаунча
    print("запускаем лаунчер")
    subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version="1.12.2-forge-14.23.5.2859", minecraft_directory=path, options=options))
