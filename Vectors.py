import math

class Vector:
    
    #Initialises the x, y and z dimensions
    
    def __init__(self, x = 0, y = 0, z = 0):   
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
    #returns a vector in the form of a string
    
    def __str__(self):            
        return f"Vector({self.x}i + {self.y}j + {self.z}k)"
    
    #accessing the elements of the vector usng indexing
    
    def __getitem__(self, item):  
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.z
        else:
            return IndexError("The vector is in 3-Dimensions only!")
        
    #function for addition of vectors
    
    def __add__(self, other):
        return Vector(self.x + other.x,
                      self.y + other.y,
                      self.z + other.z)
    
    #function for subtracton of vectors
    
    def __sub__(self, other):
        return Vector(self.x - other.x,
                      self.y - other.y,
                      self.z - other.z)
    
    #function for multiplication of vectors
    
    def __mul__(self, other):
        if isinstance(other, Vector):  #vector dot product
            return (self.x * other.x
                   + self.y * other.y
                   + self.z * other.z)
        elif isinstance(other, (int, float)):  #scalar multiplication
            return Vector(self.x * other,
                    self.y * other,
                    self.z * other)
        else:
            return TypeError("Operand must be of Type Vector, int, float")
        
    #function for scalar divison
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x / other,
                          self.y / other,
                          self.z / other)
        else:
            return TypeError("Vector Divsion is not possible")
        
    #function to find the magnitude of a vector
    
    def get_magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    #function to find a unit vector
    
    def normalize(self):
        magnitude = self.get_magnitude()
        return Vector(self.x / magnitude,
                      self.y / magnitude,
                      self.z / magnitude)



        






















