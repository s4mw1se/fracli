"""A module to represent a note."""

import json
from datetime import datetime
from typing import List, Optional
from dataclasses import dataclass, asdict


@dataclass
class Note:
    """A class to represent a note."""
    note_id: int
    parent_note: Optional['Note'] = None
    note_color: str = ""
    title: str = ""
    ticket_id: str = ""
    ticket_link: str = ""
    priority: int = 0
    body: str = ""
    parent_note_id: int = 0
    status: int = 1
    collaborators: List[str] = None
    tags: List[int] = None
    attachments: List[str] = None
    urls: List[str] = None
    child_notes: List[int] = None
    created_at: datetime = None
    edited_at: datetime = None
    reminder: datetime = None
    sprint_start: datetime = None
    sprint_end: datetime = None
    previous_version_backup: List['Note'] = None

    def __post_init__(self):
        if self.parent_note:
            self.notebook = self.parent_note.notebook
            self.parent_note_id = self.parent_note.note_id

        self.collaborators = [] if self.collaborators is None else self.collaborators
        self.tags = [] if self.tags is None else self.tags
        self.attachments = [] if self.attachments is None else self.attachments
        self.urls = [] if self.urls is None else self.urls
        self.child_notes = [] if self.child_notes is None else self.child_notes
        self.created_at = datetime.now() if self.created_at is None else self.created_at
        self.previous_version_backup = [
        ] if self.previous_version_backup is None else self.previous_version_backup

    def __set_note_id(self):
        try:
            value = int(input("Enter note id: "))
            self.note_id = value
        except ValueError as e:
            print(f"Invalid note id: {e}")

    def __set_note_color(self):
        value = input("Enter note color: ")
        self.note_color = value

    def __set_title(self):
        value = input("Enter title: ")
        self.title = value

    def __set_ticket_id(self):
        value = input("Enter ticket id: ")
        # Add custom validation for ticket id format
        # Example validation: Ticket id should start with "TKT-" followed by numbers
        if not value.startswith("TKT-") or not value[4:].isdigit():
            raise ValueError(
                "Invalid ticket id format. It should start with 'TKT-' followed by numbers.")
        self.ticket_id = value

    def __set_ticket_link(self):
        value = input("Enter ticket link: ")
        # Add custom validation for ticket link format
        # Example validation: Ticket link should start with "http://" or "https://"
        if not value.startswith(("http://", "https://")):
            raise ValueError(
                "Invalid ticket link format. It should start with 'http://' or 'https://'.")
        self.ticket_link = value

    def __set_priority(self):
        try:
            value = int(input("Enter priority (1-5): "))
            if 1 <= value <= 5:
                self.priority = value
            else:
                print("Priority must be between 1 and 5. Setting priority to 0.")
                self.priority = 0
        except ValueError as e:
            print(f"Invalid priority: {e}. Setting priority to 0.")
            self.priority = 0

    def __set_body(self):
        value = input("Enter body: ")
        self.body = value

    def __set_parent_note_id(self):
        try:
            value = int(input("Enter parent note id: "))
            self.parent_note_id = value
        except ValueError as e:
            print(f"Invalid parent note id: {e}")

    def __set_status(self):
        try:
            value = input(
                "Enter status (1 = active (default), 2 = on hold, 3 = completed, 0 = inactive): ")
            if value == "":
                self.status = 1
            else:
                value = int(value)
                if value in [0, 1, 2, 3]:
                    self.status = value
                else:
                    print("Invalid status. Setting status to 1 (active).")
                    self.status = 1
        except ValueError as e:
            print(f"Invalid status: {e}. Setting status to 1 (active).")
            self.status = 1

    def __set_collaborators(self):
        value = input("Enter collaborators (comma-separated): ")
        collaborators = [collaborator.strip() for collaborator in value.split(
            ",") if collaborator.strip()]
        self.collaborators = collaborators

    def __set_tags(self):
        value = input("Enter tags (comma-separated): ")
        tags = [int(tag.strip()) for tag in value.split(",") if tag.strip()]
        self.tags = tags

    def __set_attachments(self):
        value = input("Enter attachments (comma-separated): ")
        attachments = [attachment.strip()
                       for attachment in value.split(",") if attachment.strip()]
        self.attachments = attachments

    def __set_urls(self):
        value = input("Enter URLs (comma-separated): ")
        urls = [url.strip() for url in value.split(",") if url.strip()]
        self.urls = urls

    def __set_child_notes(self):
        value = input("Enter child note ids (comma-separated): ")
        child_notes = [int(note_id.strip())
                       for note_id in value.split(",") if note_id.strip()]
        self.child_notes = child_notes

    def update_note(self):
        print("Update Note:")
        print("Leave the field empty to keep the existing value.")

        self.__set_note_color()
        self.__set_title()
        self.__set_ticket_id()
        self.__set_ticket_link()
        self.__set_priority()
        self.__set_body()
        self.__set_parent_note_id()
        self.__set_status()
        self.__set_collaborators()
        self.__set_tags()
        self.__set_attachments()
        self.__set_urls()
        self.__set_child_notes()

        self.edited_at = datetime.now()

    def __eq__(self, other):
        if isinstance(other, Note):
            return self.note_id == other.note_id
        return False

    def __hash__(self):
        return hash(self.note_id)

    def __str__(self):
        return f"Note(note_id={self.note_id}, title='{self.title}', status={self.status}, created_at={self.created_at}, edited_at={self.edited_at})"

    @classmethod
    def from_json(cls, json_string):
        """Create a Note object from a JSON string."""
        data = json.loads(json_string)
        note = cls(**data)

        # Convert datetime strings to datetime objects
        if 'created_at' in data and data['created_at']:
            note.created_at = datetime.strptime(
                data['created_at'], "%Y-%m-%d %H:%M")
        if 'edited_at' in data and data['edited_at']:
            note.edited_at = datetime.strptime(
                data['edited_at'], "%Y-%m-%d %H:%M")
        if 'reminder' in data and data['reminder']:
            note.reminder = datetime.strptime(
                data['reminder'], "%Y-%m-%d %H:%M")
        if 'sprint_start' in data and data['sprint_start']:
            note.sprint_start = datetime.strptime(
                data['sprint_start'], "%Y-%m-%d %H:%M")
        if 'sprint_end' in data and data['sprint_end']:
            note.sprint_end = datetime.strptime(
                data['sprint_end'], "%Y-%m-%d %H:%M")

        # Recursively create Note objects for parent_note and previous_version_backup
        if 'parent_note' in data and data['parent_note']:
            note.parent_note = cls.from_json(json.dumps(data['parent_note']))
        if 'previous_version_backup' in data and data['previous_version_backup']:
            note.previous_version_backup = [cls.from_json(json.dumps(
                version)) for version in data['previous_version_backup']]

        return note

    def to_json(self):
        """Convert the note to a JSON string."""
        note_dict = asdict(self)
        note_dict["created_at"] = self.created_at.strftime(
            "%Y-%m-%d %H:%M") if self.created_at else None
        note_dict["edited_at"] = self.edited_at.strftime(
            "%Y-%m-%d %H:%M") if self.edited_at else None
        note_dict["reminder"] = self.reminder.strftime(
            "%Y-%m-%d %H:%M") if self.reminder else None
        note_dict["sprint_start"] = self.sprint_start.strftime(
            "%Y-%m-%d %H:%M") if self.sprint_start else None
        note_dict["sprint_end"] = self.sprint_end.strftime(
            "%Y-%m-%d %H:%M") if self.sprint_end else None

        # Recursively convert parent_note and previous_version_backup to JSON
        if self.parent_note:
            note_dict["parent_note"] = json.loads(self.parent_note.to_json())
        if self.previous_version_backup:
            note_dict["previous_version_backup"] = [json.loads(
                version.to_json()) for version in self.previous_version_backup]

        return json.dumps(note_dict, indent=4)
