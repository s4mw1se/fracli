import json
from note import Note
from typing import List


class NoteController:
    """
    A class to represent a controller for working with notes.
    """
    def __init__(self, file_path: str = "notes.json"):
        self.file_path = file_path
        self.notes: List[Note] = []
        self.load_notes()

    def create_note(self, note: Note):
        """
        Create a new note.
        """
        self.notes.append(note)
        self.save_notes()
        print(f"Note created with id: {note.note_id}")

    def read_note(self, note_id: int) -> Note:
        """
        Read a note by its id.
        """
        for note in self.notes:
            if note.note_id == note_id:
                return note
        raise ValueError(f"Note with id {note_id} not found.")

    def update_note(self, note_id: int, updated_note: Note):
        """
        Update a note by its id.
        """
        for i, note in enumerate(self.notes):
            if note.note_id == note_id:
                self.notes[i] = updated_note
                self.save_notes()
                print(f"Note with id {note_id} updated.")
                return
        raise ValueError(f"Note with id {note_id} not found.")

    def delete_note(self, note_id: int):
        for i, note in enumerate(self.notes):
            if note.note_id == note_id:
                del self.notes[i]
                self.save_notes()
                print(f"Note with id {note_id} deleted.")
                return
        raise ValueError(f"Note with id {note_id} not found.")

    def load_notes(self):
        """
        Load notes from a file.
        """
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                self.notes = [Note.from_json(json.dumps(note_data))
                              for note_data in data]
        except FileNotFoundError:
            self.notes = []

    def save_notes(self):
        """
        Save notes to a file.
        """
        data = [json.loads(note.to_json()) for note in self.notes]
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def get_all_notes(self) -> List[Note]:
        """
        Get all notes.
        """
        return self.notes
