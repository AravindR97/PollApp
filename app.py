import database as db

welcome = "\nWelcome to Poll App!"

menu = """\n1) Create new poll
2) List open polls
3) Vote on a poll
4) Show poll votes
5) Select a random winner from a poll option
6) Exit

Enter your choice: 
"""

print(welcome)
choice = int(input(menu))

while choice:
    if choice == 1:
        title = input("\nEnter the title of the poll: ")
        owner = input("\nEnter the poll owner\'s name: ")
        db.new_poll(title, owner)
    elif choice == 2:
        print(db.get_polls())
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        pass
    else:
        break
    choice = int(input(menu))

