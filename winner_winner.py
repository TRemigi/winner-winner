import os
import pickle
from time import sleep

### Functions ###

# Displays program title


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

# Displays main menu


def main_user_input():
    display_title()
    # display user choices
    print("\n[1] Display all giveaways")
    print("[2] Add new giveaway")
    print("[3] Add entries or end a giveaway")
    print("[q] Quit")

    return input("Enter your selection: ")

# Loads giveaways from pickle file, or creates it


def load_giveaways():
    try:
        file_object = open('giveaways.pydata', 'rb')
        giveaways = pickle.load(file_object)
        file_object.close()
        return giveaways
    except Exception as e:
        print(e)
        return {}

# Initiates process of adding entries to an existing giveaway


def update_giveaway():
    # Create a list of all giveaways and ask user to select one to update
    giveaways_list = []
    for giveaway in giveaways.keys():
        giveaways_list.append(giveaway)
    for index, giveaway_name in enumerate(giveaways_list):
        print("[%d] %s" % (index, giveaway_name.title()))
    user_input = input("Choose a giveaway to update: ")
    # Use user input to grab correct key from giveaways dictionary
    selected_giveaway = giveaways_list[int(user_input)]
    try:
        # Create a list to hold new entries until they are pushed to dictionary key
        new_entries = []
        # Instantiate variable to hold results of new entry input
        new_entry = ''
        while new_entry != "done":
            # Pass get_new_entry function the new_entries list and selected_giveaway. See function.
            new_entry = get_new_entry(new_entries, selected_giveaway)
            # if input was 'done', print all new entries and ask user if they want to finish and add, continue adding more, or cancel
            if new_entry == "done":
                for entry in new_entries:
                    print(entry)
                print("\n[f] Finished")
                print("[n] Not Finished")
                print("[x] Cancel - New entries will be lost")
                verify_entries = ''
                verify_entries = input(
                    "\nFinish and add these entries to giveaway?")
                # If finished, append new entries to selected giveaways key
                if verify_entries == 'f':
                    for entry in new_entries:
                        giveaways[selected_giveaway].append(entry)
                        # If not finished, return to get_new_entry menu to continue adding
                elif verify_entries == 'n':
                    new_entry = get_new_entry(new_entries, selected_giveaway)
                    # Cancel new entries and return to main menu
                elif verify_entries == 'x':
                    break
                else:
                    print("\nI don't understand that command (>_<)")
    except Exception as e:
        print(e)

# Gets user input to add one or more new entries to selected giveaway


def get_new_entry(new_entries, selected_giveaway):
    # Display title and print giveaway + existing entries
    display_title()
    print("Updating: %s" % selected_giveaway.title())
    print("\nExisting Entries:")
    for entry in giveaways[selected_giveaway]:
        print(entry.title())
        # Print any entries that are ready to be added
    print("\nNew entries:")
    for entry in new_entries:
        print(entry.title())
    print("\nType a name to enter into the giveaway.")
    # Get user input. If it's anything other than 'done', add it to the new_entries array, then return it.
    new_entry = input(
        "Enter 'done' when finished: ")
    if new_entry != "done":
        new_entries.append(new_entry)
    return new_entry

# Menu to add new giveaway to the giveaways dictionary


def new_giveaway_menu():
    # ask user to add new giveaway
    new_giveaway = input("Enter a name for the new giveaway: ")
    giveaways[new_giveaway.lower()] = []

# Displays all giveaways


def display_giveaways():
    for giveaway in giveaways:
        entrants_num = len(giveaways[giveaway])
        print("%s - %d Entries" % (giveaway.title(), entrants_num))
    input("\nPress Enter to return: ")

# Quits the app after saving giveaways dictionary to pickle


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
