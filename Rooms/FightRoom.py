from Rooms.Room import Room
from Enemies.Goblin import Goblin


class FightRoom(Room):
    goblin = Goblin("Goblin", 50)

    def __init__(self, room_name, user, reward):
        super().__init__(room_name)
        self.user = user
        self.is_gobelin = True
        self.reward = reward

    def v_fight_room(self, goblin):
        print(f"{self.user.name} enters in the FR room.. ")
        print("")
        self.start_fight(self.user, goblin)

    # Start fight function or nothing if already fight
    def start_fight(self, user, goblin):
        if self.is_gobelin:
            print(f"A fight between {user.name} and {goblin.name} started !")
            # Fight loops
            while True:
                print(f"{goblin.name} has {goblin.pv} You have {self.user.pv} PV !")
                # User attacks Goblin
                self.user.attack(goblin)
                # If Goblin has 0 or less end (Do the same for user later)
                if goblin.pv <= 0:
                    self.end_fight()
                    break
                # Goblin attacks User
                self.goblin.attack(self.user)
                # If Goblin has 0 or less end (Do the same for user later)
                if goblin.pv <= 0:
                    self.end_fight()
                    break
        else:
            print("There is nothing to do in this room...")

    def end_fight(self):
        print("")
        print(f"{self.user.name} wins the fight !")
        self.is_gobelin = False
        # Key reward
        print("")
        print("Congrats you win a key")
        # Add key into the inventory
        print("")
