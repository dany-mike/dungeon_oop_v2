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
                print(goblin.pv)
                attack_choice = input("What do you want to do ? 'sword_attack' 'block_shield' ('magic_attack' -10PV )")
                if attack_choice == 'sword_attack':
                    print(f"{self.user.name} uses the Sword Attack !")
                    goblin.pv -= self.user.inventory['sword_attack']
                if attack_choice == 'magic_attack':
                    print()
                # User win if goblin does not have pv
                print(goblin.pv)
                if goblin.pv <= 0:
                    print(f"{self.user.name} wins the fight !")
                    self.is_gobelin = False
                    # Key reward
                    print("Congrats you win a key")
                    break
        else:
            print("There is nothing to do in this room...")


