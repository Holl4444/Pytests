def breakCamelCase(string: str):
    words = string.split(' ')
    clean_array = []
    for word in words:
        word = word[0] + ''.join([f' {char}' if char == char.upper() else char for char in word[1:]])
        clean_array.append(word)
    return ' '.join(clean_array)

print(breakCamelCase('breakCamelCase'))

