no = 11   #global variable  #common use

def fun(no):
    #global no
    print("fun no :",no)  #21
   
def main(): 
    print("main no :",no)  #11
    fun(21)
 
if __name__=="__main__":
    main()