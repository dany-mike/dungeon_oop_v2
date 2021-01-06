class Inventory:
    def __init__(self, user):
        self.user = user

    def can_check_inventory(self, print_text):
        while True:
            is_check = input(print_text)
            if is_check == 'I':
                self.user.print_inventory()
            if is_check == "y":
                return "y"
            if is_check == 'n':
                return "n"

    def can_check_inventory_room_direction(self, print_text):
        while True:
            is_check = input(print_text)
            if is_check == 'I':
                self.user.print_inventory()
            if is_check == "FR":
                return "FR"
            if is_check == 'TR':
                return "TR"
            if is_check == 'EM':
                return "EM"

