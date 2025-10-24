from time import sleep as s

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def to_decimal(numberString, originalBase):
    """
    Takes a number string and an original base and converts it into a decimal value
    """
    totalValue = 0
    power = 0 
    numberString = numberString[::-1] # reverses string
    for char in numberString:
        charDecimalValue = digits.index(char.upper())
        totalValue += (charDecimalValue * (originalBase ** power))
        power += 1

    return totalValue

def from_decimal(decimalNumber: int, targetBase: int):
    """
    Takes a decimal value and converts it to the target base, returning 0 if the decimal number is 0
    """
    if decimalNumber == 0:
        return "0"
    
    resultString = "" 
    while decimalNumber > 0:
        remainder = decimalNumber % targetBase
        decimalNumber = decimalNumber // targetBase
        charToAdd = digits[remainder]
        resultString = charToAdd + resultString

    return resultString

def main():
    print("Welcome to the hexorcist calculator ig.")
    s(3)

    # Get number string
    while True:
        numberString = input("Give me the number string: ")
        if numberString:
            break
        print("Input cannot be empty. Try again.")

    # Get original base
    while True:
        try:
            originalBase = int(input("Give me the original base (2-36): "))
            if originalBase > 1 and originalBase < 37:
                break
            print("Base must be greater than 1.")
        except ValueError:
            print("Invalid input. Enter an integer.")

    # Get target base
    while True:
        try:
            targetBase = int(input("Give me the target base (2-36): "))
            if targetBase > 1 and originalBase <37:
                break
            print("Base must be greater than 1.")
        except ValueError:
            print("Invalid input. Enter an integer.")


    if originalBase != targetBase:
        decimalValue = to_decimal(numberString, originalBase)
        resultStringAnswer = from_decimal(decimalValue, targetBase)
        print("Calculating.")
        s(0.5)
        print("Calculating..")
        s(0.5)
        print("Calculating...")
        s(0.5)
        print(f"Your value is {resultStringAnswer}. You're welcome ig.")

    else: # bases are the same, doesn't do any calculations
        print(f"Your value is {numberString}. I did no conversions, because you decided to enter the same base for the target and original.")

    s(3)

if __name__ == "__main__":
    main()