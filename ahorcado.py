import random

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]

random_word = WORDS[random.randint(0, len(WORDS) - 1)]
secret_word = ['_'] * len(random_word)

def initializeGame():
    lives = len(IMAGES) - 1
    drawTemplate('', lives)

    while(True):
        letter = input("Enter a letter: ")
        
        if letter in random_word and letter not in secret_word:
            drawTemplate(letter, lives)
        else:
            lives = lives - 1
            drawTemplate('', lives)   

        if("".join(secret_word) == "".join(random_word)):
            print('Ganaste !')
            break
        elif lives == 0:
            print('Perdiste ! La palabra era {}'.format(random_word))
            break     

def drawTemplate(letter, lives):
    print(IMAGES[(len(IMAGES) - 1) - lives])

    for n, i in enumerate(random_word):
        if i == letter:
            secret_word[n] = letter

    print(" ".join(secret_word))      
    

if __name__ == "__main__":
    initializeGame()