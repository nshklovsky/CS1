

#will document upon resubmision

import random

def chorus ():
    print("Twinkle twinkle little star, How I wonder what you are, Up above the world so high.Like a diamond in the sky, Twinkle twinkle little star, How I wonder what you are.")

def sing_song ():
    print("Twinkle twinkle little star, How I wonder what you are, Up above the world so high.Like a diamond in the sky, Twinkle twinkle little star, How I wonder what you are.")

def add(num1,num2):
    print(num1+num2)

def print_list(my_list):
    for item in my_list:
        print(item)

def list_vertical():
    vert_list(my_list)

def element_in_list (my_list, element):
    for item in my_list:
       if item == element:
           return True
        
    return False

def is_string_an_integer(string):
    if string.isnumeric():
        return True

    else:
        return False

def integer_check():
    
        string = input("Enter string to check:")
        print(is_string_an_integer(string))


def rand_number():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    random_number = (random.randint((num1),(num2)))
    print(random_number)

def replace_char(string, old_char, new_char):
    new_string = ""
    for s in string:
        if s == old_char:
            new_string += new_char

        else:
            new_string += s

    return new_string

    

def main():
    chorus()
    add(1, 3)
    my_list = ["a", "b", "c"]
    print_list(my_list)
    print(element_in_list(my_list, "a"))
    print(element_in_list(my_list, "e"))
    integer_check()
    rand_number()
    print(replace_char("hello","l","a"))
    

main()
    
    
    
       
    
