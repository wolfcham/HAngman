import random
import time
#Initially we have to Welcome Our user

print("Hello!! , Welcome to Hangman By TNT")
user_name = input("Enter your Name : ")
print("Hello" + user_name + "Welcom to Hangmam")
time.sleep(2)
print("Let's Play")
time.sleep(3)

# Defining the main functions
def functions():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = "April", "Window", "DATA", "Analyst", "Dubai", "India","Redmi", "Python", "Cricket", "Lungs", "Code"
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display ='_' * length
    already_guessed = []
    play_game = " "
#Excute a loop after the first round ends

def play_round():
    global play_game
    play_game = input("Do you Want to play Again ? y = Yes and n = no \n")
    while play_game not in["y","n","Y","N"]:
        play_game = input("Do you Want to play Again ? y = Yes and n = no \n")
    if play_game =='y':
        functions()
    else:
        print("Thankypu for playing!! . Come back soon")
# Inititalizing all conditions required for the game

def Hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is a Hangman Word . " + display + "Guess the word \n")
    guess = guess.strip()
    if(len(guess.strip()) == 0 or len(guess.strip()) <= 2 or guess <= "9A"):
        print("Invalid Guess. Try Again!!! \n")

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1 :]
        display = display[:index] + guess + display[index+1:]
        print(display + "\n")
    elif guess in already_guessed:
        print("Try another Word . \n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong Guess ." + str(limit - count) + "guess remaining \n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong Guess ." + str(limit - count) + "guess remaining \n")

        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong Guess ." + str(limit - count) + "guess remaining \n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong Guess ." + str(limit - count) + " Last guess remaining \n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong Guess. You are Hang \n")
            print("The word was : " ,already_guessed,word)
            play_round()

    if word == '_' * length:
        print("Congrats !! You Guess the Right word ")
        play_round()

    elif count != limit:
        Hangman()

functions()
Hangman()
