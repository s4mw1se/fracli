"""A module to represent a note."""

from datetime import datetime

class Note:
    """A class to represent a note."""

    def __init__(self, note_id: int):
        self.note_id = note_id

        self._parent_note: int = None
        self._note_color: str = ""
        self._title: str = ""
        self._ticket_id: str = ""
        self._ticket_link: str = ""
        self._priority: int = 0
        self._body: str = ""
        self._parent_note_id: int = 0
        self._status: int = 1
        self._collaborators: list[str] = []
        self._tags: list[str] = []
        self._attachments: list[str] = []
        self._urls: list[str] = []
        self._child_notes: list[int] = []
        self._created_at: datetime = None
        self._edited_at: datetime = None
        self._reminder: datetime = None
        self._sprint_start: datetime = None
        self._sprint_end: datetime = None
        self._previous_version_backups: list['Note'] = None

    @property
    def note_color(self) -> str:
        """Get the note color."""
        return self._note_color

    @note_color.setter
    def note_color(self, value: str) -> None:
        """Set the note color."""
        self._note_color = value

    @property
    def title(self) -> str:
        """Get the title of the note."""
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        """Set the title of the note."""
        self._title = value

    @property
    def ticket_id(self) -> str:
        """Get the ticket id."""
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, value: str) -> None:
        """Set the ticket id.  """
        if not isinstance(value, str):
            raise ValueError(
                "Invalid ticket id format. It should start with followed by numbers.")
        self._ticket_id = value

    @property
    def ticket_link(self) -> str:
        """Get the ticket link."""
        return self._ticket_link

    @ticket_link.setter
    def ticket_link(self, value: str) -> None:
        """Set the ticket link."""
        if not value.startswith(("http://", "https://")):
            raise ValueError(
                "Invalid ticket link format. It should start with 'http://' or 'https://'.")
        self._ticket_link = value

    @property
    def priority(self) -> int:
        """Get the priority of the note."""
        return self._priority

    @priority.setter
    def priority(self, value: int):
        """Set the priority of the note."""
        if 1 <= value <= 5:
            self._priority = value
        else:
            print("Priority must be between 1 and 5. Setting priority to 0.")
            self._priority = 0

    @property
    def body(self) -> str:
        """Get the body of the note."""
        return self._body

    @body.setter
    def body(self, value: str) -> None:
        """Set the body of the note."""
        if not isinstance(value, str):
            raise ValueError("Invalid body format. It should be a string.")
        self._body = value

    @property
    def parent_note_id(self) -> int:
        """Get the parent note id."""
        return self._parent_note_id

    @parent_note_id.setter
    def parent_note_id(self, value: int) -> None:
        """Set the parent note id."""
        if not isinstance(value, int):
            raise ValueError(
                "Invalid parent note id format. It should be an integer.")
        if value < 0:
            raise ValueError(
                "Invalid parent note id. It should be a positive integer.")
        if value == self.note_id:
            raise ValueError(
                "Invalid parent note id. It should not be the same as the note id.")
        if value > self.note_id:
            raise ValueError(
                "Invalid parent note id. It should be less than the current note id.")
        self._parent_note_id = value

    @property
    def status(self) -> int:
        """Get the status of the note. 0: deleted, 1: active, 2: archived, 3: completed."""
        return self._status

    @status.setter
    def status(self, value: int) -> None:
        """Set the status of the note. 0: deleted, 1: active, 2: archived, 3: completed."""
        if not isinstance(value, int):
            raise ValueError(
                "Invalid status id format. It should be an integer.")
        if value < 0:
            raise ValueError(
                "Invalid status id. It should be a positive integer.")
        if value > 3:
            raise ValueError("Invalid status id. It should be less than 3.")

        self._status = value

    @property
    def collaborators(self) -> list[str]:
        """Get the collaborators of the note."""
        return self._collaborators

    @collaborators.setter
    def collaborators(self, value: list[str]) -> None:
        """Set the collaborators of the note."""
        if not all(isinstance(collaborator, str) for collaborator in value):
            raise ValueError(
                "Invalid collaborators format. It should be a list of strings.")

        self._collaborators = value

    @property
    def tags(self: list[str]) -> list[str]:
        """Get the tags of the note."""
        return self._tags

    @tags.setter
    def tags(self, value: list[str]) -> None:
        """Set the tags of the note."""
        if not all(isinstance(tag, str) for tag in value):
            raise ValueError(
                "Invalid tags format. It should be a list of strings.")

        self._tags = value

    @property
    def attachments(self) -> list[str]:
        """Get the attachments of the note."""
        return self._attachments

    @attachments.setter
    def attachments(self, value: list[str]) -> None:
        """Set the attachments of the note."""
        if not all(isinstance(attachment, str) for attachment in value):
            raise ValueError(
                "Invalid attachments format. It should be a list of strings.")
        self._attachments = value

    @property
    def urls(self) -> list[str]:
        """Get the urls of the note."""
        return self._urls

    @urls.setter
    def urls(self, value: str) -> None:
        """ Set the urls of the note."""
        if not all(isinstance(url, str) for url in value):
            raise ValueError(
                "Invalid urls format. It should be a list of strings.")
        self._urls = value

    @property
    def child_notes(self) -> list[int]:
        """Get the child notes of the note."""
        return self._child_notes

    @child_notes.setter
    def child_notes(self, value: list[int]) -> None:
        """Set the child notes of the note."""
        if not all(isinstance(child_note, int) for child_note in value):
            raise ValueError(
                "Invalid child notes format. It should be a list of integers.")

        if not all(child_note < self.note_id for child_note in value):
            raise ValueError(
                "Invalid child notes. They should be less than the current note id.")
        self._child_notes = value

    @property
    def created_at(self) -> datetime:
        """Get the created date of the note."""
        return self._created_at

    @created_at.setter
    def created_at(self, value: datetime) -> None:
        """Set the created date of the note."""
        if value:
            if not isinstance(value, datetime):
                raise ValueError(
                    "Invalid created date format. It should be a datetime object.")
        if isinstance(value, datetime):
            if value > datetime.now():
                raise ValueError(
                    "Invalid created date. It should be less than the current date.")

        self._created_at = value

    @property
    def edited_at(self) -> datetime:
        """Get the edited date of the note."""
        if not self._edited_at:
            return self.created_at

        return self._edited_at

    @edited_at.setter
    def edited_at(self, value: datetime) -> None:
        """Set the edited date of the note."""
        if not isinstance(value, datetime):
            raise ValueError(
                "Invalid edited date format. It should be a datetime object.")

        if self.created_at and value < self.created_at:
            raise ValueError(
                "Invalid edited date. It should be greater than or equal to the created date.")

        self._edited_at = value
        
    @property
    def reminder(self) -> datetime:
        """Get the reminder date of the note."""
        return self._reminder

    @reminder.setter
    def reminder(self, value: datetime) -> None:
        """Set the reminder date of the note."""
        
        if value:
            if not isinstance(value, datetime):
                raise ValueError(
                    "Invalid reminder date format. It should be a datetime object.")
            
            if isinstance(value, datetime):
                if value < datetime.now():
                    raise ValueError(
                        "Invalid reminder date. It should be greater than the current date.")

                if self.created_at and value < self.created_at:
                    raise ValueError(
                        "Invalid reminder date. It should be greater than or equal to the created date.")

        self._reminder = value

    @property
    def sprint_start(self) -> datetime:
        """Get the sprint start date of the note."""
        return self._sprint_start

    @sprint_start.setter
    def sprint_start(self, value: datetime) -> None:
        """Set the sprint start date of the note."""
        if not isinstance(value, datetime):
            raise ValueError(
                "Invalid sprint start date format. It should be a datetime object.")

        if self._sprint_end and value > self._sprint_end:
            raise ValueError(
                "Invalid sprint start date. It should be less than or equal to the sprint end date.")

        self._sprint_start = value

    @property
    def sprint_end(self) -> datetime:
        """Get the sprint end date of the note."""
        return self._sprint_end

    @sprint_end.setter
    def sprint_end(self, value: datetime) -> None:
        """Set the sprint end date of the note."""
        if not isinstance(value, datetime):
            raise ValueError(
                "Invalid sprint end date format. It should be a datetime object.")

        if self._sprint_start and value < self._sprint_start:
            raise ValueError(
                "Invalid sprint end date. It should be greater than or equal to the sprint start date."
            )

        if value < datetime.now():
            raise ValueError(
                "Invalid sprint end date. It should be greater than the current date.")

        if self.created_at and value < self.created_at:
            raise ValueError(
                "Invalid sprint end date. It should be greater than or equal to the created date.")

        self._sprint_end = value
        
    @property
    def previous_version_backups(self) -> list['Note']:
        """Get the previous version backup of the note."""
        return self._previous_version_backups

    @previous_version_backups.setter
    def previous_version_backups(self, value: list['Note']) -> None:
        """Set the previous version backup of the note."""
        if not all(isinstance(note, Note) for note in value):
            raise ValueError(
                "Invalid previous version backups format. It should be a list of Note objects.")

        self._previous_version_backups = value
