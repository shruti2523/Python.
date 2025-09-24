
def main():
    print(" Enter first number : ")
    no1 = int(input())

    print(" Enter second number : ")
    no2 = int(input())

    ans = 0   #fix number

    try:
        ans = no1/no2

    except ZeroDivisionError as zobj:   #object name
        print("Exception occured due to second input",zobj)  #finally not compulsary


    print("Division is :",ans)

if __name__=="__main__":
    main()    