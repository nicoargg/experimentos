import random
import os
import sys

MENU = '''
888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P"                               '''

START = '''
  __      _____ _             _    
 /_ |    / ____| |           | |   
  | |   | (___ | |_ __ _ _ __| |_  
  | |    \___ \| __/ _` | '__| __| 
  | |_   ____) | || (_| | |  | |_  
  |_(_) |_____/_\__\__,_|_|   \__| 
 |__ \     / ____| |               
    ) |   | |    | | ___  ___  ___ 
   / /    | |    | |/ _ \/ __|/ _ 
  / /_ _  | |____| | (_) \__ \  __/
 |____(_)  \_____|_|\___/|___/\___|
                                   
                                   '''
WIN = '''

  /$$$$$$                                            /$$              
 /$$__  $$                                          | $$              
| $$  \__/  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$ 
| $$ /$$$$ |____  $$| $$__  $$ |____  $$ /$$_____/|_  $$_/   /$$__  $$
| $$|_  $$  /$$$$$$$| $$  \ $$  /$$$$$$$|  $$$$$$   | $$    | $$$$$$$$
| $$  \ $$ /$$__  $$| $$  | $$ /$$__  $$ \____  $$  | $$ /$$| $$_____/
|  $$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$ /$$$$$$$/  |  $$$$/|  $$$$$$$
 \______/  \_______/|__/  |__/ \_______/|_______/    \___/   \_______/
                                                                      
                                                                      
                                                                      
'''

LOOSE = '''

                                    $$\ $$\             $$\               
                                    $$ |\__|            $$ |              
 $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$$ |$$\  $$$$$$$\ $$$$$$\    $$$$$$\  
$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$ |$$ |$$  _____|\_$$  _|  $$  __$$\ 
$$ /  $$ |$$$$$$$$ |$$ |  \__|$$ /  $$ |$$ |\$$$$$$\    $$ |    $$$$$$$$ |
$$ |  $$ |$$   ____|$$ |      $$ |  $$ |$$ | \____$$\   $$ |$$\ $$   ____|
$$$$$$$  |\$$$$$$$\ $$ |      \$$$$$$$ |$$ |$$$$$$$  |  \$$$$  |\$$$$$$$\ 
$$  ____/  \_______|\__|       \_______|\__|\_______/    \____/  \_______|
$$ |                                                                      
$$ |                                                                      
\__|                                                                      
'''

HANGMANPICS = ['''
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
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']





def run():
    with open("./files/data2.txt","r",encoding="utf-8") as f:
        word_list = [word.strip() for word in f]
    random_word = random.choice(word_list) #chooses a random word of data2.txt
    what_word = ["_"] * len(random_word)

    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        random_word = random_word.replace(a, b).replace(a.upper(), b.upper()) #replace the letters with ´

    lives = 0

    while True:
        os.system("clear")
        os.system("cls")
        for character in what_word:
            print(character, end=" ") #prints in console _ for letters in the word
        print(HANGMANPICS[lives])

        letter = input("\nIngrese una letra: ")

        found = False

        for index, char in enumerate(random_word): #obtains the index of the choosed letter
            if char == letter:
                what_word[index] = letter
                found = True
        if not found:
            lives += 1
        if lives ==  7:
            print(LOOSE)
            print("La palabra era " + random_word)
            break

                
        if "_" not in what_word:
            print(WIN)
            break    

        
def menu():
    print(MENU)
    print(START)
    option = int(input(": "))
    if option == 1:
        run()
    if option == 0:
        sys.exit()
    
        

if __name__ == '__main__':
    os.system("clear")
    menu()
