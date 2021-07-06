import os

class Note:
    
    def __init__(self, note_tags, note_name, note_content):
        this.name = note_name
        this.tags = note_tags
        this.content = note_content
        this.dir_path = os.getcwd() + '\\notes\\' + note_name
    
    # Content should be a string
    def get_content(self):
        return this.content
    
    def update_content(self, new_content):
        this.content = new_content
    
    # Name should be a string
    def get_name(self):
        return this.name
        
    def update_name(self, new_name):
        this.name = new_name
        this.dir_path = ow.getcwd() + '\\notes\\' + new_name
    
    
    # Tags should be an array of strings
    def get_tags(self):
        return this.tags
    
    def update_tags(self, new_tags):
        this.tags = new_tags
