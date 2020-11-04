import math


class Polygonclass:
    def __init__(self, edges, circumradius=0):
        self.edges = edges
        self.circumradius = circumradius
        self.interior_angle = (edges - 2) * (180 / edges)
        self.edge_length = 2 * circumradius * math.sin(math.pi / edges)
        self.apothem = circumradius * math.cos(math.pi / edges)
        self.area = (edges * self.edge_length * self.apothem) / 2
        self.perimeter = edges * self.edge_length

  
    @property
    def get_edges(self):
        return self.__edges
    
    @get_edges.setter
    def set_edges(self,in_val):
        if in_val < 3:
            raise ValueError(f"Polygon Cant be formed with {in_val} edges")
        else:
            self.__edges=in_val
            
    @property
    def get_circumradius(self):
        return self.__circumradius
    
    @get_circumradius.setter
    def set_circumradius(self,in_val):
        if in_val < 0:
            raise ValueError(f"Circumradius must be positive")
        else:
            self.__circumradius=in_val

    def __repr__(self):
        value=f"Result Polygon with {self.edges} edges and {self.circumradius} circumradius has got Interior Angle =  {self.interior_angle:.2f} Edge_length = {self.edge_length:.2f}  Apothem = {self.apothem:.2f} Area = {self.area:.2f}  Perimeter = {self.perimeter:.2f}"
        return value
    
    def __eq__(self,other):
        if isinstance(other,Polygon):
            return self.edges == other.edges and self.circumradius == other.circumradius
        else:
            return False
        
    def __gt__(self,other):
        if isinstance(other,Polygon):
            return self.edges > other.edges
        else:
            return False

# p = Polygonclass(3, 10)
# print(p.perimeter)
#circumradius has got Interior Angle=  {self.interior_angle}, Edge_length= {self.edge_length} Apothem{self.apothem} Area={self.area} Perimeter={self.perimeter}
