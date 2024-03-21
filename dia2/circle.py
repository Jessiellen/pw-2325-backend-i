# import unittest
# import math
# math.pi

# class Circle:
#     def __init__(self, radius: float):
#         self.radius = radius

#     def get_area(self) -> float:
#         return math.pi * (self.radius ** 2)

#     def get_circumference(self) -> float:
#         return 2 * math.pi * self.radius

# class CircleTests(unittest.TestCase):
    
#     def setUp(self) -> None:
#         self.circle = Circle(radius=5)   
        
#     def test_calculate_area(self):
        
#         area = self.circle.get_area()
        
#         self.assertAlmostEqual(area, 78.53981633974483)
        
#     def test_calculate_circumference(self):
#         circumference = self.circle.get_circumference()
#         self.assertAlmostEqual(circumference, 31.41592653589793)

# if __name__ == "__main__":
#     unittest.main()
    
    
# /////////////CORREÇÃO////////////
import math
class Circle:
    
    def __init__(self, radious:int) -> None:
        self.radious = radious
    
    @property
    def perimeter(self) ->float:
        return 2*math.pi*self.radious
    
    @property
    def perimeter(self) ->float:
        return math.pi*self.radious**2
    
    