from Rooms.Room import Room
from Enemies.Goblin import Goblin
from Rooms.Fight import Fight


class FightRoom(Room):
    goblin = Goblin("Goblin", 50)

    def __init__(self, room_name, user, reward, typewriter):
        super().__init__(room_name, typewriter)
        self.user = user
        self.is_gobelin = True
        self.reward = reward

    def v_fight_room(self, goblin):
        self.typewriter(f"{self.user.name} enters in the FR room.. ")
        input("")
        print("")
        # Call fight instance
        fight = Fight(self.typewriter)
        # execute start_fight and end_fight method in Fight.py
        fight.start_fight(self.user, goblin, self.is_gobelin, self.reward, "key", "", "")
        self.is_gobelin = False
