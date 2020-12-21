from Rooms.Room import Room
from Enemies.Goblin import Goblin


class FightRoom(Room):
    goblin = Goblin("Goblin", 50)

    def __init__(self, room_name, user):
        super().__init__(room_name)
        self.user = user
        self.is_gobelin = True

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
                self.user.attack(goblin)
               
                if goblin.pv <= 0:
                    print(f"{self.user.name} wins the fight !")
                    self.is_gobelin = False
                    # Key reward
                    print("Congrats you win a key")
                    break
        else:
            print("There is nothing to do in this room...")


