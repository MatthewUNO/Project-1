import unittest
from functions import *

class TestShapes(unittest.TestCase):

    #Test Rectangle
    def test_generate_rectangle(self):
        self.assertEqual(generate_rectangle(5, 10), 50)
        self.assertAlmostEqual(generate_rectangle(1, 1.6), 1.6, delta=0.001)
        
        with self.assertRaises(TypeError):
            generate_rectangle('0.1')
            
        with self.assertRaises(ValueError):
            generate_rectangle(0, 0)
            generate_rectangle(-1, 1.5)

    #Test Triangle
    def test_generate_triangle(self):
        self.assertEqual(generate_triangle(2,1,0), 1)
        self.assertAlmostEqual(generate_triangle(2, 4, 0), 4, delta=0.001)
        
        with self.assertRaises(TypeError):
            generate_triangle('0.1')
            
        with self.assertRaises(ValueError):
            generate_triangle(2, 0, 0)
            generate_triangle(1, 1.5, 0)

    # Test Square
    def test_generate_square(self):
        self.assertEqual(generate_square(10), 100)
        self.assertAlmostEqual(generate_square(0.1), 0.01, delta=0.001)

        with self.assertRaises(TypeError):
            generate_square('0.1')

        with self.assertRaises(ValueError):
            generate_square(0)
            generate_square(-4)

    # Test Circle
    def test_generate_circle(self):
        self.assertAlmostEqual(generate_circle(2), 12.566, delta=0.001)

        with self.assertRaises(TypeError):
            generate_circle('0.1')

        with self.assertRaises(ValueError):
            generate_circle(0)
            generate_circle(-4)
    
if __name__ == '__main__':
    unittest.main()