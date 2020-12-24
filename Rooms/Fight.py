class Fight:

    def start_fight(self, user, enemy, is_enemy, reward, reward_key_value):
        if is_enemy:
            print(f"A fight between {user.name} and {enemy.name} started !")
            # Fight loops
            while True:
                print(f"{enemy.name} has {enemy.pv} You have {user.pv} PV !")
                # User attacks Goblin
                user.attack(enemy)
                # If Goblin has 0 or less end (Do the same for user later)
                if enemy.pv <= 0:
                    self.end_fight(reward, user, reward_key_value, is_enemy)
                    break
                # Goblin attacks User
                enemy.attack(user)
                # If Goblin has 0 or less end (Do the same for user later)
                if enemy.pv <= 0:
                    self.end_fight(reward, user, reward_key_value, is_enemy)
                    break
        else:
            print("There is nothing to do in this room...")

    @staticmethod
    def end_fight(reward, user, reward_key_value, is_enemy):
        print("")
        print(f"{user.name} wins the fight !")
        # Key reward
        print("")
        print("Congrats you win a key")
        # Add key into the inventory
        user.inventory[reward_key_value] = reward
