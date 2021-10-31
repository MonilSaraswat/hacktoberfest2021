def inputValues():
    firstNumber = int(input("Enter first number : "))
    secondNumber = int(input("Enter second number : "))
    return [firstNumber , secondNumber]

choice = 'Y'
while(choice in ('Y' , 'y')):
    values = inputValues()
    operation = input("What Do you want to perform : ")
    if (operation in ('+' ,'plus' , 'add' , 'adition')):
        print("Output is :" , values[0]+values[1])
        choice = input("Do you want to continue... Y/N ")
    elif(operation in ('-' ,'minus' , 'subtract' , 'subtraction')):
        print("Output is :" ,  abs(values[0]-values[1]))
        choice = input("Do you want to continue... Y/N ")
    elif(operation in ('*' , 'multiply' , 'multiplication')):
        print("Output is :" , values[0]*values[1])
        choice = input("Do you want to continue... Y/N ")
    elif(operation in ('/' , 'divide' , 'division')):
        print("Output is :" , values[0]/values[1])
        choice = input("Do you want to continue... Y/N ")
    else:
        choice = input("Not a correct Input.. \n Do you want to continue... Y/N ")

else: print("Thanks for using my calculator")
