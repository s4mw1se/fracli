"""A module to represent a note."""

from datetime import datetime
from dataclasses import dataclass


@dataclass
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
        self._collaborators: list[str] = None
        self._tags: list[int] = None
        self._attachments: list[str] = None
        self._urls: list[str] = None
        self._child_notes: list[int] = None
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
        self._body = value

    @property
    def parent_note_id(self) -> int:
        """Get the parent note id."""
        return self._parent_note_id

    @parent_note_id.setter
    def parent_note_id(self, value: int) -> None:
        """Set the parent note id."""
        self._parent_note_id = value

    @property
    def status(self) -> int:
        """Get the status of the note. 0: deleted, 1: active, 2: archived, 3: completed."""
        return self._status

    @status.setter
    def status(self, value: int) -> None:
        """Set the status of the note. 0: deleted, 1: active, 2: archived, 3: completed."""
        if value in [0, 1, 2, 3]:
            self._status = value
        else:
            print("Invalid status. Setting status to 1 (active).")
            self._status = 1

    @property
    def collaborators(self) -> list[str]:
        """Get the collaborators of the note."""
        return self._collaborators

    @collaborators.setter
    def collaborators(self, value: list[str]) -> None:
        """Set the collaborators of the note."""
        self._collaborators = value

    @property
    def tags(self: list[str]) -> list[str]:
        """Get the tags of the note."""
        return self._tags

    @tags.setter
    def tags(self, value) -> None:
        """Set the tags of the note."""
        self._tags = value

    @property
    def attachments(self) -> list[str]:
        """Get the attachments of the note."""
        return self._attachments

    @attachments.setter
    def attachments(self, value: list[str]) -> None:
        """Set the attachments of the note."""
        self._attachments = value

    @property
    def urls(self) -> list[str]:
        """Get the urls of the note."""
        return self._urls

    @urls.setter
    def urls(self, value: str) -> None:
        """ Set the urls of the note."""
        self._urls = value

    @property
    def child_notes(self) -> list[int]:
        """Get the child notes of the note."""
        return self._child_notes

    @child_notes.setter
    def child_notes(self, value: list[int]) -> None:
        """Set the child notes of the note."""
        self._child_notes = value

    @property
    def created_at(self) -> datetime:
        """Get the created date of the note."""
        return self._created_at

    @created_at.setter
    def created_at(self, value: datetime) -> None:
        """Set the created date of the note."""
        self._created_at = value

    @property
    def edited_at(self) -> datetime:
        """Get the edited date of the note."""
        return self._edited_at

    @edited_at.setter
    def edited_at(self, value: datetime) -> None:
        """Set the edited date of the note."""
        self._edited_at = value

    @property
    def reminder(self) -> datetime:
        """Get the reminder date of the note."""
        return self._reminder

    @reminder.setter
    def reminder(self, value: datetime) -> None:
        """Set the reminder date of the note."""
        self._reminder = value

    @property
    def sprint_start(self) -> datetime:
        """Get the sprint start date of the note."""
        return self._sprint_start

    @sprint_start.setter
    def sprint_start(self, value: datetime) -> None:
        """Set the sprint start date of the note."""
        self._sprint_start = value

    @property
    def sprint_end(self) -> datetime:
        """Get the sprint end date of the note."""
        return self._sprint_end

    @sprint_end.setter
    def sprint_end(self, value: datetime) -> None:
        """Set the sprint end date of the note."""
        self._sprint_end = value

    @property
    def previous_version_backups(self) -> list['Note']:
        """Get the previous version backup of the note."""
        return self._previous_version_backups

    @previous_version_backups.setter
    def previous_version_backups(self, value: list['Note']) -> None:
        """Set the previous version backup of the note."""
        self._previous_version_backups = value
