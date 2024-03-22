# create a rectangulo objecto with "width" and "heigth" attributes and create 2 methods
# -area
# -perimeter

# Create test that for insuccess and sucess paths

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)


# rect = Rectangle(4, 5)
# print(f"Area: {rect.area()}")
# print(f"Perimeter: {rect.perimeter()}")

# import unittest
# import rectangulo

# class TestRetangulo(unittest.TestCase):
#     def test_area(self):
#         retangulo = rectangulo.Retangulo(4, 5)
#         self.assertEqual(retangulo.area(), 20)

#     def test_perimetro(self):
#         retangulo = rectangulo.Retangulo(4, 5)
#         self.assertEqual(retangulo.perimetro(), 18)

# if __name__ == '__main__':
#     unittest.main()

# /////////////CORREÇÃO////////////////////


import unittest
import math
math.pi

class Rectangle:
    def __init__(self, width:int, height:int):
        self.width=width
        self.height=height

    
    def get_area(self) -> int:
        return self.width*self.height
    
    def get_perimeter(self) -> int:
        return (self.width*2)+self.height*2

class RectangleTests(unittest.TestCase):
    
    def setUp(self) -> None:
        self.rectangle = Rectangle(width=5, height=7)   
        
    def test_calculate_area(self):
        
        area = self.rectangle.get_area()
        
        self.assertEqual(area, 35)
        
    def test_calculate_perimeter(self):
        perimeter = self.rectangle.get_perimeter()
        assert perimeter == 24

if __name__ == "__main__":
    unittest.main()
