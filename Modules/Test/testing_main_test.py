import unittest
import MAIN_TEST
import os

#######################################
#Unittest documentation: https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
#Unittest video: https://www.youtube.com/watch?v=6tNS--WetLI
#######################################

#######################################
#Get files in other directory
print(os.getcwd()) #Get current directory
print("BOTH FILES: TESTING AND MAIN FILE ARE EXPECTED TO BE IN THE SAME FOLDER")
# os.chdir("D:\CIRO (Estudos Compactados)\CENTENNIAL\CENTENNIAL (ENERGY ENGINEERING)\Matérias\Python\Projects\Modules\Test") #Change the directory
# print(os.getcwd()) #Get current directory

######################################



class Testmain(unittest.TestCase):
    def test_input(self): #ALL FUNCTIONS SHOULD START WITH THE NAME TEST
        guess=5
        answer=5
        result1=MAIN_TEST.guessing(guess,answer)
        self.assertTrue(result1)

    def test_input1(self): #ALL FUNCTIONS SHOULD START WITH THE NAME TEST
        guess=5
        answer=3
        result1=MAIN_TEST.guessing(guess,answer)
        self.assertFalse(result1)

    def test_input2(self): #ALL FUNCTIONS SHOULD START WITH THE NAME TEST
        guess=11
        answer=5
        result1=MAIN_TEST.guessing(guess,answer)
        self.assertEqual(result1,None) #IN THE MAIN_FUNCTION IT IS GOING TO APPEAR HEY BOZO..., BUT PRINT IS NOT RETURN,WHAT IS REALLY RETURNING IS NONE


if __name__=="__main__":
	unittest.main()



        # test_param = 10  # This variable has to match the one in the main file
        # result = Hypothetical_Main_file.mainfunction(test_param)  # The result of the test is being
        # # validated with the one from the main file
        # self.assertEqual(result, 10)  # The validation is made here by comparing the
        # # result of this file with the actual answer (10+5) equals 15


unittest.main()
# If it is okay, it means the programming is code
# If it is bad it is foinf to appear False
