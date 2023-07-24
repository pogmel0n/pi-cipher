with open("/Users/fangqi/Documents/snek/pystuff/cryptography/pi.txt") as f:
    pi = f.read()

check = False
decrypt = "x"
key = 1000000
word = 0

while check == False and key > 1000000 - len(word):
    if decrypt == "y":
        decrypt = True
        with open("/Users/fangqi/Documents/snek/pystuff/cryptography/ciphertext.txt", "r") as f:
            word = f.read()
        check = True
    elif decrypt == "n":
        decrypt = False
        with open("/Users/fangqi/Documents/snek/pystuff/cryptography/plaintext.txt") as f:
            word = f.read()
            word = word.replace(" ", "")
        check = True
    else:
        decrypt = input("decrypt: ").lower()

key = int(input("key: "))

def encrypt(word, key, decrypt):
    shiftkey = pi[key:(key + (2 * len(word)))]
    endword = ""
    counter = 0
    for shift in range(0, (len(shiftkey)), 2):
        s = (int(shiftkey[shift]) * 10 + int(shiftkey[shift + 1])) % 26

        if decrypt:
            s = 26 - s

        letter = word[counter]

        if ord(letter) < 65 or ord(letter) < 97 and ord(letter) > 90 or 122 < ord(letter):
                endword += letter

        elif (letter.isupper()):
                endword += chr((ord(letter) + s - 65) % 26 + 65)
    
        else:
                endword += chr((ord(letter) + s - 97) % 26 + 97)

        counter += 1
    return endword

f = open("/Users/fangqi/Documents/snek/pystuff/cryptography/ciphertext.txt", "w")
f.write(encrypt(word, key, decrypt))

