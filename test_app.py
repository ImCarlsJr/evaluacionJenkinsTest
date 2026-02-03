import unittest
from app import suma

class TestSuma(unittest.TestCase):

    def test_suma_correcta(self):
        self.assertEqual(suma(2, 3), 5)

    def test_suma_negativos(self):
        self.assertEqual(suma(-1, -1), -2)

if __name__ == "__main__":
    unittest.main()
