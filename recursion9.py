#recursion logic code
#input : 4
#output : * * * *

def Display(no):
    if (no >= 1):
        print("*",end=" ")
        no = no - 1
        Display(no)

        
def main():
    Display(4)
    
if __name__ =="__main__":
    main()    
