import unittest
import test
from sut import *

class TestSut(unittest.TestCase):

    def test_area(self):
        calculararea=area(20, 2)
        self.assertTrue(calculararea == 40)

    def test_saludar(self):
        saludo = saludar('Damian')
        self.assertTrue(saludo == "Hola Damian")

    def test_sumar(self):
        calcularsuma = sumar(15, 15)
        self.assertTrue(calcularsuma == 30)

if __name__ == '__main__':
    unittest.main()
