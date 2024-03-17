class MyComplexNumber:
    def __init__(self, real= 0,imag = 0): 
        print("MyComplexNumber constructor executing...")
        self.real_part = real
        self.image_part = image
    
    def displayComplex (self):
        print("{0}+{1}j" .format(self.real_part,self.imag_part))