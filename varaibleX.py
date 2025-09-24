def Display(*A):  
    print(type(A))
    print("Inside Display",A)
    

def main():
    Display(11,21,51,101)
    Display(2,4,55,67,55,44)
    Display(11,33,22) 
    Display(11)   
    Display()




if __name__ == "__main__":
    main()    