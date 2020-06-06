import os
os.chdir("D:\CIRO (Estudos Compactados)\CENTENNIAL\CENTENNIAL (ENERGY ENGINEERING)\Matérias\Python")
print(os.getcwd())

with open("demo.txt",mode="a") as my_file: #Just set the path and put another file name - It will create automatically
    text = my_file.write("\nThis is a new file")
    print(text)