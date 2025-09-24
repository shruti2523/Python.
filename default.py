def CalculatePercentage(Obtained,Total=500):
    output=((Obtained/Total)*100)
    return output

def main():
    

    print("enter obtained marks:")
    value2=int(input())

    output=((value2/value1)*100)

    result=CalculatePercentage(value2) #default argument

    print("percentage:",result)




if __name__ == "__main__":
    main()