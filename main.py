from character import Character

def main():
    hero = Character("Knight", 30, 5)
    enemy = Character("Goblin", 20, 3)
    enemy2 = Character("Dragon", 30, 5)

    print(hero)
    print(enemy)
    print(enemy2)
    print()

    while hero.is_alive() and (enemy.is_alive() or enemy2.is_alive()):
        hero.attack(enemy)
        hero.attack(enemy2)
        if enemy.is_alive():
            enemy.attack(hero)
        if enemy2.is_alive():
            enemy2.attack(hero)

        #
        if not hero.is_alive():
            hero.hp = 0
        if not enemy.is_alive():
            enemy.hp = 0
        if not enemy2.is_alive():
            enemy2.hp = 0


        print(hero)
        print(enemy)
        print(enemy2)
        print()

    print("Battle over!")
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} and {enemy2.name} wins!")

if __name__ == "__main__":
    main()
