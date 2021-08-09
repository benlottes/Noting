import os
import numpy
from termcolor import cprint
from note import Note
from fileOperations import FileOperations 

os.system('color')

file_operations = FileOperations()

cont = True

while(cont):
    print("Please select an Option:")
    print("1. List Notes")
    print("2. New Note")
    print("3. Edit Note")
    print("4. Search Tags")
    print("5. Quit")
    
    selection = int(input())
    
    if selection == 1:
        for tag in file_operations.all_notes:
            cprint(tag, 'red', attrs=['bold'])
            for note in file_operations.all_notes[tag]:
                print(note.get_name() + ':')
                print(' '.join(note.get_tags())) 
                print(str(note.get_content()) + '\n')
    elif selection == 2:
        name = input('Note name: ')
        tags = input('Tags: ')
        content = input('Content: ').replace('\\n', '\n')
        file_operations.save_new_file(name, tags, content)
    elif selection == 3:
        print("Please select an Option:")
        print("1. Change Tags")
        print("2. Change Name")
        print("3. Change Content")
        sel = int(input())
        if sel == 1:
            name = input('Note name: ')
            new_tags = input('New tags: ')
            file_operations.update_tags(name, new_tags)
        elif sel == 2:
            old_name = input('Note name: ')
            new_name = input('New name: ')
            file_operations.update_name(old_name, new_name)
        elif sel == 3:
            name = input('Note name: ')
            new_text = input('New text: ').replace('\\n', '\n')
            file_operations.update_text(name, new_text)
        else:
            print('invalid input')
    elif selection == 4:
        search_tags = input("Tags: ")
        for x in file_operations.search_with_tags(search_tags):
            print(x.get_name() + '\n' + x.get_content())
    elif selection == 5:
        cont = False
    else:
        print("bad input")
