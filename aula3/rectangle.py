class Rectangle:
    
     def __init__(self,width:int, height:int) -> None:
        self.width=width
        self.height=height
    
     def get_area(self) -> int:
        """
             Calculates the Rectangleś area
        """
        return (self.width*2)+self.height*2
     
     def get_perimeter(self) ->int:
        return self.width*self.height   
