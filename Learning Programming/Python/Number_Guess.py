import random

def main():
    lives = 0
    specialNum = random.randint(1, 100)
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100.")
    print(f"Num is {specialNum}")
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty_level == "easy":
        lives = 10
    elif difficulty_level == "hard":
        lives = 5
    

    guess_correct = False

    while lives > 0 and guess_correct == False:
        print(f"You have {lives} attempts remaining to guess the number.")
        userNum = int(input("Make a guess: "))
        if userNum < specialNum:
            print("Too low.")
            lives -= 1
        elif userNum > specialNum:
            print("Too high.")
            lives -= 1
        else:
            print(f"You got it! The number was {specialNum}")
            guess_correct = True
    
    if lives == 0:
        print("You've run out of guesses, you lose.")


if __name__=="__main__":
    main()




    

