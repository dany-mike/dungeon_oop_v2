import random


class Fight:
    def __init__(self, typewriter):
        self.typewriter = typewriter

    def start_fight(self, user, enemy, is_enemy, reward, reward_key_value, second_reward, second_reward_key_value):
        if is_enemy:
            print("")
            self.typewriter(f"A fight between {user.name} and {enemy.name} started !")
            input("")
            print("")
            while True:
                user_number = input("Choose a number '1' or '2': ")
                try:
                    user_nbr_int = int(user_number)
                except ValueError:
                    print("")
                    print("Choose 1 or 2")
                    print("")
                    continue
                print("")
                if 1 <= user_nbr_int <= 2:
                    print("")
                    self.typewriter(f"You choose {str(user_nbr_int)}")
                    break
                else:
                    print("")

            number_to_find = random.randrange(1, 3)
            self.typewriter(f"The right number was {number_to_find} !")
            print("")
            if int(user_number) == int(number_to_find):
                self.typewriter(f"{user.name} has the first attack !")
                # Fight loops
                while True:
                    self.typewriter(f"{enemy.name} has {enemy.pv} You have {user.pv} PV !")
                    # User attacks Enemy
                    user.attack(enemy)
                    input("")
                    # Enemy attacks User
                    if enemy.pv <= 0:
                        self.end_fight(reward, user, reward_key_value, second_reward, second_reward_key_value)
                        break

                    enemy.attack(user)
                    input("")
                    if user.pv <= 0:
                        self.lose_fight(user.name)
                        break
            else:
                self.typewriter(f'{enemy.name} has the first attack !')
                # Fight loops
                while True:
                    self.typewriter(f"{enemy.name} has {enemy.pv} You have {user.pv} PV !")
                    # Enemy attacks User
                    enemy.attack(user)
                    input("")
                    # If Enemy has 0 or less end (Do the same for user later)
                    if user.pv <= 0:
                        self.lose_fight(user.name)
                        break
                    # User attacks Enemy
                    user.attack(enemy)
                    input("")
                    # If Enemy has 0 or less end (Do the same for user later)
                    if enemy.pv <= 0:
                        self.end_fight(reward, user, reward_key_value, second_reward, second_reward_key_value)
                        break
        else:
            print("There is nothing to do in this room...")

    def end_fight(self, reward, user, reward_key_value, second_reward, second_reward_key_value):
        print("")
        self.typewriter(f"{user.name} wins the fight !")
        input("")
        # Key reward
        print("")
        self.typewriter(f"Congrats you find a {reward} in a treasure chest !")
        input("")
        print("")
        # Add key into the inventory
        user.inventory[reward_key_value] = reward
        if second_reward == "exit key":
            user.inventory[second_reward_key_value] = second_reward
            self.typewriter(f"There is also a {second_reward} in the treasure chest !")
            input("")
            print("")

    @staticmethod
    def lose_fight(username):
        print("")
        print(f"{username} loose the fight :( ")
        input("")
        print("you lose all your inventory :( ")
