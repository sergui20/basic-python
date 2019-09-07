KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}

def encrypt_message(message):
    words = message.split(" ")
    encrypted_message = []

    for word in words:
        new_message = ''
        for letter in word:
            new_message += KEYS[letter]

        encrypted_message.append(new_message)

    return " ".join(encrypted_message)

def decode_message(message):
    words = message.split(" ")
    decoded_message = []

    for word in words:
        new_message = ''
        for letter in word:
            for key, value in KEYS.items():
                if letter == value:
                    new_message += key

        decoded_message.append(new_message)   

    return " ".join(decoded_message)         



def main():
    while True:
        command = input('''
            What would you like to do ?

            [c] encrypt a message
            [d] decode a message
            [e] exit
        ''')

        if command == 'c':
            message = input("Enter the message to encrypt: ")
            encrypted_message = encrypt_message(message)
            print('Encrypted message')
            print(encrypted_message)
        elif command == 'd':
            message = input("Enter a message to decode: ")    
            decoded_message = decode_message(message)
            print(decoded_message)
        elif command == 'e':
            print("leaving...")    
            break
        else:
            print("Command not found ! Enter a valid one")    

if __name__ == "__main__":
    print('Encrypt and decode messages...')
    main()