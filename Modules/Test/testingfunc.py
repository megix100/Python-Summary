import unittest
import Test
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

    def test_add(self): #ALL FUNCTIONS SHOULD START WITH THE NAME TEST
    	print("Checking for Normal Errors")
    	result1=Test.add(10,5)
    	self.assertEqual(result1,15)

    	#You can run multiple tests in the same function, if some of them fail it is going to show Ran 1 Test Failed, Not Ran 2 tests and failed
    	result2=Test.add(-1,-2)
    	self.assertEqual(result2,-3)

    def test_sub(self): #ALL FUNCTIONS SHOULD START WITH THE NAME TEST
    	result1=Test.sub(10,5)
    	self.assertEqual(result1,5) #THIS TEST IS WRONG, SO SINCE IT IS THE SECOND TEST, IT IS GOING TO APPEAR FAILED IN THE OUTPUT 

    	#You can run multiple tests in the same function, if some of them fail it is going to show Ran 1 Test Failed, Not Ran 2 tests and failed
    	result2=Test.sub(-1,-2)
    	self.assertEqual(result2,1)

    def test_mult(self): #ALL FUNCTIONS SHOULD START WITH THE NAME TEST
    	result1=Test.mult(10,5)
    	self.assertEqual(result1,50)

    	#You can run multiple tests in the same function, if some of them fail it is going to show Ran 1 Test Failed, Not Ran 2 tests and failed
    	result2=Test.mult(-1,-2)
    	self.assertEqual(result2,2)

    def test_div(self): #SAME AS BEFORE
    	print("\nChecking for Exceptions")
    	with self.assertRaises(ZeroDivisionError):
    		Test.divide(10,0)

    # def test_add1(self): #SAME AS BEFORE- Check the one in front of the add. Each test must have a different name. Otherwise it is not going to run
    # 	print("\nChecking for Exceptions")
    # 	with self.assertRaises(ValueError):
    # 		Test.add(10,"ksaksaskj")

    def test_add1(self): #ALL FUNCTIONS SHOULD START WITH THE NAME TEST
    	print("After doing the part above to check ValueError the calculation was updated")
    	result1=Test.add("ssssss",5)
    	self.assertEqual(result1,None)

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
