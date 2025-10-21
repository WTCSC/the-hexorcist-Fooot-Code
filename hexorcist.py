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
    Takes a decimal value
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
    print("Give me the number string")
    numberString = input("> ")
    print("Give me the original base, in an integer")
    originalBase = int(input("> "))
    print("Give me the target base")
    targetBase = int(input("> "))

    if originalBase != targetBase:
        decimalValue = to_decimal(numberString, originalBase)
        resultStringAnswer = from_decimal(decimalValue, targetBase)
        print(f"Your value is {resultStringAnswer}. You're welcome ig.")

    else:
        print(f"Your value is {numberString}. I did no conversions, because you decided to enter the same base for the target and original.")

if __name__ == "__main__":
    main()