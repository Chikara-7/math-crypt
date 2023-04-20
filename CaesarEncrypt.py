def encrypt(text, s):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char
    return result

text = input("Text: ")
s = int(input("Shift: "))
print ("Encrypt: " + encrypt(text,s))
exit = input("press Enter to close")
