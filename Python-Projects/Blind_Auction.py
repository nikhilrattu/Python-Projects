print("welcome to the blind auction\n")
data={}
cont=True

while cont:
    name = input("What is your name? \n")
    bid = int(input("What is your bid?\n$"))
    data[name] = bid
    extra_player=input("Is there any other player? type yes or no\n")
    print("\n"*100)
    if extra_player=="no":
        cont=False
highest_bid=max(data.items())
print(highest_bid)