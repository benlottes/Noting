import os
import numpy

class FileOperations:

    def __init__(self):
        self.note_file = os.getcwd() + ('\\notes\\')
        self.all_notes = self.store_notes();

    def save_new_file(self, note_name, tags, note_content):
        try:
            f = open(self.note_file + note_name + '.txt', 'x')
            f.write(tags + '\n' + note_content)
            f.close()
            self.all_notes[note_name] = tags.split()
            return True
        except FileExistsError:
            return False

    #Dictionary in form {'Name of note', [tags, for, note]}            
    def store_notes(self):
        note_names = os.listdir(self.note_file)
        notes = {}
        for name in note_names:
            with open(self.note_file + name) as f:
                tags = f.readline().strip().split()
                notes[name] = tags
        print(notes)
        return notes

    def update_tags(self, note_name, new_tags):
        self.all_notes[note_name] = new_tags.split()
        with open(self.note_file + note_name, 'r+') as f:
            lines = f.readlines()
            lines[0] = (new_tags + '\n')
            
            f.seek(0)
            f.truncate(0)
            f.writelines(lines)
    
    def _match_tags(self, saved_tags, search_tags):
        search_set = set(search_tags)
        common_set = search_set.intersection(saved_tags)
        return(list(common_set))
    
    def search_with_tags(self, search_tags):
        all_matches = [[] for _ in range(len(search_tags))]
        print(all_matches)
        for note in self.all_notes:
            print(self.all_notes[note])
            matched_tags = self._match_tags(self.all_notes[note], search_tags)
            print(matched_tags)
            print(len(search_tags)-len(matched_tags))
            all_matches[len(search_tags)-len(matched_tags)].insert(0, note)
        return all_matches
    
    def get_text(self, note_name):
        with open(self.note_file + note_name) as f:
            text_array = f.readlines()[1:]
            text = ''
            for line in text_array:
                text = text + line
            return text
            
    def update_text(self, note_name, new_text):
        with open(self.note_file + note_name, 'r+') as f:
            tags = f.readline()
            f.seek(0)
            f.truncate(0)
            
            f.write(tags)
            f.write(new_text)
    
f = FileOperations()

