import os
import cairosvg

sciezka = "./logo/svg"


for plik in os.listdir(sciezka):
  if plik.endswith(".svg"):
    cairosvg.svg2png(url=os.path.join(sciezka, plik), write_to=os.path.join(sciezka, plik.replace(".svg", ".png")))
