print("CHANGING DIRECTORY")

import os
#https://www.youtube.com/watch?v=tJxcKyFMTGo
print("\nOld Directory")
print(os.getcwd()) #Get current directory
os.chdir("D:\CIRO (Estudos Compactados)\CENTENNIAL\CENTENNIAL (ENERGY ENGINEERING)\Matérias\Python")
#The current directory was changed above
print("\nNew Current Directory")
print(os.getcwd()) #Get current directory
# os.mkdir() #Create a first level PASTE
os.makedirs("Test (This paste can be deleted)\Test (This paste can also be deleted)") #Create paste in any level
print("\nChecking everything in the current directory")
print(os.listdir())  #Check what is in the current directory
os.rename("Python_text.txt","Test.txt") #Change the Name of the file
os.rmdir("Test (This paste can be deleted)\Test (This paste can also be deleted)") #Remove paste in any level
os.removedirs("Test (This paste can be deleted)") #Remove EVERYTHING - ALL PASTES

print("\nOPENING A FILE AND READING/WRITING IT - YOU CAN DO BOTH")

with open("Test.txt",mode="r+") as my_file: #Type in mode r+,so you can read and write
    #HOWEVER IF THE FILE HAVE SOMETHING ALREADY WRITTEN YOU SHOULD APPEND
    #READING A FILE
    print(my_file.seek(0))
    print(my_file.read())
    print(my_file.seek(0))

    #WRITING IN A FILE
    text=my_file.write("It\'s a good day today, right?")
    print(text)

with open("Test.txt",mode="a") as my_file: #Type in a file that already has something written on it
    #WRITING IN A FILE THAT HAS SOMETHING WRITTEN ON IT
    text=my_file.write("\nIt\'s a good day today, right?")
    print(text)

print("\nOPENING A FILE AND READING IT")

with open("Test.txt") as my_file: #REMEMBER TO PUT THE FILE EXTENSION (TXT) AND THE FUNCTION MY_FILE
    #This option on the top WITHOUT NEEDING TO CLOSE REQUIRES INDENTATION
# my_file=open('Test.txt') - THIS IS NOT A GOOD WAY TO OPEN THE FILE SINCE YOU HAVE TO CLOSE LATER. IT DOESN'T REQUIRE INDENTATION
    print("\nChecking file information")
    print(my_file)

    print("\nChecking what is inside the file")
    print(my_file.read())

    print("\nIf we try to read again. It doesn't work. Because it is like a cursor, so if you finished reading that is it")
    print(my_file.read())

    print("\nHowever you can read again if you put seek(0) which moves the cursor to the top")
    print(my_file.seek(0))
    print(my_file.read())

    print("\nYou can read line by line")
    print(my_file.seek(0))
    print(my_file.readline())
    print(my_file.readline())
    print(my_file.readline())

    print("\nCreate a list which each element is one line. REMEMBER TOPUT THE CURSOS BACK AT THE BEGINNING SEEK(0)")
    print(my_file.seek(0))
    print(my_file.readlines())

    # my_file.close() #YOU HAVE TO CLOSE THE FILE

os.rename("Test.txt","Python_text.txt")


# print("\n OPENING A FILE AND JUST WRITING IN IT")
# with open("Test.txt",mode="w") as my_fi: #to write type in mode W, read is in default)