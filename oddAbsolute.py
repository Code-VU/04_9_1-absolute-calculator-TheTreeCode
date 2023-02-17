def inputValidation():
    while True:
        try:
            in_num  = int(input("Enter a number: "))
            break
        except:
            print("Please enter only numeric values, without any text or special characters. Please try again.")
            continue
    return in_num

def calculateAbsolute():
    # This first line is provided for you
    n=inputValidation()
    if n > 21: difference = (n-21)*2
    else: difference = n - 21
    if difference < 0: difference = difference * -1
    print (f'Result: {difference}')
    # end assignment

## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()
