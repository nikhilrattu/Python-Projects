import random


def set_difficulty():
    while True:
        choose=input("Type 'easy' or 'hard': ").lower().strip()
        if choose=="easy":
            return 10
        elif choose=="hard":
            return 5
        else:
            print("Invalid Input")

def check_guess(guess,number):
    if guess>number:
        print("Too high")

        return False
    elif guess<number:
        print("Too low")
        return False
    else:
        print("Correct")
        return True 
def play():
    number = random.randint(1,50)
    correct=False
    attempts=set_difficulty()
    while not correct and attempts>0:
        guess=int(input("Guess a number: "))
        correct= check_guess(guess,number)
        if not correct:
            attempts-=1
            print(f"You have {attempts} attempts left \n")
    if not correct:
        print(f"you lost. the number was {number}")

print("""   ____     _   _ U _____ u ____    ____     _____    _   _  U _____ u _   _       _   _   __  __     ____  U _____ u   ____     
U /"___|uU |"|u| |\| ___"|// __"| u/ __"| u |_ " _|  |'| |'| \| ___"|/| \ |"|   U |"|u| |U|' \/ '|uU | __")u\| ___"|/U |  _"\ u  
\| |  _ / \| |\| | |  _|" <\___ \/<\___ \/    | |   /| |_| |\ |  _|" <|  \| |>   \| |\| |\| |\/| |/ \|  _ \/ |  _|"   \| |_) |/  
 | |_| |   | |_| | | |___  u___) | u___) |   /| |\  U|  _  |u | |___ U| |\  |u    | |_| | | |  | |   | |_) | | |___    |  _ <    
  \____|  <<\___/  |_____| |____/>>|____/>> u |_|U   |_| |_|  |_____| |_| \_|    <<\___/  |_|  |_|   |____/  |_____|   |_| \_\   
  _)(|_  (__) )(   <<   >>  )(  (__))(  (__)_// \\_  //   \\  <<   >> ||   \\,-.(__) )(  <<,-,,-.   _|| \\_  <<   >>   //   \\_  
 (__)__)     (__) (__) (__)(__)    (__)    (__) (__)(_") ("_)(__) (__)(_")  (_/     (__)  (./  \.) (__) (__)(__) (__) (__)  (__) 
      """)
play()
while input("Do you want to play again> type 'y' or 'n'") == "y": play()
       