from PyDictionary import PyDictionary
dictionary=PyDictionary()


with open("pi.txt") as f:
    pi = f.read()

check = False
decrypt = "x"
key = 1000000
word = ""

while check == False and key >= 1000000 - len(word):
    if decrypt == "y":
        decrypt = True
        with open("ciphertext.txt", "r") as f:
            word = f.read()
        check = True
    elif decrypt == "n":
        decrypt = False
        with open("plaintext.txt") as f:
            word = f.read()
            word = word.replace(" ", "")
        check = True
    else:
        decrypt = input("decrypt: ").lower()

key = int(input("key: "))

def encrypt_or_decrypt(word, key, decrypt):
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
if decrypt == True:
    f = open("plaintext.txt", "w")
else:
    f = open("ciphertext.txt", "w")


key_list = []
for possible_key in range(0, 1000000-len(word)):
    possible_decripted_message = encrypt_or_decrypt(word, possible_key, decrypt)
    """
    two_letter_word = dictionary.meaning(possible_decripted_message[0:2])
    three_letter_word = dictionary.meaning(possible_decripted_message[0:3])
    four_letter_word = dictionary.meaning(possible_decripted_message[0:4])
    five_letter_word = dictionary.meaning(possible_decripted_message[0:5])
    six_letter_word = dictionary.meaning(possible_decripted_message[0:6])
    seven_letter_word = dictionary.meaning(possible_decripted_message[0:7])
    eight_letter_word = dictionary.meaning(possible_decripted_message[0:8])
    nine_letter_word = dictionary.meaning(possible_decripted_message[0:9])
    ten_letter_word = dictionary.meaning(possible_decripted_message[0:10])
    if two_letter_word != None or three_letter_word != None or four_letter_word != None or five_letter_word != None or six_letter_word != None or seven_letter_word != None or eight_letter_word != None or nine_letter_word != None or ten_letter_word != None:
        print(possible_key, " ", possible_decripted_message)
    """
    if "€" not in possible_decripted_message.lower() and "â" not in possible_decripted_message.lower() and "[" not in possible_decripted_message.lower() and "{" not in possible_decripted_message.lower():
        key_list.append(possible_key)
        print(possible_decripted_message)

print(key_list)
for possible_key in key_list:
    print(encrypt_or_decrypt(word, possible_key, decrypt))

f.write(encrypt_or_decrypt(word, 61736, decrypt))
