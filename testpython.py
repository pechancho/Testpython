import unittest

import math
from sut import *

class Test(unittest.TestCase):

    def test_tarea(self):
        self.assertEqual(area(2, 3),6)

    def test_saludar(self):
        self.assertEqual(saludar("damian"),"Hola damian")

    def test_sumar(self):
        self.assertEqual(sumar(30, 10),40)

   
	
		
	
    def testcomparar2(self):
	
	
	
        self.assertEqual(comparar(2,1),"A mayor que B")
	
	
    def testcomparar(self):
        self.assertEqual(comparar(1,2),"A menor que B")
	
    def testcomparar3(self):
	
        self.assertEqual(comparar(2,2),"A y B son iguales")


	
    def testvalorabs(self):
        self.assertEqual(valorabsoluto(-50),50)
        
    def testvalorabs2(self):
        self.assertEqual(valorabsoluto(40),40)
	
	
        
    def testtotal(self):
        self.assertEqual(costototal(2, 2),"El costo total es $4")

    
    def test_supercalc(self):
        math.exp=MagicMock(return_value=2)
        math.sqrt=MagicMock(return_value=2)
        a=supercalc(3)
        self.assertTrue(a==2)



if __name__ == '__main__':
    unittest.main()
