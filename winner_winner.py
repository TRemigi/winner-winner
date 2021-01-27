import os
import pickle
from time import sleep

### Functions ###


def display_title():
    os.system('clear')
    print("\t           .---.           .---.")
    print("\t          /. ./|          /. ./|")
    print("\t      .--'.  ' ;      .--'.  ' ; ")
    print("\t     /__./ \ : |     /__./ \ : |")
    print("\t .--'.  '   \: . .--'.  '   \: .")
    print("\t/___/ \ |    ' '/___/ \ |    ' ' ")
    print("\t;   \  \;      :;   \  \;      : ")
    print("\t \   ;  `      | \   ;  `      | ")
    print("\t  .   \    .\  ;  .   \    .\  ;")
    print("\t   \   \   ' \ |   \   \   ' \ | ")
    print("\t    :   '  |--'     :   '  |--'  ")
    print("\t     \   \ ;         \   \ ;    ")
    print("\t      '---' inner     '---' inner")
    print("\t___________________________________")
    print("\n")


def main_user_input():
    display_title()
    # display user choices
    print("\n[1] Display all giveaways")
    print("[2] Add new giveaway")
    print("[3] Add entries or end a giveaway")
    print("[q] Quit")

    return input("Enter your selection: ")


def load_giveaways():
    try:
        file_object = open('giveaways.pydata', 'rb')
        giveaways = pickle.load(file_object)
        file_object.close()
        return giveaways
    except Exception as e:
        print(e)
        return {}


def load_giveaway_entries(chosen_giveaway):
    try:
        file_object = open('%s.pydata' % chosen_giveaway, 'rb')
        entries = pickle.load(file_object)
        file_object.close()
        return entries
    except Exception as e:
        print(e)
        return []


def update_giveaway():
    giveaways_list = []
    for giveaway in giveaways.keys():
        giveaways_list.append(giveaway)
    for index, giveaway_name in enumerate(giveaways_list):
        print("\n[%d] %s" % (index, giveaway_name.title()))
    user_input = input("Choose a giveaway to update: ")
    selected_giveaway = giveaways_list[int(user_input)]
    try:
        display_title()
        print("Updating: %s" % selected_giveaway)
        for entry in giveaways[selected_giveaway]:
            print(entry)
        new_entries = []
        new_entry = ''
        while new_entry != "done":
            new_entry = get_new_entry(new_entries)
            if new_entry == "done":
                for entry in new_entries:
                    print(entry)
                print("\n[y] Finished")
                print("[n] Not Finished")
                print("[x] Cancel - New entries will be lost")
                verify_entries = input(
                    "\nFinish and add these entries to giveaway?")
                if verify_entries == 'y':
                    for entry in new_entries:
                        giveaways[selected_giveaway].append(entry)
                        main_user_input()
                elif verify_entries == 'n':
                    get_new_entry()
                else:
                    main_user_input()
    except Exception as e:
        print(e)


def get_new_entry(new_entries):
    os.system('clear')
    for entry in new_entries:
        print(entry)
    new_entry = input(
        '"\nType a name to add to entries: ')
    if new_entry != "done":
        new_entries.append(new_entry)
    return new_entry


def new_giveaway_menu():
    # ask user to add new giveaway
    new_giveaway = input("Enter a name for the new giveaway: ")
    giveaways[new_giveaway.lower()] = []


def display_giveaways():
    for giveaway in giveaways:
        entrants_num = len(giveaways[giveaway])
        print("\n%s - %d Entrants" % (giveaway.title(), entrants_num))
    input("\nPress Enter to return: ")


def quit():
    try:
        file_object = open('giveaways.pydata', 'wb')
        pickle.dump(giveaways, file_object)
        file_object.close()
        print("\nThanks!")
    except Exception as e:
        print(e)


### Start of Program ###
giveaways = load_giveaways()

choice = ''
display_title()
while choice != 'q':
    choice = main_user_input()

    # display appropriate menu/data based on user input
    display_title()
    if choice == '1':
        display_giveaways()
    elif choice == '2':
        new_giveaway_menu()
    elif choice == '3':
        update_giveaway()
    elif choice == 'q':
        quit()
    else:
        print("\nI didn't understand that choice (>_<)\n")
