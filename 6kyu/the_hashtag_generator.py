def generate_hashtag(text):
    print(text)
    if len(text) == 0:
        return False
    textFinalLocation = 0
    text = "#" + text.capitalize()
    for character in text:
        if character == " ":
            textFinalLocation = text.find(" ", textFinalLocation + 1)
            upperCharacter = text[textFinalLocation + 1].upper()
            text = text[:textFinalLocation + 1] + upperCharacter + text[textFinalLocation + 2:]
        else:
            continue
    text = text.replace (" ", "")
    if len(text) > 140:
        return False
    return text
