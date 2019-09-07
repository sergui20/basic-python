#To use more characters
# -*- coding: utf-8 -*-

def main():
    number = input("Enter a number: ")
    result = is_Prime(number)
    if(result):
        print('Tu numero ES primo')
    else:
        print('Tu numero NO ES primo')    

def is_Prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3, number):
            if number % i == 0:
                return False
                
    return True    

if __name__ == '__main__':
    main()