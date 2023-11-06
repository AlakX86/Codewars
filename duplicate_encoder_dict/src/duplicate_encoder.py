def duplicate_encoder(string):
    newCodification = string.lower()
    char_codifications = {}
    for character in newCodification:
        if newCodification.count(character) == 1:
            char_codifications[character] = '('
        elif newCodification.count(character) > 1:
            char_codifications[character] = ')'
    newString = ""
    for character in newCodification:
        newString += char_codifications[character]
    return newString
