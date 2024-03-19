from models.note import Note
from datetime import datetime
from urllib.parse import ParseResult, urlparse

class NoteBuilder:
    def __init__(self, note_id: int):
        if not isinstance(note_id, int):
            raise TypeError("note_id must be an integer.")
        
        if note_id is None:
            raise ValueError("note_id must not be None.")
        
        self.new_note = Note(note_id=note_id)

from datetime import datetime

class NotePrompter:
    def __init__(self, note_id: int):
        if not isinstance(note_id, int):
            raise TypeError("note_id must be an integer.")
        
        if note_id is None:
            raise ValueError("note_id must not be None.")
        
        self.new_note = Note(note_id=note_id)
        

    def prompt_parent_note_id(self):
        """ Prompt the user for the parent note ID. """
        parent_note_id = int(input("Enter the parent note ID (0 for no parent): "))
        self.new_note.parent_note_id = parent_note_id

    def prompt_note_color(self):
        """ Prompt the user for the note color."""
        note_color = input("Enter the note color: ")
        self.new_note.note_color = note_color

    def prompt_title(self):
        """ Prompt the user for the note title. """
        title = input("Enter the note title: ")
        while not title:
            print("Title cannot be blank.")
            title = input("Please enter a title: ")

    def prompt_ticket_id(self):
        """ Prompt the user for a ticket ID. """
        ticket_id = input("Enter the ticket ID (blank for none): ")
        self.new_note.ticket_id = ticket_id

    def prompt_ticket_link(self):
        """ Prompt the user for a ticket link. """
        ticket_link = input("Enter the ticket link (blank for none): ")
        
        if not ticket_link:
            self.new_note.ticket_link = None
            return
        invalid = True
        
        while invalid:
            try:
                ticket_url:ParseResult = urlparse(ticket_link)
                if not all([ticket_url.scheme, ticket_url.netloc]):
                    raise ValueError
                invalid = False
                self.new_note.ticket_link = ticket_url.geturl()
                return
            except ValueError:
                print("Invalid URL. Please enter a valid URL.")
                ticket_link = input("Enter the ticket link: ")
        return
        
    def prompt_priority(self):
        """ Prompt the user for the note priority."""
        
        try:
            priority = int(input("Enter the priority (0-5): "))
            if 0 <= priority <= 5:
                self.new_note.priority = priority
                return
            else:
                raise ValueError
        except ValueError:
            
    
        

    def prompt_body(self):
        """ Prompt the user for the note body."""
        body = input("Enter the note body: ")

    def prompt_parent_note_id(self):
        """ Prompt the user for the parent note ID."""
        parent_note_id = int(input("Enter the parent note ID: "))

    def prompt_status(self):
        """ Prompt the user for the note status."""
        status = int(input("Enter the status (1-5): "))

    def prompt_collaborators(self):
        """ Prompt the user for the note collaborators."""
        collaborators = input("Enter collaborators (comma-separated): ")
        collaborators = [c.strip() for c in collaborators.split(",")]

    def prompt_tags(self):
        """ Prompt the user for the note tags."""
        tags = input("Enter tags (comma-separated integers): ")
        tags = [int(t.strip()) for t in tags.split(",")]

    def prompt_attachments(self):
        attachments = input("Enter attachments (comma-separated): ")
        attachments = [a.strip() for a in attachments.split(",")]

    def prompt_urls(self):
        urls = input("Enter URLs (comma-separated): ")
        urls = [u.strip() for u in urls.split(",")]

    def prompt_child_notes(self):
        child_notes = input("Enter child note IDs (comma-separated integers): ")
        child_notes = [int(c.strip()) for c in child_notes.split(",")]

    def prompt_created_at(self):
        created_at = input("Enter the creation date and time (YYYY-MM-DD HH:MM:SS): ")
        created_at = datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S")

    def prompt_edited_at(self):
        edited_at = input("Enter the last edited date and time (YYYY-MM-DD HH:MM:SS): ")
        edited_at = datetime.strptime(edited_at, "%Y-%m-%d %H:%M:%S")

    def prompt_reminder(self):
        reminder = input("Enter the reminder date and time (YYYY-MM-DD HH:MM:SS): ")
        reminder = datetime.strptime(reminder, "%Y-%m-%d %H:%M:%S")

    def prompt_sprint_start(self):
        sprint_start = input("Enter the sprint start date and time (YYYY-MM-DD HH:MM:SS): ")
        sprint_start = datetime.strptime(sprint_start, "%Y-%m-%d %H:%M:%S")

    def prompt_sprint_end(self):
        sprint_end = input("Enter the sprint end date and time (YYYY-MM-DD HH:MM:SS): ")
        sprint_end = datetime.strptime(sprint_end, "%Y-%m-%d %H:%M:%S")

    def prompt_previous_version_backups(self):
        # This method would require additional implementation to handle Note objects
        pass
        
    