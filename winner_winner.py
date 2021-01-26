import os
import pickle
from time import sleep

### Functions ###


def display_title():
    os.system('clear')
    print("\t***********************************************")
    print("\t***************  WINNER WINNER  ***************")
    print("\t***********************************************")


def main_user_input():
    os.system('clear')
    # display user choices
    print("\n[1] Display all giveaways")
    print("[2] Select givaway to add entries or complete")
    print("[3] Add new giveaway")
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
        return []


def load_giveaway_entries(chosen_giveaway):
    try:
        file_object = open('%s.pydata' % chosen_giveaway, 'rb')
        entries = pickle.load(file_object)
        file_object.close()
        return entries
    except Exception as e:
        print(e)
        return []


def prev_giveaways_menu():
    for index, giveaway in enumerate(giveaways):
        print("\n[%d] %s" % (index, giveaway))
    user_selection = input("Enter your selection: ")
    selected_giveaway = giveaways[user_selection]
    print("\n%s" % selected_giveaway)


def add_giveaway_menu():
    # ask user to add new giveaway
    new_giveaway = input("Enter a name for the new giveaway: ")
    giveaways.append(new_giveaway)


def display_giveaways():
    for giveaway in giveaways:
        print("\n%s" % giveaway)
    input("\nPress Enter to return: ")


def quit():
    try:
        file_object = open('giveaways.pydata', 'wb')
        pickle.dump(giveaways, file_object)
        file_object.close()
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
        prev_giveaways_menu()

    elif choice == '3':
        add_giveaway_menu()
