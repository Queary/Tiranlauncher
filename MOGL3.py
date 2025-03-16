import requests
from tqdm import tqdm
from urllib.parse import urlencode
import patoolib
import os
import shutil
import subprocess
from tqdm import tqdm
import sys

def Delete(title):
    os.remove(title)

def DownMods(s=1):
    print("библиотеки загружены")
    f = 1
    md = "TMOGL"
    df = "downloaded_file.zip"
    #mi = 26


    def sizeof_fmt(num: int | float) -> str:
        for x in ['bytes', 'KB', 'MB', 'GB']:
            if num < 1024.0:
                return "%.1f %s" % (num, x)

            num /= 1024.0

        return "%.1f %s" % (num, 'TB')
    print("получил ссылки")
    base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
    if s == 1:
        public_key = 'https://disk.yandex.ru/d/9c8-tFh7olg70A'
    elif s==2:
        public_key = 'https://disk.yandex.ru/d/moBWIvZsbSnXdg'
    elif s==3:
        public_key = 'https://disk.yandex.ru/d/xs7gTME_ilOvrg'
    print("connect")
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
    print("начинается скачивание")
    if(f == 1):print("113Mб")
    with open("downloaded_file.zip", mode='wb') as f:
        for data in tqdm(rs.iter_content(chunk_size), total=num_bars, unit='Kb', file=sys.stdout):
            
            f.write(data)
    #file_data = open(rs, mode='rb').read()

    print("скачивание закончилось")
    #"""
    #перед этим удаление старых загрузок
    if(os.path.isdir(md)):
       print("файл есть "+str(md))
       shutil.rmtree(md)
       print("файл удален "+str(md))
    else:
        print("файл не найден "+md)
    #перед этим удаление mods
    if(os.path.isdir("mods")):
        print("файл найден mods")
        try:
            shutil.rmtree("mods")
            print("файл mods удален")
        except:
            print("файл mods не удален")
            print("возможно не достаточно прав")
            print("включите прогу от имени админа")
            print("или удалите папку вручную")
            print("перезапустите программу самостоятельно")
            EX = input()

    '''
    if(os.path.isdir(mf)):
       print("файл есть "+str(mf))
       shutil.rmtree(mf)
       print("файл удален "+str(mf))
    else:
        print("файл не найден "+mf)
    '''
    #разархивация
    patoolib.extract_archive(df, outdir="./")
    print("файл разархивирован "+df)
    #удаление rar
    try:
        os.remove(df) #shutil.rmtree(df)(old)
        print("файл rar удален "+df)
    except:
        print("не удалось удалить файл "+df)
        EX = input()
    #переменование
    print("переменовываю")
    os.rename(md,"mods")
    #показать конец
    print("нажмите enter чтобы закрыть программу щегла")
    #EX = input()
