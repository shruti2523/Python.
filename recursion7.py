 #using for loop
#input : 4
#output : * * * *

def Display(no):
    for i in range(no):
        print("*",end=" ")
    print()    

def main():
    Display(4)
    
if __name__ =="__main__":
    main()    
