print("Converting Images from PNG to JPG")

import sys
import os
from PIL import Image

path = "D:\CIRO (Estudos Compactados)\CENTENNIAL\CENTENNIAL (ENERGY ENGINEERING)\Matérias\Python\Projects\Image Processing\Images"
new_extension="png"
old_extension="jpg"

for filename in os.listdir(path): #Loop inside the files in the folder
  clean_name = os.path.splitext(filename)[0] #The figure can just be converted from PNG to JPG if it is separated from the extension
  # Otherwise the img.save is not going to work since the filename is going to be jpg.png
  #The (filename)[0] gets the first item of the text tuple, which is the filename without the extension
  os.chdir(path)
  img=Image.open(f'{path}\{filename}')
  #added the / in case user doesn't enter it. You may want to check for this and add or remover it. 
  if new_extension=="png":
  	img.save(f'{clean_name}.'+new_extension, new_extension) #CREATE NEW EXTENSION FILES
  	os.remove(f'{clean_name}.'+old_extension) #REMOVE OLD EXTENSION FILES
  elif new_extension=="jpg":
  	img.save(f'{clean_name}.'+new_extension, old_extension) #CREATE NEW EXTENSION FILES
  	os.remove(f'{clean_name}.'+old_extension)  #REMOVE OLD EXTENSION FILES
  print('all done!')