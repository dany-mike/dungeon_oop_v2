class Inventory:
    def __init__(self, user):
        self.user = user

    def can_check_inventory(self, print_text):
        is_red_potion = "red_potion" in self.user.inventory

        while True:
            is_check = input(print_text)
            if is_check == 'I':
                self.user.print_inventory()
            self.change_sword(is_check)
            if is_check == "y":
                return "y"
            if is_check == 'n':
                return "n"
            if is_red_potion:
                if is_check == "red_potion":
                    if self.user.potion_number > 0:
                        self.user.potion_number -= 1
                        self.user.take_potion()
            else:
                print("You dont have potion")
                print("")

    def can_check_inventory_room_direction(self, print_text):
        is_red_potion = "red_potion" in self.user.inventory

        while True:
            is_check = input(print_text)
            if is_check == 'I':
                self.user.print_inventory()
            self.change_sword(is_check)
            if is_check == "FR":
                return "FR"
            if is_check == 'TR':
                return "TR"
            if is_check == 'EM':
                return "EM"
            if is_red_potion:
                if is_check == "red_potion":
                    if self.user.potion_number > 0:
                        self.user.potion_number -= 1
                        self.user.take_potion()
            else:
                print("You dont have potion")
                print("")

    def change_sword(self, input_text):
        if input_text == "excalibur":
            self.user.active_sword = "Excalibur"
            print("Excalibur equipped !")
        if input_text == "royal_sword":
            self.user.active_sword = "Royal Sword"
            print("Royal Sword equipped !")
        if input_text == "fire_sword":
            self.user.active_sword = "Fire Sword"
            print("Fire sword equipped !")
