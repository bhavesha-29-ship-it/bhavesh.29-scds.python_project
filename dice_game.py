# Name : A.Bhavesh
# ID : scds/2025/1069
# Collaborators : Bhavesh, Vamsi Krishna, Bhuvaneswar

import random

def create_enemy(level):
    names = ["Goblin", "Skeleton", "Orc"]
    name = random.choice(names)
    hp = random.randint(15, 25) + level * 3
    return {"name": name, "hp": hp}

def battle(player):
    enemy = create_enemy(player["level"])
    print(f"\n{enemy['name']} appears! HP: {enemy['hp']}")

    while player["hp"] > 0 and enemy["hp"] > 0:

        print(f"\n{player['name']} HP: {player['hp']} | Potions: {player['potions']} | Score: {player['score']}")
        print(f"{enemy['name']} HP: {enemy['hp']}")

        print("\n1. Attack")
        print("2. Heal")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":

            damage = random.randint(1, 6)

            # Critical hit chance
            if damage == 6:
                damage *= 2
                print("CRITICAL HIT!")

            enemy["hp"] -= damage
            player["score"] += damage

            print(f"You dealt {damage} damage!")

        elif choice == "2":

            if player["potions"] > 0:

                heal = random.randint(6, 12)
                player["hp"] += heal
                player["potions"] -= 1

                print(f"Healed {heal} HP")

            else:
                print("No potions!")
                continue

        else:
            print("Invalid choice")
            continue

        # Enemy attack
        if enemy["hp"] > 0:

            enemy_damage = random.randint(3, 8)
            player["hp"] -= enemy_damage

            print(f"Enemy dealt {enemy_damage} damage")

    # Player wins
    if player["hp"] > 0:

        print(f"Defeated {enemy['name']}!")

        player["level"] += 1
        player["potions"] += 1
        player["score"] += 20   # Bonus points

        return True

    else:
        print("You died!")
        return False

def game():

    print("=== Competitive Battle Game ===")

    name = input("Enter your name: ")

    player = {
        "name": name,
        "hp": 30,
        "level": 1,
        "potions": 2,
        "score": 0
    }

    while True:

        alive = battle(player)

        if not alive:
            break

        print("\nContinue? (y/n)")

        if input("> ").lower() != "y":
            break

    print("\n=== GAME OVER ===")
    print(f"Final Score: {player['score']}")
    print(f"Final Level: {player['level']}")

game()
