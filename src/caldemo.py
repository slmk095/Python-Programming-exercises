print("Calculator")
num1 = int(input("Give the first number:"))
numA = int(input("Give the second number:"))


#Operator Mode List



print("\n(1)+\n(2)-\n(3)*\n(4)/\n(5)Change numbers\n(6)Quit\
\nCurrent numbers:",num1,numA)


#Input Mode Choice

operation_choice=input("Please select something (1-6):")

#If-Elif selection and operation performance structure.

    if operation_choice == "1":
        sum= int(num1)+int(numA)
        print("The result is:",sum)


    elif operation_choice == "2":
        difference= int(num1)-int(numA)
        print("The result is:",difference)


    elif operation_choice == "3":
        product= int(num1)*int(numA)
        print("The result is:",product)



    elif operation_choice == "4":
        quotient= int(num1)/int(numA)
        print("The result is:",quotient)



    elif operation_choice == "5":




    elif operation_choice == "6":
        print("Thanks!")




    else:
        print("Selection was not correct.")