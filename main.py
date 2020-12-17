from User.User import User

while True:
    def main():
        print("Welcome in the dungeon game !")
        user = User("Link", 100)
        user.go_in_dungeon()

    if __name__ == '__main__':
        main()

    is_restart = input("Do you want to restart ?: (yes/no): ")
    if is_restart == 'yes':
        print("Let's restart !")
    else:
        print("Bye bye see you soon!")
        break
