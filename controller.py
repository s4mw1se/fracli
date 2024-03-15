import json
from note import Note
from datetime import datetime, timedelta

class Controller:
    """A class to represent a controller for working with notes."""
    def __init__(self):
        self.notes:list[str] = []
        
    def clean_tags(self, tags:list[str]):
        """Remove duplicate tags."""
        if len(tags) == 0:
            return []
        
        tags = [tag.lower().strip() for tag in tags]
        return list(set(tags))
    
    def get_reminder_date(self, days:int):
        return datetime.now() + timedelta(days=days)
        
    def create_note(self, parent_id:int = None):
        new_note_id = len(self.notes)
        
        if parent_id:
            parent_note = self.get_note_by_id(parent_id)
        
        parent_note = None
        if parent_id:
            parent_note = self.get_note_by_id(parent_id)
        
        note = Note(new_note_id, parent_note=parent_note)
        note.title = input("Enter title: ")
        note.body = input("Enter body: ")
        note.priority = int(input("Enter priority: "))
        note.status = int(input("Enter status: "))
        tags_input = input("Enter tags: ").split()
        note.tags = self.clean_tags(tags_input)
        note.created_at = datetime.now()
        note.edited_at = datetime.now()
        note.reminder = input("Remind in how many days? (0 for no reminder): ")
        self.notes.append(note)


    def get_note_by_id(self, note_id:int):
        """Get a note by its id."""
        return self.notes[note_id]