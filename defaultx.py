def CalculatePercentage(Obtained=400,Total=500):
    output=((Obtained/Total)*100)
    return output

def main():
    result=CalculatePercentage(350,450)
    print("percentage:",result)

    result=CalculatePercentage(350,)
    print("percentage:",result)
    

    result=CalculatePercentage()
    print("percentage:",result)




if __name__ == "__main__":
    main()