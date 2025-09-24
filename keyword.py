def CalculatePercentage(Total,Obtained):
    output=((Obtained/Total)*100)
    return output

def main():
    print("enter total marks:")
    value1=int(input())

    print("enter obtained marks:")
    value2=int(input())

    output=((value2/value1)*100)

    result=CalculatePercentage(Obtained=value2,Total=value1) #keyword argument
    
    print("percentage:",result)




if __name__ == "__main__":
    main()