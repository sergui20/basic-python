# -*- coding: utf-8 -*-

def main():
    word = input("Enter a word to check if it is a palindrome: ")
    result = check_if_palindrome(word)
    print(result)

def check_if_palindrome(word):
    reversed_word = word[::-1]
    
    if word.lower() == reversed_word.lower():
        return 'It is a palindrome'
    else:
        return 'It is not a palindrome'    

if __name__ == '__main__':
    main()