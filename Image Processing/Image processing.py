#In order to import the Image Processing Package:
#Open Power Shell
#Go to the directory that tou have ur programming file:
#   cd "FILE PATH"
#Type pip3 install Pillow
#IT HAS TO BE IN SUBLIME
from PIL import Image, ImageFilter
img=Image.open("./Images/pikachu.jpg") #./ => Means current directory

print("Checking Image Characteristics")
print(img) #Shows the size
print(img.format)
print(img.size)
print(img.mode) #RGB => Color RGB => Red, Green, Blue
print(dir(img.mode))

print("Change Image Filter")
filtered_img=img.filter(ImageFilter.BLUR) #Applying Blur to an Image
filtered_img.save("blur.png","png") #Saving the Image with the name blur and changing the file extension to PNG
	
print("Change Image Color or Formats -The one it was before was RGB")
filtered_img=img.convert("L") #Applying Blur to an Image
filtered_img.save("gray.png","png") #Saving the Image with the name blur and changing the file extension to PNG
filtered_img.show()

print("Rotate Image and Gray")
crooked=filtered_img.rotate(90)
crooked.save("rotate.png","png")
crooked.show()

print("Resizing") #Resize can distort the image, so it is better to use thumbnail
resizing=img.resize((300,100))#It has to be a tuple for resizing. That's why there are two brackets 
resizing.save("resize.png","png")
resizing.show()

print("Resizing Properly")
img.thumbnail((300,100)) 
img.save("thumbnailresizing.png","png") #It doesn't return a new image, it just 
img.show()

print("Cropping an Image")
box = (100, 100, 400, 400)
crooped = img.crop(box)
crooped.show()




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

# import sys
# import os
# from PIL import Image

# path = sys.argv[1]
# directory = sys.argv[2]

# if not os.path.exists(directory):
#     os.makedirs(directory)

# for filename in os.listdir(path):
#   clean_name = os.path.splitext(filename)[0]
#   img = Image.open(f'{path}{filename}')
#   #added the / in case user doesn't enter it. You may want to check for this and add or remover it. 
#   img.save(f'{directory}/{clean_name}.png', 'png')
#   print('all done!')