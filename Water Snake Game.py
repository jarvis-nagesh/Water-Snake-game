# Snake Water Gun Game :
import random

user = input("Enter Your Name\n")
list = [1,2,3]
n = 1
user_points=0
comp_points=0

while(n<=10):
    comp = random.choice(list)  # 1.Water 2.Snake 3.Gun
    print(f"\nPOINTS: Computer:{comp_points},{user}:{user_points}")
    print("1.Water\t2.Snake\t3.Gun")
    user_input = int(input("Select Your choice\n"))

    # Both Water
    if comp==1 and user_input==1:
        print(f"Computer : Water , {user} : Water")
        print("Tie, Both Choose Water\n")
        n=n+1
        continue
    # comp-water and user-snake
    elif comp==1 and user_input==2:
        print(f"Computer : Water , {user} : Snake")
        print("Congrats: Snake Won\n")
        user_points = user_points +1
        n=n+1
        continue

    # comp-water and user-gun
    elif comp==1 and user_input==3:
        print(f"Computer : Water\t{user} : Gun")
        print("Ohho..! Water Won\n")
        comp_points = comp_points +1
        n = n + 1
        continue

    # Both have Snake
    elif comp==2 and user_input==2:
        print(f"Computer : Snake , {user} : Snake")
        print("Tie, Both Choose Snake\n")
        n=n+1
        continue

    # Comp-Snake and User-Water
    elif comp==2 and user_input==1:
        print(f"Computer : Snake\t{user} : Water")
        print("Ohho..! Snake Won\n")
        comp_points = comp_points +1
        n = n + 1
        continue

    #Comp-Snake and User-Gun
    elif comp==2 and user_input==3:
        print(f"Computer : Snake\t{user} : Gun")
        print("Congrats: Gun Won\n")
        user_points = user_points +1
        n = n + 1
        continue

    # Both have Gun
    elif comp==3 and user_input==3:
        print(f"Computer : Gun , {user} : Gun")
        print("Tie, Both Choose GUn\n")
        n=n+1
        continue

    # Comp-Gun and user-water
    elif comp==3 and user_input==1:
        print(f"Computer : Gun\t{user} : Water")
        print("Congrats: Water Won\n")
        user_points = user_points +1
        n = n + 1
        continue

    # Comp-Gun and User-Snake
    elif comp==3 and user_input==2:
        print(f"Computer : Gun\t{user} : Snake")
        print("Ohho..! Gun Won\n")
        comp_points = comp_points + 1
        n = n + 1
        continue

# Score and Result
# If Computer Win
if comp_points > user_points:
    print("Sorry..!, You Are Lose.\n")
    print(f"\t\t\tSCORE:\n\t\t\tComputer:{comp_points},{user}:{user_points}")
    print("Thanks For Playing...!")

# If User Win
elif comp_points < user_points:
    print("Congratulation..!, You Win, Well Played.\n")
    print(f"\t\t\tSCORE:\n\t\t\tComputer:{comp_points},{user}:{user_points}")
    print("Thanks For Playing...!")

# If Tied
else:
    print("Match Draw..!")
    print(f"\t\t\tSCORE:\n\t\t\tComputer:{comp_points},{user}:{user_points}")
    print("Thanks For Playing...!")