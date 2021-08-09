import os
import numpy

from note import Note

# Need to make all tags lowercase so caps dont matter


class FileOperations:

    def __init__(self):
        # Directory for note files
        self.note_file = os.getcwd() + ('\\notes\\')
        
        # A dictionary with keys cooresponding to every tag used in all the notes
        self.all_notes = {}
        self.store_notes()
    
    # note_name: String, no .txt | tags: List of Strings | note_content: String
    def _update_dict(self, note_name, tags, note_content):
        note = Note(note_name, tags, note_content)
        for tag in tags:
            if tag in self.all_notes:
                self.all_notes[tag].append(note)
            else:
                self.all_notes[tag] = [note]
    
    # note_name: String, no .txt | tags: String, spaces in between | note_content: String
    def save_new_file(self, note_name, tags, note_content):        
        try:
            f = open(self.note_file + note_name + '.txt', 'x')
            tags = tags + ' ' + note_name
            f.write(tags + '\n' + note_content)
            f.close()
            
            self._update_dict(note_name, tags.strip().split(), note_content)
            return True
        except FileExistsError:
            print('FileExistsError Thrown')
            return False

    # Generates dictionary in form {'tag', [Each, note, with, tag]}
    def store_notes(self):
        note_names = os.listdir(self.note_file)
        for note_name in note_names:
            with open(self.note_file + note_name) as f:
                tags = f.readline().strip().split()
                self._update_dict(note_name.split('.')[0], tags, ''.join(f.readlines()))
    
    # note_name: String, no .txt | new_tags: String, seperated by spaces
    def update_tags(self, note_name, new_tags):
        with open(self.note_file + note_name + '.txt', 'r+') as f:
            lines = f.readlines()
            old_tags = lines[0].strip().split()
            note_content = lines[1:]
            new_tags = new_tags + ' ' + note_name
            lines[0] = (new_tags + '\n')
            f.seek(0)
            f.truncate(0)
            f.writelines(lines)
            
            print(old_tags)
            for tag in old_tags:
                for i, note in enumerate(self.all_notes[tag]):
                    if note.get_name() == note_name:
                        del self.all_notes[tag][i]
                        break
            del self.all_notes[note_name]
            print(new_tags.strip().split())
            self._update_dict(note_name, new_tags.strip().split(), ''.join(note_content))

    # search_list: List sent from search_with_tags
    def _order_search(self, search_list):
        return sorted(set(search_list), key = lambda ele: search_list.count(ele), reverse = True)
    
    # search_tags: String, seperated by spaces
    def search_with_tags(self, search_tags):
        search_tags = search_tags.strip().split()
        matches = []
        for tag in search_tags:
            if tag in self.all_notes:
                matches.extend(self.all_notes[tag])
        return self._order_search(matches)
    
    # Doesn't work
    # note_name: String, no .txt | new_text: String with newlines
    def update_text(self, note_name, new_text):
        with open(self.note_file + note_name + '.txt', 'r+') as f:
            lines = f.readlines()
            tags = lines[0].strip().split()
            lines[1:] = new_text
            f.seek(0)
            f.truncate(0)
            f.writelines(lines)
            
            for tag in tags:
                for i, note in enumerate(self.all_notes[tag]):
                    if note.get_name() == note_name:
                        del self.all_notes[tag][i]
                        break
            del self.all_notes[note_name]
            self._update_dict(note_name, tags, new_text)
    
    # old_name: String, no .txt | new_name: String, no .txt
    def update_name(self, old_name, new_name):
        try:
            os.rename(self.note_file + old_name + '.txt', self.note_file + new_name + '.txt')

            with open(self.note_file + new_name + '.txt', 'r+') as f:
                lines = f.readlines()
                old_tags = lines[0]
                tags = old_tags.split()[:-1][0] + ' ' + new_name
                note_content = lines[1:]
                lines[0] = (tags + '\n')
                f.seek(0)
                f.truncate(0)
                f.writelines(lines)
                
                for tag in old_tags.strip().split():
                    for i, note in enumerate(self.all_notes[tag]):
                        if note.get_name() == old_name:
                            del self.all_notes[tag][i]
                            break
                del self.all_notes[old_name]
                self._update_dict(new_name, tags.strip().split(), ''.join(note_content))
            return True
        except(FileExistsError):
            print('FileExistsError Thrown')
            return False

f = FileOperations()

