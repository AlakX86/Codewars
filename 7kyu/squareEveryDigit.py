def square_digits(num):
    count = 0
    numberString = str(num)
    lenNumberString = len(numberString)
    completeNumber = ""
    while count < lenNumberString:
        numberPosition = numberString[count]
        num = int(numberPosition) ** 2
        num = str(num)
        completeNumber = completeNumber + num
        count = count + 1
    completeNumber = int(completeNumber)
    return completeNumber
