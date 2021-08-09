import os

class Note:
    
    def __init__(self, note_name, note_tags, note_content):
        self.name = note_name
        self.tags = note_tags
        self.content = note_content
        self.dir_path = os.getcwd() + '\\notes\\' + note_name
    
    # Content should be a string
    def get_content(self):
        return self.content
    
    def update_content(self, new_content):
        self.content = new_content
    
    # Name should be a string
    def get_name(self):
        return self.name
        
    def update_name(self, new_name):
        self.name = new_name
        self.dir_path = os.getcwd() + '\\notes\\' + new_name

    # Tags should be an array of strings
    def get_tags(self):
        return self.tags
    
    def update_tags(self, new_tags):
        self.tags = new_tags
