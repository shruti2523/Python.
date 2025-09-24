no = 11   #global variable  #common use

def fun():
    global no     ####*
    print("Inside fun")
    x = 21      #local variable  # not common
    print("Value of x is : ",x)   #21
    no = no + 1
    print("Value of no : ",no)    #12

def main(): 

    print("Value of no before fun : ",no)  #11
    fun()
    print("Value of no after fun : ",no)   #12
    
if __name__=="__main__":
    main()