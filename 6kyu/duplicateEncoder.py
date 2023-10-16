def duplicate_encode(word):
    word = word.lower()
    counter = 0
    newWord = ""
    while counter < len(word):
        count = word.count(word[counter])
        if count == 1:
            newWord = newWord + "("
        else:
            newWord = newWord + ")"
        counter += 1
    return newWord
