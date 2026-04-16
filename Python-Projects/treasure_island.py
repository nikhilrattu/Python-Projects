print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
direction=input("Choose the direction where you wanna go left or right\n")
if direction=="left":
    print("You pick left like a true explorer. Bold move. The island nods in approval.\n")
    swim = input("Would you like to swim or wait?")
    if swim == "wait":
        print("You wait patiently. For once, doing nothing is the smartest thing you’ve ever done.\n")
        door = input("Would you like to enter red, yellow or blue door\n")
        if door == "red":
            print("You open the red door. Turns out it’s just fire. Lots and lots of fire. Game over\n")
        elif door == "yellow":
            print("You open the yellow door… jackpot! Treasure, glory, and bragging rights unlocked. You win!\n")
        elif door == "blue":
            print("The blue door creaks open… beasts rush out like it’s feeding time. Spoiler: it is. Game over.\n")
        else:
            print("You pick a mystery door. The game wasn’t coded for this. Reality glitches. Game over.\n")
    elif swim == "swim":
        print("You dive in heroically… and immediately become a trout’s lunch special. Game over.\n")
    else:
        print(
            "You attempt something that is definitely not swimming. The fish call it “experimental cuisine.” Game over.\n")
elif direction=="right":
    print("You confidently stride right… straight into a perfectly camouflaged hole. Gravity wins. Game over.\n")
else:
    print("You try a “creative” direction. The island deletes you from existence. Game over.\n")
