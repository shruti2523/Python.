
def main():
    ans = 0
    
    try:
        print(" Enter first number : ")
        no1 = int(input())

        print(" Enter second number : ")
        no2 = int(input())

        ans = no1/no2

    except ZeroDivisionError as zobj:   #object name
        print("Exception occured due to second input",zobj)  #finally not compulsary

    except ValueError as vobj:
        print("Invalid data type of input : ",vobj)


    except Exception as eobj:    #except any error
        print("Exception occured : ",eobj)   

    print("Division is : ",ans)     

if __name__=="__main__":
    main()    
