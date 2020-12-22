from Rooms.Room import Room
from Enemies.DarkUser import DarkUser


class MiniBossRoom(Room):
    dark_user = DarkUser("Dark User", 100)

    def __init__(self, room_name, user, is_dark_user, reward):
        super().__init__(room_name)
        self.user = user
        self.is_dark_user = is_dark_user
        self.reward = reward

    def v_mini_boss_room(self, dark_user):
        print(f"{self.user.name} enters in the FR room.. ")
        print("")
        self.start_fight(self.user, dark_user)

    def start_fight(self, user, dark_user):
        if self.is_dark_user:
            print(f"A fight between {user.name} and {dark_user.name} started !")
            # Fight loops
            while True:
                print(f"{dark_user.name} has {dark_user.pv} You have {self.user.pv} PV !")
                # User attacks Goblin
                self.user.attack(dark_user)
                # If Goblin has 0 or less end (Do the same for user later)
                if dark_user.pv <= 0:
                    self.end_fight()
                    break
                # Goblin attacks User
                self.dark_user.attack(self.user)
                # If Goblin has 0 or less end (Do the same for user later)
                if dark_user.pv <= 0:
                    self.end_fight()
                    break
        else:
            print("There is nothing to do in this room...")

    def end_fight(self):
        print("")
        print(f"{self.user.name} wins the fight !")
        self.is_dark_user = False
        # Key reward
        print("")
        print("Congrats you win the boss key")
        # Add key into the inventory
        self.user.inventory["boss_key"] = self.reward
