
def message_finder(message, original_alphabet, new_alphabet):
    '''
    Encrypts a message using a secret alphabet
    
    Args:
        message (str): the string that needs to be encrypted
        original_alphabet (list): standard set of letters that we start with
        new_alphabet (list): secret letters to use to encrypt the message
    Returns:
        str: encrypted message.
    '''
    new_message = '' #empty string to store encrypted message

    for m in message: #goes over each character in tn the message
        for letter in original_alphabet: #for every letter in the original alphabet
            if m == letter: #checks that current character matches current letter in alphabet
                new_message += new_alphabet[original_alphabet.index(letter)] #encrypts new_message 

    return new_message #returns encrypted message

def printinfo_encrypt(websites, usernames, passwords, password_encrypt, i):
    '''
   Prints lists for websites, usernames, passwords, and encrypted passwords
    
    Args:
        websites (list): list of user entered websites
        usernames (list): list of user entered usernames
        passwords (list): list of user entered password
        password_encrypt (list): list of user entered encrypted password
        i(int): index of print info
    Returns:
        vertically prints all args
    '''
    print(f'''\nwebsite: {websites[i]} 
username: {usernames[i]}
password: {passwords[i]}
secure password: {password_encrypt[i]}
''') 

def printinfo_standard(websites, usernames, passwords, i):
    '''
    Prints lists for websites, usernames, passwords, and encrypted passwords
    
    Args:
        websites (list): list of user entered websites
        usernames (list): list of user entered usernames
        passwords (list): list of user entered passwords
        i(int): index of print info
    Returns:
        vertically prints all args
    '''
    print(f'''\nwebsite: {websites[i]}
username: {usernames[i]}
password: {passwords[i]}
''')



def main(): #main function
     websites = [] #empty list that stores websites
     usernames = [] #empty list that stores usernames
     passwords = [] #empty list that stores passwords
     password_encrypt = [] #empty list that stores encrypted passwords

     while True: #loops code
    
         websites.append(input("please enter a website ")) #prompts user to enter a website and appends it to the websites list
         usernames.append(input("please enter a username "))#prompts user to enter a username and appends it to the usernames list
         passwords.append(input("please enter a password "))#prompts user to enter a password and appends it to the passwords list

         continue_choice = input("would you like to add more (1) continue (2) encrypt a password (3)") #prompts user to continue, encrypt a password, or add more passwords

         if continue_choice == "3": #if user chooses to encrypt a password
             alphabet = list(" ABCDEFGHIJKLMNOPQRSTUVWXYZ") #defines original alphabet 
             secret_alphabet = list("3*!B%^&HL:|?<>Z(~`.,}{\c#12") #defines secret alphabet
             message = str.upper(input("Enter message: ")) #prompts user to enter a message to encrypt and converts it to uppercase
             encrypt = input("Would you still like to encrypt?(y/n)") #prompts user to confirm encryption

             if encrypt == "y": #if the user confirms encryption
                 new_message = message_finder(message, alphabet, secret_alphabet) #encrypts message user message_finder function
                 print(new_message) #prints the encrypted message
                 password_encrypt.append(new_message) #adds encrypted message to the password_encrypt list
                 break #breaks loop
                
             else: #if the user chooses not to encrypt
                 break #breaks loop
                

         elif continue_choice == "2": #if the user chooses to continue
              break #breaks loop
            

          
          
     while True: #loops code continuously prompting the user to choose an action
                   
          mode = input("Would like to: print all(1), or print specific(2) change password (3) change username (4) exit (5)") #prompts user to choose an action

          if mode == "1": #if the user chooses to print all
              for i in range(len(websites)): #iterate and print information stored in each list
                  printinfo_encrypt(websites, usernames, passwords, password_encrypt, i) #call the printinfo_encrypt function for all entrys
                  
          elif mode == "2": #if the user chooses to print a specific entry
               name = input("Enter a website in the list: ") #prompts user to enter a specific website to print
               if name in websites: #checks if user input is in websites list
                     i = websites.index(name) #finds the index of the websites
                     printinfo_standard(websites, usernames, passwords, i)#call the printinfo_standard function
                     
          elif mode == "3": #if the user chooses to change a password
               password_change = input("Which website would you like to change the password for") #prompts user to enter the website of the password they want to change
               index = websites.index(password_change) #finds the index of the website
               passwords[index] = input("enter new password") #prompts user to enter a new passoword and updates it
               
          elif mode == "4": #if the user chooses to change a username
               username change = input("Which website would you like to change the username for") #prompts user to enter the website of the username they want to change
               index = websites.index(username_change) #finds the index of the website
               usernames[index] = input("enter new username") #prompts user to enter a new username and updates it
               
          elif mode == "5": #if the user wants to exit
               break #breaks loop and ends code
                

main() #calls the main function to start the code
                    
             
         



