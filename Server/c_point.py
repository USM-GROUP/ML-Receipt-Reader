class point:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @classmethod
    def set_x(self, x):
        self.x = x
    
    @classmethod
    def set_y(self, y):
        self.y = y

    @classmethod
    def set_point(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

    def __repr__(self):
        return "("+str(self.x)+","+str(self.y)+")"
