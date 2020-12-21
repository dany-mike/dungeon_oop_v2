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

    def start_fight(self, user, goblin):
        if self.is_gobelin:
            print(f"A fight between {user.name} and {goblin.name} started !")
            while True:
                print(f"{goblin.name} has {goblin.pv} You have {self.user.pv} PV !")
                attack_choice = input("What do you want to do ? 'sword_attack' 'magic_attack' (-10PV): "
                                      "")
                if attack_choice == 'sword_attack':
                    print(f"{self.user.name} uses the Sword Attack !")
                    goblin.pv -= self.user.inventory['sword_attack']
                    print(f"{goblin.name} loose {self.user.inventory['sword_attack']} PV !")
                if attack_choice == 'magic_attack':
                    print(f"{self.user.name} uses the Magic Attack !")
                    goblin.pv -= self.user.inventory['magic_attack']
                    print(f"{goblin.name} loose {self.user.inventory['magic_attack']} PV !")
                    self.user.pv -= 10
                    print(f"But {self.user.name} loose 10 PV")
                # User win if goblin does not have pv
                if goblin.pv <= 0:
                    print(f"{self.user.name} wins the fight !")
                    self.is_gobelin = False
                    # Key reward
                    print("Congrats you win a key")
                    break
        else:
            print("There is nothing to do in this room...")


