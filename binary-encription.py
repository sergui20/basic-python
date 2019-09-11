def encrypt(message):
    encrypted_message = []
    for letter in message:
        encrypted_word = format(ord(letter), 'b')
        encrypted_message.append(encrypted_word)

    return " ".join(encrypted_message)    

def decrypt(message):
    message += " "
    decrypted_message = []
    memory = ''
    for binary in message:
        if binary == " ":
            letter = bin_to_letter(memory)
            decrypted_message.append(letter)
            memory = ""
        else:
            memory += binary

    return "".join(decrypted_message)   

def bin_to_letter(binary):
    sumatory = 0
    for idx, num in enumerate(binary[::-1]):
        if num == '1':
            sumatory += 2 ** int(idx)
            
    return chr(sumatory)
    # or just
    # return chr(int(binary, 2))
    

def main():
    while True:
        command = int(input('''
            What would you like to do ?

            [1] encrypt a message
            [2] decrypt a message
            [3] exit
        '''))

        if command == 1:
            message = str(input("Enter the message you want to encrypt: "))
            encrypted_message = encrypt(message)
            print(encrypted_message)
        elif command == 2:
            message = str(input("Enter the message you want to decrypt: "))
            decrypted_message = decrypt(message)
            print(decrypted_message)
        elif command == 3:
            break
        else: 
            print("Command not found !")

if __name__ == "__main__":
    main()