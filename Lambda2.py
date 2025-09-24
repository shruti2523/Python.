def CheckEven(NO):
    if(NO % 2 == 0):
        return True
    else:
        return False


ret = CheckEven(10)

if ret == True:
    print("Number is Even")
else:
    print("Number is False")   

