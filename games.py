import random

def rps(player, bst):
    print("\n\033[1mWelcome to Rock Paper Scissor\033[0m")
    print("\033[1mHow to play?\033[0m")
    print("\t 1. Type Rock / Paper / Scissor")
    print("\t 2. Rock wins Against Scissor, Paper wins against Rock and Scissors win against Paper")

    ch = ['rock', 'paper', 'scissor']
    ps, cs, t = 0, 0, 0

    for _ in range(bst):
        while True:
            userch = input("Type Rock / Paper / Scissor: ").lower()
            if userch not in ch:
                print("Invalid choice. Please try again.")
                continue
            compch = random.choice(ch)
            print(f"Computer chose: {compch}")
            if userch == compch:
                print("It's a Tie")
                t += 1
            elif (userch == "rock" and compch == "scissor") or (userch == "paper" and compch == "rock") or (userch == "scissor" and compch == "paper"):
                print("Congrats You Win!!!\n")
                ps += 1
            else:
                print("Computer Wins. You Lost\n")
                cs += 1
            break

    if ps > cs:
        print(f"\033[1mFinal Score\033[0m\n {player} Score = {ps} \n Computer Score = {cs}\n Tied = {t}\n Total Games = {bst}", f"\n\033[1m\033[32m{player} Wins the Match\033[0m\033[0m")
    else:
        print(f"\033[1mFinal Score\033[0m\n {player} Score = {ps} \n Computer Score = {cs}\n Tied = {t}\n Total Games = {bst}", f"\n\033[1m\033[31m{player} Loses the Match\033[0m\033[0m")


def guess(player, rng):
    print("\n\033[1mWelcome To Guess The Number Game\033[0m")
    print("\033[1mHow to play?\033[0m")
    print("\t1. Guess the Number Until You Get it Right")

    if rng < 0:
        print("Please Enter a Positive number")
        return

    num = random.randint(0, rng)
    gcount = 0
    while True:
        try:
            guess = int(input("Enter Your Guessed Number: "))
            gcount += 1
            if guess == num:
                print(f"Congrats {player}!! You Guessed The Number in {gcount} tries")
                break
            elif guess > num:
                print("Your Guess is high")
            else:
                print("Your Guess is low")
        except ValueError:
            print("Please enter a valid number")


def main():
    pn = None
    while True:
        print("\033[1mWelcome to Python Games\033[0m")
        print("   1. Type \033[1mrps\033[0m For Rock Paper Scissors Game")
        print("   2. Type \033[1mguess\033[0m For Guess The Number Game")
        
        if pn is None:
            pn = input("Enter the Player Name: ").strip()
            if not pn:
                print("Please Type your name. You can't leave it empty")
                pn = None
                continue

        game = input("Enter the Game You Want To Play: ").lower().strip()
        if game == "rps":
            try:
                bst = int(input("Best Of (default is 1): ") or 1)
                rps(pn, bst)
            except ValueError:
                print("Please enter a valid number for Best Of")
        elif game == "guess":
            try:
                rng = int(input("Enter the Range (default is 10): ") or 10)
                guess(pn, rng)
            except ValueError:
                print("Please enter a valid range number")
        else:
            print("Please Enter A Valid Game Name\n")

        next_step = input("Do you want to continue or quit? To continue type '1' or 'continue', to quit type 'quit' or 'q': ").lower().strip()
        if next_step in ["1", "continue"]:
            continue
        elif next_step in ["q", "quit"]:
            print("\nThank You For Playing")
            break
        else:
            print("Invalid input, exiting the game.")
            break


if __name__ == "__main__":
    main()