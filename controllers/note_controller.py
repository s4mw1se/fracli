from models.note import Note
from datetime import datetime

class NoteController:
    """The NoteController class is a controller for the Note model. It is responsible for creating, reading, updating, and deleting notes.
    It is also responsible for managing the notes in the application."""
    def __init__(self, notes: list[Note] = None):
        if notes is None:
            notes = []
        
        self._notes = notes
        
    @property
    def notes(self) -> list[Note]:
        """Get the notes in the application."""
        return self._notes
    
    @notes.setter
    def notes(self, value: list[Note]) -> None:
        """Set the notes in the application."""
        self._notes = value
    
    def get(self, note_id: int) -> Note:
        """Get a note by its id."""
        if not isinstance(note_id, int):
            raise TypeError("note_id must be an integer.")
        
        if note_id is None:
            raise ValueError("note_id must not be None.")

        for note in self._notes:
            if note.note_id == note_id:
                return note
        
        return None
    
    def create(self) -> Note:
        """Create a new note."""
        new_note = Note(note_id=len(self._notes) + 1)
        title = input("Enter the title of the note: ")
        