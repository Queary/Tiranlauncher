import requests
import minecraft_launcher_lib
import subprocess
import os
from tqdm import tqdm
import sys
import shutil
from urllib.parse import urlencode
import patoolib

#проверить с установкой и сразу запуском лаунчера

status = 0
nick   = ""
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
options ={
    'username':"Test",
}


print("run main.py")
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
if minecraft_launcher_lib.utils.get_installed_versions(path) == []:
    print("не установлена")
    print("запуск установщика")
    minecraft_launcher_lib.forge.install_forge_version("1.12.2-14.23.5.2859",path, callback=callback_setup)
    print("установка завершена")
else:
    print("установлена")

print("скачиваем MOGL3_UPD")
print("активация с main.py")
import requests
from urllib.parse import urlencode
base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
public_key = 'https://disk.yandex.ru/d/xs7gTME_ilOvrg'
final_url = base_url + urlencode(dict(public_key=public_key))
response = requests.get(final_url)
download_url = response.json()['href']
rs = requests.get(download_url, stream=True)
# Total size in bytes.
total_size = int(rs.headers.get('content-length', 0))
#print('From content-length:', sizeof_fmt(total_size))
print("обработка ссылок и их файлов к загрузке")
chunk_size = 1024
print(str(total_size) + " total size")
num_bars = int(total_size / chunk_size)
print(str(num_bars) + " num_bars")
file_name = os.path.basename("downloaded_file.zip")
#file_data = open(file_name, mode='rb').read()
#print('/', sizeof_fmt(len(file_data)))
print(os.getenv('APPDATA')+"\\.A")
print("113Mб")
with open(os.getenv('APPDATA')+ "\\.A\\downloaded_file.zip", mode='wb') as f:
    for data in tqdm(rs.iter_content(chunk_size), total=num_bars, unit='Kb', file=sys.stdout):
        f.write(data)
print("MOGL3_UPD скачен")
print("MOGL3_UPD распаковываем")
patoolib.extract_archive(os.getenv('APPDATA')+ "\\.A\\downloaded_file.zip", outdir=os.getenv('APPDATA')+ "\\.A\\")
print("удаляем лишнее с временных разгрузок")
os.remove(os.getenv('APPDATA')+ "\\.A\\downloaded_file.zip")
print("поиск подуля MOGL3_UPD")

ppp = os.getenv('APPDATA')+".A\\MOGL3"

print("MOGL3VFT")
print(os.getenv('APPDATA')+".\\A\\")

#sys.path.append(os.getenv('APPDATA')+".A\\")#первый
sys.path.insert(1, os.getenv('APPDATA')+".A\\") #второй
import MOGL3VFT
print("запуск MOGL3_UPD")
MOGL3.DownMods(2)
MOGL3.Delete("__pycache__")

#print("запускаем лаунчер")
'''
import MOGL3
MOGL3.DownMods(2)
MOGL3.Delete("__pycache__")'''
#print(minecraft_launcher_lib.forge.is_forge_version_valid("1.12.2-14.23.5.2859"))
#subprocess.call(gmc(version="1.12.2-forge-14.23.5.2859", minecraft_directory=mine_path, options=options))
#запуск лаунча
#subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version="1.12.2-forge-14.23.5.2859", minecraft_directory=path, options=options))
