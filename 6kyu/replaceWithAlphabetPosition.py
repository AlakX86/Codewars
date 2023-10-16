import string
def alphabet_position(text):
    fullString = ""
    for character in text:
        if character in string.ascii_lowercase:
            number = string.ascii_lowercase.index(character)
        elif character in string.ascii_uppercase:
            number = string.ascii_uppercase.index(character)
        else:
            continue
        number = number + 1
        numberString = str(number)
        fullString = fullString + numberString + " "
    return fullString[:-1]