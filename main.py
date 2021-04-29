import random
import graphics




def pickRandomWord():
    wB = open("wordBank.txt", "r")
    wBList = []
    for i in wB:
        wBList.append(i)

    return random.choice(wBList)

wordToGuess = pickRandomWord()[:-1]
letters = []
guessedLetters = []

for c in wordToGuess:
    letters.append(c)
numLetters = len(letters)

def redisplay():
    global wrongGuesses
    print(graphics.manGraphics[wrongGuesses])
    wrongGuessesList = []
    for l in guessedLetters:
        if l not in letters:
            wrongGuessesList.append(l)
    print("Wrong Guesses: ", end="")
    for letter in wrongGuessesList:
        print(letter, end=", ")
    print("\n")
    for l in letters:
        if l in guessedLetters:
            print(l, end=" ")
        else:
            print("_", end=" ")

def checkWinner():
    allLettersGuessed = []
    for i in letters:
        allLettersGuessed.append(False)
    for i in range(0, len(letters)):
        if letters[i] in guessedLetters:
            allLettersGuessed[i] = True
    for letter in allLettersGuessed:
        if letter == False:
            return False
    return True
#this logic is about the dumbest thing i've ever made^^


wrongGuesses = 0
while wrongGuesses != 7:
    if checkWinner():
        print("""
                                                     __            __                                           
                                                    /  |          /  |                                          
  ______    ______    _______  __    __         ____$$ | __    __ $$ |____    _______         ______    ______  
 /      \  /      \  /       |/  |  /  |       /    $$ |/  |  /  |$$      \  /       |       /      \  /      \ 
/$$$$$$  | $$$$$$  |/$$$$$$$/ $$ |  $$ |      /$$$$$$$ |$$ |  $$ |$$$$$$$  |/$$$$$$$/       /$$$$$$  |/$$$$$$  |
$$    $$ | /    $$ |$$      \ $$ |  $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$      \       $$ |  $$ |$$ |  $$ |
$$$$$$$$/ /$$$$$$$ | $$$$$$  |$$ \__$$ |      $$ \__$$ |$$ \__$$ |$$ |__$$ | $$$$$$  |      $$ \__$$ |$$ \__$$ |
$$       |$$    $$ |/     $$/ $$    $$ |      $$    $$ |$$    $$/ $$    $$/ /     $$/       $$    $$ |$$    $$ |
 $$$$$$$/  $$$$$$$/ $$$$$$$/   $$$$$$$ |       $$$$$$$/  $$$$$$/  $$$$$$$/  $$$$$$$/         $$$$$$$ | $$$$$$$ |
                              /  \__$$ |                                                    /  \__$$ |/  \__$$ |
                              $$    $$/                                                     $$    $$/ $$    $$/ 
                               $$$$$$/                                                       $$$$$$/   $$$$$$/  """)
        break
    redisplay()
    if wrongGuesses == 6:
        print("\n" + wordToGuess)
        print("""
 __                                          __                        __                                            __                                     
/  |                                        /  |                      /  |                                          /  |                                    
$$ | _____  ____    ______    ______        $$ |____    ______    ____$$ |       __    __   ______   __    __       $$ |  ______    _______   ______        
$$ |/     \/    \  /      \  /      \       $$      \  /      \  /    $$ |      /  |  /  | /      \ /  |  /  |      $$ | /      \  /       | /      \       
$$ |$$$$$$ $$$$  | $$$$$$  |/$$$$$$  |      $$$$$$$  | $$$$$$  |/$$$$$$$ |      $$ |  $$ |/$$$$$$  |$$ |  $$ |      $$ |/$$$$$$  |/$$$$$$$/ /$$$$$$  |      
$$ |$$ | $$ | $$ | /    $$ |$$ |  $$ |      $$ |  $$ | /    $$ |$$ |  $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ |$$ |  $$ |$$      \ $$    $$ |      
$$ |$$ | $$ | $$ |/$$$$$$$ |$$ \__$$ |      $$ |__$$ |/$$$$$$$ |$$ \__$$ |      $$ \__$$ |$$ \__$$ |$$ \__$$ |      $$ |$$ \__$$ | $$$$$$  |$$$$$$$$/       
$$ |$$ | $$ | $$ |$$    $$ |$$    $$/       $$    $$/ $$    $$ |$$    $$ |      $$    $$ |$$    $$/ $$    $$/       $$ |$$    $$/ /     $$/ $$       |      
$$/ $$/  $$/  $$/  $$$$$$$/  $$$$$$/        $$$$$$$/   $$$$$$$/  $$$$$$$/        $$$$$$$ | $$$$$$/   $$$$$$/        $$/  $$$$$$/  $$$$$$$/   $$$$$$$/       
                                                                                /  \__$$ |                                                                  
                                                                                $$    $$/                                                                   
                                                                                 $$$$$$/                                                                    """)
        break
    guess = input("\nGuess a letter: ")
    guessedLetters.append(guess)
    if guess not in letters:
        wrongGuesses += 1


