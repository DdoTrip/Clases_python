# Module Lab: Caesar Cipher Program Bug #2
#
# In a previous lab, you created a Caesar cipher program. This version of
# the program is buggy. Use a debugger to find the bug and fix it.

# Double the given alphabet
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# Get a message to encrypt
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

# Get a cipher key
def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return int(shiftAmount)  # Convert the shift amount to an integer

# Encrypt message
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = message.upper()  # Convert the message to uppercase
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + cipherKey
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

# Decrypt message
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * cipherKey  # No need to convert to int again
    return encryptMessage(message, decryptKey, alphabet)

# Main program logic
def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(f'Original Message: {myMessage}')
    myCipherKey = getCipherKey()
    print(f'Cipher Key: {myCipherKey}')
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decrypted Message: {myDecryptedMessage}')

# Main logic
runCaesarCipherProgram()
