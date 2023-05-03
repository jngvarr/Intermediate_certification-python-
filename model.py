import os
import menu
import datetime

note_id_counter = 0
notes = {}

def create_note():

    new_note = dict()
    new_note['id'] = get_new_ID()
    new_note['note_title'] = input("Input note title: ")
    new_note['note_text'] = input("Input note body: ")
    new_note['create/edit_time'] = datetime.datetime.today().strftime(
        "%Y-%m-%d_%H:%M:%S")
    save_note_to_file(new_note)
    os.system("cls")
    menu.user_menu()


def get_new_ID():
    global note_id_counter
    note_id_counter = get_last_note_ID()
    note_id_counter += 1
    return note_id_counter


def get_last_note_ID():
    if isFileExists():
        with open(os.path.dirname(os.path.abspath(__file__)) + '\\notes.csv', 'r', encoding='utf-8') as file:
            lines = file.read().splitlines()
            last_line = lines[-1]
            note_id_counter = last_line[:last_line.index(";")]
            return int(note_id_counter)
    else:
        return 0

def isFileExists():
    return os.path.exists(os.path.dirname(os.path.abspath(__file__)) + '\\notes.csv')


def save_note_to_file(new_note):

    if not isFileExists():
        with open(os.path.dirname(os.path.abspath(__file__)) + '\\notes.csv', 'a', encoding='utf-8') as file:
            file.write(
                f"{'id'};{'note_title'};{'note_body'};{'create/edit_time'}\n")
            file.write(
                f"{new_note['id']};{new_note['note_title']};{new_note['note_text']};{new_note['create/edit_time']}\n")
    else:
        with open(os.path.dirname(os.path.abspath(__file__)) + '\\notes.csv', 'a', encoding='utf-8') as file:
            file.write(
                f"{new_note['id']};{new_note['note_title']};{new_note['note_text']};{new_note['create/edit_time']}\n")


def notes_list():
    dict = dictinaryCreate()
    os.system("cls")
    for k, v in dict.items():
        print('{k1:3s} : {v0:25s} {v2:20s}'.format(k1=k, v0=v[0], v2=v[2]))
        # print('%3s %s %-25s %-20s' % (k, ":", v[0], v[2]))
    print("-"*60)
    input("Press \"ENTER\" to continue ")
    menu.user_submenu(dict)


def print_note(choice, dict):
    os.system("cls")
    print("-"*60)
    print(dict[choice][0], ":", dict[choice][1])
    print("-"*60)
    input("Press \"ENTER\" to return to main menu.")
    menu.user_menu()


def dictinaryCreate():
    dict = {}
    if isFileExists():
        with open(os.path.dirname(os.path.abspath(__file__))+'\\notes.csv', 'r', encoding='utf-8') as file:
            lines = file.read().splitlines()
            for i in range(len(lines)):
                key, val = lines[i][:lines[i].index(
                    ";")], (lines[i][lines[i].index(";")+1:]).split(";")
                dict[key] = val
            return dict


def notes_byDate_list(dict, date):
    os.system("cls")
    print("-"*60)
    for k, v in dict.items():
        if v[2][:v[2].index("_")] == date:
            print('{k1:3s} : {v0:25s} {v2:20s}'.format(
                k1=k, v0=v[0], v2=v[2]))
    print("-"*60)
    input("Press \"ENTER\" to return to main menu.")
    print("-"*60)
    menu.user_menu()


def delete_note(id, dict):
    del(dict[id])
    input("Press \"ENTER\" to return to main menu.")
    save(dict)
    notes_list

def save(dict):
    with open(os.path.dirname(os.path.abspath(__file__)) + '\\notes.csv', 'w', encoding='utf-8') as file:
        for k, v in dict.items():
            file.write(
                f"{k};{v[0]};{v[1]};{v[2]}\n")
            
def edit_note(id, dict):
    dict[id][0] = input("Input new notes name: ")
    dict[id][1] = input("Input new notes text: ")
    dict[id][2] = datetime.datetime.today().strftime("%Y-%m-%d_%H:%M:%S")
    save(dict)
    notes_list()