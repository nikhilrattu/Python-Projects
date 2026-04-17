import random
choice = input(f"What do you choose? Rock, Paper, Scissors: "
               "Type 0 for 'rock', 1 for 'paper', 2 for 'scissors': \n")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
if choice == "0":
    print(f"You chose {rock}\n")
elif choice == "1":
    print(f"You chose {paper}\n")
else:
    print(f"You chose {scissors}\n")
Computer_choices=[rock,paper,scissors]
final_choice=random.choice(Computer_choices)
print(f"Computer chose: {final_choice}\n")
if final_choice == rock and choice == "0":
    print("Draw\n")
elif final_choice == paper and choice == "0":
    print("You lose\n")
elif final_choice == scissors and choice == "0":
    print("You win\n")
elif final_choice == paper and choice == "1":
    print("Draw\n")
elif final_choice == scissors and choice == "1":
    print("You lose\n")
elif final_choice == rock and choice == "1":
    print("You win\n")
elif final_choice == scissors and choice == "2":
    print("You draw\n")
elif final_choice == paper and choice == "2":
    print("You win\n")
elif final_choice == rock and choice == "2":
    print("You lose\n")