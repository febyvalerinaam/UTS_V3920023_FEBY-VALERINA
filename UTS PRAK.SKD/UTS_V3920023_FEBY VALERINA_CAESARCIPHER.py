def enkripsi():
    input_text = str(input("Masukan Text yang akan anda enkripsi: "))
    input_key = int(input("Masukan key/shift yang akan anda pakai: "))
    result = ""
    #transverse the plain text
    for i in range(len(input_text)):
        char = input_text[i]
    # Encrypt uppercase characters in plain text

        if char.isupper():
            result += chr((ord(char) + input_key - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        elif char == " ":
            result += " "
        else:
            result += chr((ord(char) + input_key - 97) % 26 + 97)

    return result

def dekripsi():
    Alpabeth1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    #Alpabeth2 = "abcdefghijklmnopqrstuvwxyz"
    input_encrypted = str(input("Masukan pesan yang akan di dekripsi: " ))

    for key in range(len(Alpabeth1)):
        translated = ""
        for symbol in input_encrypted:
            if symbol in Alpabeth1:
                num = Alpabeth1.find(symbol)
                num = num - 2
                if num < 0:
                    num = num + len(Alpabeth1)
                translated = translated + Alpabeth1[num]
            else:
                translated = translated + symbol

        print('Hacking key #%s: %s' % (key, translated))


