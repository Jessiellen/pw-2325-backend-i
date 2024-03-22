from rectangle import Rectangle


def test_calculate_are():
    area = Rectangle(width=5,heigth=7).get_area() 
    
    assert area == 35
def test_calculate_perimeter():
    perimeter = Rectangle(width=5,heigth=7).get_perimeter()
    
    assert perimeter == 24
       
