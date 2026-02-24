def numTest():
    print("Select operation. \n1.Add \n2.Subtract \n3.Multiply \n4.Divide")
    enterSign = int(input("Enter choice(1/2/3/4): "))
    enterNum1 = float(input("Enter your first number: "))
    enterNum2 = float(input("Enter your second number: "))
    
    if (enterSign == 1):
        print("Total: ", str(enterNum1 + enterNum2) )
    elif(enterSign == 2):
        print("Total: ", str(enterNum1 - enterNum2) )
    elif(enterSign == 3):
        print("Total: ", str(enterNum1 * enterNum2) )
    elif(enterSign == 4):
        print("Total: ", str(enterNum1 / enterNum2) )
    else:
        print("Invalid Sign")

numTest()