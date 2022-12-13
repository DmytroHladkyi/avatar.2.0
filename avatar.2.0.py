import requests
import random
from pathlib import Path

folder = (input("Podaj jak ma się nazywać folder: "))
nazwa = (input("Podaj jak ma się nazywać plik: "))
nazwa1 = nazwa + ".svg"
plec = input("Wybierz plec postaci: male, female, human, identicon, initials, bottts, avataaars, jdenticon, gridy lub micah: ")

response = requests.get(f'https://avatars.dicebear.com/api/{plec}/{random.random()}.svg')

Path(f'./{folder}').mkdir(exist_ok=True) # stwarza się plik, gdzie będą przechowywać się pliki z linii (with open)
with open (f'./{str(folder)}/{str(nazwa1)}', 'wb') as file: #/avatars/avatar.svg ---zapisujemy i KATALOG i NAZWE PLIKU
 file.write(response.content)