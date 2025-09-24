class Circle:
    PI = 3.14

    def __init__(self,A):
        print("Inside Circle constructor")
        
        self.Radius = A  #Radius is instance variable of  class circle

    def CalculateArea(self):
        Ans = 0.0
        Ans = Circle.PI * self.Radius * self.Radius
        return Ans
        

class CircleX(Circle):
    def __init__(self,A):
        print("Inside CircleX constructor")
        super().__init__(A)  # goes from child constructor to parent construtor
        
    def CalculateCircumference(self):
        Ans = 0.0
        Ans = 2 * Circle.PI * self.Radius
        return Ans

def main():
    obj = CircleX(10.5)
    ret = obj.CalculateArea()
    print(ret)
    print("Area of circle is",ret )
    ret = obj.CalculateCircumference()
    print(ret)

if __name__=="__main__":
    main()   