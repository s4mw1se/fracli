"""A module to represent a note."""

import json
from datetime import datetime


class Note:
    """A class to represent a note."""
    def __init__(self, note_id:int, parent_note:'Note'= None):
        self.note_id:int = note_id
        self.note_color:str
        self.title:str
        self.ticket_id:str
        self.ticket_link:str
        self.priority:int
        self.body:str
        self.parent_note_id:int
        self.status:int
        self.collaborators:list[str]
        self.tags:list[int]
        self.attachments:list[str]
        self.urls:list[str]
        self.child_notes:list[int]
        self.created_at:datetime = datetime.now()
        self.edited_at:datetime
        self.reminder:datetime
        self.spirnt_start:datetime
        self.sprint_end:datetime
        self.previous_version_backup:list[Note] # store previous versions of the note when edited
        
        if parent_note:
            self.notebook = parent_note.notebook
            self.parent_note_id = parent_note.note_id
        
       
    def to_json(self):
        dateformat = "%Y-%m-%d %H:%M"
        
        self.created_at = self.created_at.strftime(dateformat)
        self.edited_at = self.edited_at.strftime(dateformat)
        self.reminder = self.reminder.strftime(dateformat)
        self.spirnt_start = self.spirnt_start.strftime(dateformat)
        self.sprint_end = self.sprint_end.strftime(dateformat)
        
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
        
