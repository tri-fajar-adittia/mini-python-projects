def addition(number_1, number_2):
    result = number_1 + number_2
    return result

def subtraction(number_1, number_2):
    result = number_1 - number_2
    return result

def multiplication(number_1, number_2):
    result = number_1 * number_2
    return result

def division(number_1, number_2):
        try:
            result = number_1 / number_2
            return result
        except ZeroDivisionError:
            print("Cannot divide by zero.")
            return None

def operation(number_1,number_2):
    while True:
        try:
                print("\nChoose an operation:")
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")
                
                choice = int(input("Enter your choice: "))

                match choice:
                    case 1:
                        result = addition(number_1, number_2)
                    case 2:
                        result = subtraction(number_1, number_2)
                    case 3:
                        result = multiplication(number_1, number_2)
                    case 4:
                        result = division(number_1, number_2)
                    case _:
                        print("Please choose between 1 and 4.")
                        continue
                        
                return choice, result
            
        except ValueError:
            print("Invalid input. Please enter a number.")

def user_input():
    while True:
        try:
            number_1 = int(input("Enter first number: "))
            number_2 = int(input("Enter second number: "))

            return number_1,number_2
        except ValueError:
            print("Invalid input. Please enter a number.")

def display():
    print("\n===================================")
    print("          CALCULATOR APP            ")
    print("===================================")
    print("       By Tri Fajar Adittia         ")
    print("===================================\n")

def display_show(number_1, number_2, choice, result):
    match choice:
        case 1:
            print(f"\nResult: {number_1} + {number_2} = {result}")
        case 2:
            print(f"\nResult: {number_1} - {number_2} = {result}")
        case 3:
            print(f"\nResult: {number_1} * {number_2} = {result}")
        case 4:
            if result is not None:
                print(f"\nResult: {number_1} / {number_2} = {result}")

def main():
    display()

    loop = "y"

    while loop.lower() == "y":
        number_1, number_2 = user_input()
        choice, result = operation(number_1, number_2)
        display_show(number_1, number_2, choice, result) 
    
        loop = input("\nCalculate again? (y/n): ")

    print("\n===================================")
    print("Thank you for using Calculator App!")
    print("See you next time!")
    print("===================================\n")
     
main()
