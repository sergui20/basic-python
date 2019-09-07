# -*- coding: utf-8 -*-

# Del modulo lamp trae la clase Lamp
from lamp import Lamp

def main():
    lamp = Lamp(False)        

    while True:
        command = input('''
            ¿Qué deseas hacer?

            [p]render
            [a]pagar
            [s]alir
        ''')

        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            break        

if __name__ == "__main__":
    main()                    
