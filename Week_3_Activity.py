while True:
    enterPass = input("Enter Password: ")
    isaLeter = False
    isaNumber = False

    for char in enterPass:
        if char.isalpha():
            isaLeter = True
        if char.isdigit():
            isaNumber = True
    
    if isaLeter and isaNumber:
        print("Password accepted")
        break
    else:
        print("Invalid password")