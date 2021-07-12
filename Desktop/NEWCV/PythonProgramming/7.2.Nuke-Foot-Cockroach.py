import random

number = random.randint(1, 3)

if number == 1:
    chosen1 = "Foot"
elif number == 2:
    chosen1 = "Nuke"
else:
    chosen1 = "Cockroach"
count = 0
wins = 0
ties = 0
while True:
    chosen2 = input("Foot, Nuke or Cockroach? (Quit ends): ")

    if (chosen1 == "Nuke" and chosen2 == "Nuke"):
        print("You chose:", chosen2)
        print("Computer chose:", chosen1)
        print("You LOSE!")
        count += 1
    elif chosen1 == chosen2:
        print("You chose:", chosen2)
        print("Computer chose:", chosen1)
        print("It is a tie!")
        count += 1
        ties += 1
    elif (chosen1 == "Foot" and chosen2 == "Cockroach"):
        print("You chose:", chosen2)
        print("Computer chose:", chosen1)
        print("You LOSE!")
        count += 1
    elif (chosen2 == "Foot" and chosen1 == "Cockroach"):
        print("You chose:", chosen2)
        print("Computer chose:", chosen1)
        print("You WIN!")
        count += 1
        wins += 1
    elif (chosen1 == "Nuke" and chosen2 == "Foot"):
        print("You chose:", chosen2)
        print("Computer chose:", chosen1)
        print("You LOSE!")
        count += 1
    elif (chosen2 == "Nuke" and chosen1 == "Foot"):
        print("You chose:", chosen2)
        print("Computer chose:", chosen1)
        print("You WIN!")
        count += 1
        wins += 1
    elif (chosen1 == "Cockroach" and chosen2 == "Nuke"):
        print("You chose:", chosen2)
        print("Computer chose:", chosen1)
        print("You LOSE!")
        count += 1
    elif (chosen2 == "Cockroach" and chosen1 == "Nuke"):
        print("You chose:", chosen2)
        print("Computer chose:", chosen1)
        print("You WIN!")
        count += 1
        wins += 1
    elif chosen2 == "Quit":
        print("You played", count, "rounds, and won", wins,
              "rounds, playing tie in", ties, "rounds.")
        break
    else:
        print("Incorrect selection.")
