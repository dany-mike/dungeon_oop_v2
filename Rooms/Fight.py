class Fight:

    def start_fight(self, user, enemy, is_enemy, reward, reward_key_value, second_reward, second_reward_key_value):
        if is_enemy:
            print("")
            print(f"A fight between {user.name} and {enemy.name} started !")
            print("")
            # Fight loops
            while True:
                print(f"{enemy.name} has {enemy.pv} You have {user.pv} PV !")
                # User attacks Goblin
                user.attack(enemy)
                # If Goblin has 0 or less end (Do the same for user later)
                if enemy.pv <= 0:
                    self.end_fight(reward, user, reward_key_value, second_reward, second_reward_key_value)
                    break
                # Goblin attacks User
                enemy.attack(user)
                # If Goblin has 0 or less end (Do the same for user later)
                if enemy.pv <= 0:
                    self.end_fight(reward, user, reward_key_value, second_reward, second_reward_key_value)
                    break
        else:
            print("There is nothing to do in this room...")

    @staticmethod
    def end_fight(reward, user, reward_key_value, second_reward, second_reward_key_value):
        print("")
        print(f"{user.name} wins the fight !")
        # Key reward
        print("")
        print(f"Congrats you find a {reward} in a treasure chest !")
        print("")
        # Add key into the inventory
        user.inventory[reward_key_value] = reward
        if second_reward == "exit key":
            user.inventory[second_reward_key_value] = second_reward
            print(f"There is also a {second_reward} in the treasure chest !")
            print("")
