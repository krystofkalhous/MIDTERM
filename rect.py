#!/usr/bin/env python
# coding: utf-8

# In[52]:


class Rect:
    
    def __init__(self, x1, y1, x2, y2):
        self.x_1 = x1
        self.x_2 = x2
        self.y_1 = y1
        self.y_2 = y2
        
    def __repr__(self):
        return f"Rect({self.x_1},{self.y_1},{self.x_2},{self.y_2})"
    
    def perimeter(self):
        return (2 * (self.x_2 - self.x_1) + 2 * (self.y_2 - self.y_1))
    
    def area(self):
        return ((self.x_2 - self.x_1) * (self.y_2 - self.y_1))
    
    def __eq__(self, other):
        if (self.x_1 == other.x_1 and self.x_2 == other.x_2 and self.y_1 == other.y_1 and self.y_2 == other.y_2):
            return True
        
        else:
            return False
        
    def __contains__(self, other):
        if self.area() >= other.area():
            if (other.x_1 >= self.x_1 and other.y_1 >= self.y_1 and other.x_2 <= self.x_2 and other.y_2 <= self.y_2):
                return True
            
        else:
            return False
        
    def __and__(self, other):
        if (self.x_1 > self.x_2) or (self.y_1 > self.y_2) or (other.x_1 > other.x_2) or (other.y_1 > other.y_2): #wrong input from recodex? contradicts the task?
            a, b, c, d = 0, 0, 0, 0
            self.x_1, self.y_1, self.x_2, self.y_2 = a, b, c, d
            
            return self
            
        elif self in other:
            return self
        
        elif (min(self.x_1, self.y_1) <= min(other.x_1, other.y_1)) and (self.x_2 >= other.x_1) and (self.y_2 >= other.y_1):
            a = max(self.x_1, other.x_1)
            b = max(self.y_1, other.y_1)
            
            c = min(self.x_2, other.x_2)
            d = min(self.y_2, other.y_2)
            
            self.x_1, self.y_1, self.x_2, self.y_2 = a, b, c, d
            
            return self
        
        elif (max(self.x_1, self.y_1) >= max(other.x_1, other.y_1)) and (self.x_2 >= other.x_1) and (self.y_2 >= other.y_1):
            a = max(self.x_1, other.x_1)
            b = max(self.y_1, other.y_1)
            
            c = min(self.x_2, other.x_2)
            d = min(self.y_2, other.y_2)
            
            self.x_1, self.y_1, self.x_2, self.y_2 = a, b, c, d
            
            return self
        
        
        else:
            a, b, c, d = 0, 0, 0, 0
            self.x_1, self.y_1, self.x_2, self.y_2 = a, b, c, d
            
            return self
        

