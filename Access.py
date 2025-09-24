class student:
    def __init__(self,A,B,C):
        self.Name=A
        self._Age=B
        self.__Marks = C

    def Display(self):
                print(self.Name)  
                print( self._Age)
                print(self.__Marks) 


obj = student('rahul',24,89) 
obj.Display()  

print(obj.Name)
print(obj._Age)
#print(obj._Marks)

        