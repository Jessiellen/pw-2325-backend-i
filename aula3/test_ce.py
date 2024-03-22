# def escreve(a):
#     print (a)
    
# a=1
# escreve(a)

# if __name__ == "__main__":
#     a=3
#     escreve(a)
    
#   //////////Minha solução/////////////  
# def escreve(*numeros):
#     for numero in numeros:
#         print(numero)

# if __name__ == "__main__":
#     a = 1
#     b = 2
#     c = 3
#     escreve(a, b, c)


# import pytest 

# def sum(a:int, b:int) -> int:
#     return a+b

# @pytest.mark.parametrize(
#     argnames="a,b,result",
#     argvalues=[
#         (1,2,3),
#         (2,2,4)
#     ]
# )

# def test_cenas(a,b,result):
#     assert sum(a,b) is result
    
# def two():
#     assert 1 == 1

# import pytest
# import unittest
# import math
# math.pi 

# class Rectangle:

#     def __init__(self, width:int, height:int):
#         self.width=width
#         self.height=height

    
#     def get_area(self) -> int:
#         return self.width*self.height
    
#     def get_perimeter(self) -> int:
#         return (self.width*2)+self.height*2

# class RectangleTests(unittest.TestCase):
    
#     def setUp(self) -> None:
#         self.rectangle = Rectangle(width=5, height=7)   
        
#     def test_calculate_area(self):
        
#         area = self.rectangle.get_area()
        
#         self.assertEqual(area, 35)
        
#     def test_calculate_perimeter(self):
#         perimeter = self.rectangle.get_perimeter()
#         assert perimeter == 24

# import pytest
# import unittest
# import math
# math.pi 

# class Circle:
    
#     def __init__(self, radious:int) -> None:
#         self.radious = radious
    
#     @property
#     def perimeter(self) ->float:
#         return 2*math.pi*self.radious
    
#     @property
#     def area(self) ->float:
#         return math.pi*self.radious**2


# class CircleTests(unittest.TestCase):
    
#     def setUp(self) -> None:
#         self.circle = Circle(radious=5)
        
#     def test_perimeter(self):
#         assert 31.416 == round(self.circle.perimeter, 3)
        
#     def test_area(self):
#         assert 78.54 == round(self.circle.area, 2)


