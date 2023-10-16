def to_camel_case(text):
    textFinalLocation = 0
    for character in text:
        if character == "-":
            textFinalLocation = text.find("-", textFinalLocation + 1)
            upperCharacter = text[textFinalLocation + 1].upper()
            text = text[:textFinalLocation + 1] + upperCharacter + text[textFinalLocation + 2:]
        elif character == "_":
            textFinalLocation = text.find("_", textFinalLocation + 1)
            upperCharacter = text[textFinalLocation + 1].upper()
            text = text[:textFinalLocation + 1] + upperCharacter + text[textFinalLocation + 2:]
        else:
            continue
    text = text.replace ("_", "")
    text = text.replace ("-", "")
    return text