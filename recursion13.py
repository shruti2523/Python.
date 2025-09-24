#recursion logic code
#input : 4
#output : 24 



def Factorial(no):
    Fact = 1


    while(no>=1):
        Fact = Fact * no
        no = no -1
    return  Fact    
   
    
def main():
    ret = Factorial(4)
    print(ret)
    
if __name__ =="__main__":
    main()    
