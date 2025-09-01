def breakCamelCase(string: str):
    words = string.split(' ')
    clean_array = []
    clean_word = ''
    for word in words:
        flag = 0
        for i, char in enumerate(word[1:]):
            if char == char.upper():
                if flag > 0:
                    clean_word = clean_word[:i + 1 + flag] + ' ' + clean_word[i + 1 + flag:]
                else:
                    clean_word += word[:i + 1] + ' ' + word[i + 1:]
                flag += 1
        if flag:
            clean_array.append(clean_word)
            clean_word = ''
        else:
            clean_array.append(''.join(word))
    return ' '.join(clean_array) if len(clean_array) > 1 else clean_array[0]

print(breakCamelCase('breakCamelCase'))
