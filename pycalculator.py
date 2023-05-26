# Create a while function to enable repeatability in the program
while True:
    print("Please press: 1 for Addition, 2 for Subtraction, 3 for Multiplication, 4 for Division")
    decision = input("Enter the number of your choice: ")

    # Create an if and elif function for ADDITION
    if decision == "1":
        print("You have selected Addition mode! Prepare to input two numbers to be combined.")
        try:
            num1 = input("Enter your 1st number: ")
            num2 = input("Enter your 2nd number: ")
            sum = float(num1) + float(num2)
            print("This is your output: ", sum)
        except ValueError:
            print("An error has been detected. Proceeding to redo function.")

        # Create an option to repeat the program
        print("Do you still wish to use this program: y/n?")
        choice = input(": ").lower
        if choice == "y":
            True
        else:
            break
    
     # Create an if and elif function for SUBTRACTION
    if decision == "2":
        print("You have selected Subtraction mode! Prepare to input two numbers to be included.")
        try:
            num1 = input("Enter your 1st number: ")
            num2 = input("Enter your 2nd number: ")
            difference = float(num1) - float(num2)
            print("This is your output: ", difference)
        except ValueError:
            print("An error has been detected. Proceeding to redo function.")

        # Create an option to repeat the program
        print("Do you still wish to use this program: y/n?")
        choice = input(": ").lower
        if choice == "y":
            True
        else:
            break

     # Create an if and elif function for MULTIPLICATION
    if decision == "3":
        print("You have selected Multiplication mode! Prepare to input two numbers to be multiplied.")
        try:
            num1 = input("Enter your 1st number: ")
            num2 = input("Enter your 2nd number: ")
            product = float(num1) * float(num2)
            print("This is your output: ", product)
        except ValueError:
            print("An error has been detected. Proceeding to redo function.")
        
        # Create an option to repeat the program
        print("Do you still wish to use this program: y/n?")
        choice = input(": ").lower
        if choice == "y":
            True
        else:
            break

    # Create an if and elif function for DIVISION
    if decision == "4":
        print("You have selected Division mode! Prepare to input two numbers to be divided.")
        try:
            num1 = input("Enter your 1st number: ")
            num2 = input("Enter your 2nd number: ")
            quotient = float(num1) * float(num2)
            print("This is your output: ", quotient)
        except ValueError:
            print("An error has been detected. Proceeding to redo function.")

         # Create an option to repeat the program
        print("Do you still wish to use this program: y/n?")
        choice = input(": ").lower
        if choice == "y":
            True
        else:
            break
    
    # Create an else function in case there is a mis-input
    else:
        print("That number is not part of the choices... would you like to keep using the program? y/n")
        choice = input(": ").lower
        if choice == "y":
            True
        else:
            break

print("Thank you! I hope this calculator served you well! :> ")