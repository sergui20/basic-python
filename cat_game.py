class Cat:

    _CATS = ['''

    |\---/|
    | o_o |
     \_^_/

    ''',
             '''
        |\__/,|   (`
      _.|o o  |_   ) )
    -(((---(((--------

    ''',
             '''
     _._     _,-'""`-._
    (,-.`._,'(       |\`-/|
        `-.-' \ )-`( , o o)
              `-    \`_`"'-

    ''',
             '''
     |\__/,|   (`
     |_ _  |.--.) )
     ( T   )     /
    (((^_(((/(((_/

    ''',
             '''
          |\      _,,,---,,_
    ZZZzz /,`.-'`'    -.  ;-;;,_
         |,4-  ) )-,_. ,\ (  `'-'
        '---''(_/--'  `-'\_)

    ''']

    def __init__(self, name):
        self.name = name
        self.energy = 5
        self.hungry = 5

    def display_cat(self, index):
        print(self._CATS[index])

    def play(self):
        if self.energy == 1:
            self.display_cat(0)
            print("Your cat {} doesn't want to play, he need to sleep or a little bit of love".format(self.name))
        elif self.hungry == 1:
            self.display_cat(0)
            print("Your cat {} doesn't want to play, he need to eat".format(self.name))
        else:
            self.energy -= 1
            self.display_cat(1)

    def eat(self):
        if self.hungry == 5:
            self.display_cat(0)
            print("Your cat {} doesn't want to eat, he is not hungry".format(self.name))
        else:
            self.hungry += 1
            self.display_cat(2)

    def receive_love(self):
        if self.energy == 5:
            self.display_cat(0)
            print("Don't bother him now, he doesn't want your love")
        elif self.hungry == 1:
            self.display_cat(0)
            print("He doesn't want your love now. If you love him, go feed him")
        else:
            self.energy += 1
            self.display_cat(3)

    def go_to_sleep(self):
        if self.energy == 5:
            self.display_cat(0)
            print("The one who need to sleep is you !")
        elif self.hungry == 1:
            self.display_cat(0)   
            print("You can't take him bed ! He need to eat !")
        else:
            self.energy += 1
            self.hungry = 1
            self.display_cat(4)

    def say_goodbye(self):
        if self.energy == 1:
            print("Your cat died ! You didn't give him enough affection before you left")
        elif self.hungry == 1:
            print("Your cat died ! You didn't leave him enough food before you left")
        else:
            self.display_cat(0)
            self.energy = 1
            self.hungry = 1
            print("Goodbye ! Don't forget comming back soon !")

    def get_cat_status(self):
        status = dict()
        status['energy'] = self.energy
        status['hungry'] = self.hungry
        return status                  


def main():
    print("Welcome to your virtual cat")
    name = str(input("Give a name to your cat: "))
    cat = Cat(name)
    cat.display_cat(0)

    while True:
        command = int(input('''
            What do you want to do with your cat ?

            [1] Play
            [2] Eat
            [3] Give him love
            [4] Take him to sleep
            [5] Say him goodbye
            [6] Check your cat status
        '''))

        if command == 1:
            cat.play()
        elif command == 2:
            cat.eat() 
        elif command == 3:
            cat.receive_love()
        elif command == 4:
            cat.go_to_sleep()
        elif command == 5:
            cat.say_goodbye()
            break
        elif command == 6:
            status = cat.get_cat_status()
            print('''
                Energy: {}
                Hungry: {}
            '''.format(status['energy'], status['hungry']))
        else:
            print("Command not found !")          

if __name__ == "__main__":
    main()