import model
import re
import os


def user_menu():
    os.system("cls")
    menu_items = {1: "Create new note",
                  2: "Notes list",
                  3: "Close app"}

    choice = int(input(f'Chose the action: \n\n'+''.join(str(k) + ". "
                                                         + str(v) + ' - press ' + str(k) + "." + '\n' for k, v in menu_items.items())+" -> "))
    while choice not in menu_items.keys():
        choice = int(input("Wrong choise, try again: "))
    if choice == 1:
        model.create_note()
    if choice == 2:
        model.notes_list()


def user_submenu(dict):

    menu_items = {1: "To print note by number type notes ID: ",
                  2: "To print note by date type date in format \"YYYY-MM-DD\": ",
                  3: "To edit note type: \"edit ID_number: \"",
                  4: "To delete note type: \"delete ID_number: \"",
                  5: "To enter previous menu type \"back\": "}
    print("-" * 60 + "\n")
    for k, v in menu_items.items():
        print(k, ".", v)
    print("-"*60)

    choice = input("Chose the action: ")
    pattern_date_format = r'^\d{4}-\d{2}-\d{2}$'
    if re.match(pattern_date_format, choice):
        model.notes_byDate_list(dict, choice)
    elif "edit" in choice:
        note_to_edit = choice[choice.index(" ")+1:]
        model.edit_note(note_to_edit, dict)
    elif "delete" in choice:
        note_to_delete = choice[choice.index(" ")+1:]
        model.delete_note(note_to_delete, dict)
    elif choice in dict.keys():
        model.print_note(choice, dict)
    elif choice == "back":
        user_menu()
    else:
        print("Wrong input, try again")
        user_submenu(dict)