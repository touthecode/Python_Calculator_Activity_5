# Create a while function to enable repeatability in the program
while True:
    print("Please press: 1 for Addition, 2 for Subtraction, 3 for Multiplication, 4 for Division")
    decision = input("Enter the number of your choice: ")

    # Create a function for ADDITION
    if decision == "1":
        print("You have selected Addition mode! Prepare to input two numbers to be combined.")
        try:
            num1 = input("Enter your 1st number: ")
            num2 = input("Enter your 2nd number: ")
            sum = int(num1) + int(num2)
            print("This is your output: ", sum)
        except ValueError:
            print("An error has been detected. Proceeding to redo function.")