def duplicate_count_func(text):
    char_count = {}
    for char in text:
        char_lower = char.lower()
        if char_lower.isalnum():
            char_count[char_lower] = char_count.get(char_lower, 0) + 1

    duplicate_count = sum(count > 1 for count in char_count.values())
    return duplicate_count
