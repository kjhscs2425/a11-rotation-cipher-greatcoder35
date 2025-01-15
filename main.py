import string
alphabet = string.ascii_lowercase

## eve wants to steal my password

## make my password secret
#key = 4

#def encrypt(plaintext):
#    ciphertext = ""
#    for letter in plaintext:
#        old_position = alphabet.find(letter)
#        if old_position == -1:
#            ciphertext += " "
#        else:
#            new_position = old_position + key
#            new_position = new_position % len(alphabet)
#            new_letter = alphabet[new_position]
#            ciphertext += new_letter
#    return ciphertext

#print(encrypt(password))

# Your task:
# figure out what key I used to encrypt this message:

secret_message = "y qc q iushuj cuiiqwu oek mybb duluh wkuii"
actual_message = "i am a secret message you will never guess"
def decrypt(plaintext,keyy):
    key = keyy
    ciphertext = ""
    for letter in plaintext:
        old_position = alphabet.find(letter)
        if old_position == -1:
            ciphertext += " "
        else:
            new_position = old_position + key
            new_position = new_position % len(alphabet)
            new_letter = alphabet[new_position]
            ciphertext += new_letter
    return ciphertext

def brute_force():
    keys_to_test = int(input("How many keys should I test? "))
    for i in range(keys_to_test):
        print(f"key tested: {i+1}")
        print(decrypt(secret_message,i+1))
        print(" ")

brute_force()