class Inventory:
    def __init__(self, user):
        self.user = user

    def can_check_inventory(self, print_text):
        while True:
            is_potion = "red_potion" in self.user.inventory
            is_check = input(print_text)
            if is_check == 'I':
                self.user.print_inventory()
            if is_check == "y":
                return "y"
            if is_check == 'n':
                return "n"
            if is_check == "red_potion":
                if is_potion:
                    print(self.user.potion_number)
                    self.user.potion_number -= 1
                    self.user.take_potion()
                    print(self.user.potion_number)
                    if self.user.potion_number == 0:
                        self.user.inventory.pop("red_potion")
                        self.user.inventory.pop("red_potion_name")
                else:
                    print("You dont have a potion")

    def can_check_inventory_room_direction(self, print_text):
        while True:
            is_potion = "red_potion" in self.user.inventory
            is_check = input(print_text)
            if is_check == 'I':
                self.user.print_inventory()
            if is_check == "FR":
                return "FR"
            if is_check == 'TR':
                return "TR"
            if is_check == 'EM':
                return "EM"
            if is_check == "red_potion":
                if self.user.potion_number == 0:
                    print("You dont have a potion")
                else:
                    self.user.potion_number -= 1
                    self.user.take_potion()
                    if self.user.potion_number == 0:
                        self.user.inventory.pop("red_potion")
