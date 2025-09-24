no = 11   #global variable  #common use

def fun():
    print("Inside fun")
    x = 21   #local variable  # not common
    print("Value of x is : ",x) 
    print("Value of no : ",no)

def sun():
    print("Inside sun")
    y = 51    #local
    print("Value of y is : ",y)
    print("Value of no : ",no)


def main(): 
    fun()
    sun()

if __name__=="__main__":
    main()