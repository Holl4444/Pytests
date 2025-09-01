def breakCamelCase(string: str):
    if not string:
        return ''
    return ' '.join(        
        ''.join(f' {char}' if char.isupper() else char for char in word) 
        for word in string.split(' ')).lstrip()
       

print(breakCamelCase('breakCamelCase'))