
# import os
# from PIL import Image

# # Zdefiniuj ścieżkę do katalogu z plikami SVG
# Path = "G:/Image Dodnoldos/logo/svg/"

# # Przejdź przez wszystkie pliki w katalogu
# for plik in os.listdir(Path):
#   # Jeśli plik jest plikiem SVG
#   if plik.endswith(".svg"):
#     # Otwórz plik SVG za pomocą biblioteki Pillow
#     im = Image.open(os.path.join(Path, plik))

#     # Pobierz nazwę pliku bez rozszerzenia
#     nazwa_pliku, rozszerzenie = os.path.splitext(plik)

#     # Zapisz plik jako obraz PNG z oryginalną nazwą pliku i rozszerzeniem .png
#     im.save(os.path.join(Path, nazwa_pliku + ".png"))


# import aspose.words as aw

# # SVG file's path
# fileName = "G:/Image Dodnoldos/logo/svg/"

# # create a document
# doc = aw.Document()

# # create a document builder and initialize it with document object
# builder = aw.DocumentBuilder(doc)

# # insert SVG image to document
# shape = builder.insert_image(fileName)

# # OPTIONAL
# # Calculate the maximum width and height and update page settings 
# # to crop the document to fit the size of the pictures.
# pageSetup = builder.page_setup
# pageSetup.page_width = shape.width
# pageSetup.page_height = shape.height
# pageSetup.top_margin = 0
# pageSetup.left_margin = 0
# pageSetup.bottom_margin = 0
# pageSetup.right_margin = 0

# # save as PNG
# doc.save("svg-to-png.png")



# from wand.api import library
# import wand.color
# import wand.image

# with wand.image.Image() as image:
#     with wand.color.Color('transparent') as background_color:
#         library.MagickSetBackgroundColor(image.wand, 
#                                          background_color.resource) 
#     image.read(blob=svg_file.read(), format="svg")
#     png_image = image.make_blob("png32")

# with open(output_filename, "wb") as out:
#     out.write(png_image)



import os
import cairosvg

# Zdefiniuj ścieżkę do katalogu z plikami SVG
sciezka = "G:/Image Dodnoldos/logo/svg"

# Przejdź przez wszystkie pliki w katalogu
for plik in os.listdir(sciezka):
  # Jeśli plik jest plikiem SVG
  if plik.endswith(".svg"):
    # Renderuj plik SVG do obrazu PNG
    cairosvg.svg2png(url=os.path.join(sciezka, plik), write_to=os.path.join(sciezka, plik.replace(".svg", ".png")))
