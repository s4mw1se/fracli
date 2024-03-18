from datetime import datetime
from models.note import Note
import pytest


def test_init():
    note = Note(1)
    assert note.note_id == 1
    assert note._parent_note is None
    assert note._note_color == ""
    assert note._title == ""
    assert note._ticket_id == ""
    assert note._ticket_link == ""
    assert note._priority == 0
    assert note._body == ""
    assert note._parent_note_id == 0
    assert note._status == 1
    assert note._collaborators is None
    assert note._tags is None
    assert note._attachments is None
    assert note._urls is None
    assert note._child_notes is None
    assert note._created_at is None
    assert note._edited_at is None
    assert note._reminder is None
    assert note._sprint_start is None
    assert note._sprint_end is None
    assert note._previous_version_backups is None


def test_note_color_property():
    note = Note(1)
    note.note_color = "red"
    assert note.note_color == "red"
    assert isinstance(note.note_color, str)


def test_title_property():
    note = Note(1)
    note.title = "Test Note"
    assert note.title == "Test Note"
    assert isinstance(note.title, str)


def test_ticket_id_property():
    note = Note(1)
    note.ticket_id = "123"
    assert note.ticket_id == "123"
    assert isinstance(note.ticket_id, str)
    with pytest.raises(ValueError):
        note.ticket_id = 123


def test_ticket_link_property():
    note = Note(1)
    note.ticket_link = "https://example.com"
    assert note.ticket_link == "https://example.com"
    assert isinstance(note.ticket_link, str)
    with pytest.raises(ValueError):
        note.ticket_link = "example.com"


def test_priority_property():
    note = Note(1)
    note.priority = 3
    assert note.priority == 3
    assert isinstance(note.priority, int)
    note.priority = 6
    assert note.priority == 0


def test_body_property():
    note = Note(1)
    note.body = "Test body"
    assert note.body == "Test body"
    assert isinstance(note.body, str)


def test_parent_note_id_property():
    note = Note(1)
    note.parent_note_id = 2
    assert note.parent_note_id == 2
    assert isinstance(note.parent_note_id, int)


def test_status_property():
    note = Note(1)
    note.status = 2
    assert note.status == 2
    assert isinstance(note.status, int)
    note.status = 4
    assert note.status == 1


def test_collaborators_property():
    note = Note(1)
    note.collaborators = ["user1", "user2"]
    assert note.collaborators == ["user1", "user2"]
    assert isinstance(note.collaborators, list)
    assert all(isinstance(collaborator, str) for collaborator in note.collaborators)


def test_tags_property():
    note = Note(1)
    note.tags = [1, 2, 3]
    assert note.tags == [1, 2, 3]
    assert isinstance(note.tags, list)
    assert all(isinstance(tag, int) for tag in note.tags)


def test_attachments_property():
    note = Note(1)
    note.attachments = ["file1.txt", "file2.txt"]
    assert note.attachments == ["file1.txt", "file2.txt"]
    assert isinstance(note.attachments, list)
    assert all(isinstance(attachment, str) for attachment in note.attachments)


def test_urls_property():
    note = Note(1)
    note.urls = ["https://example.com"]
    assert note.urls == ["https://example.com"]
    assert isinstance(note.urls, list)
    assert all(isinstance(url, str) for url in note.urls)


def test_child_notes_property():
    note = Note(1)
    note.child_notes = [2, 3]
    assert note.child_notes == [2, 3]
    assert isinstance(note.child_notes, list)
    assert all(isinstance(child_note, int) for child_note in note.child_notes)


def test_created_at_property():
    note = Note(1)
    now = datetime.now()
    note.created_at = now
    assert note.created_at == now
    assert isinstance(note.created_at, datetime)


def test_edited_at_property():
    note = Note(1)
    now = datetime.now()
    note.edited_at = now
    assert note.edited_at == now
    assert isinstance(note.edited_at, datetime)


def test_reminder_property():
    note = Note(1)
    now = datetime.now()
    note.reminder = now
    assert note.reminder == now
    assert isinstance(note.reminder, datetime)


def test_sprint_start_property():
    note = Note(1)
    now = datetime.now()
    note.sprint_start = now
    assert note.sprint_start == now
    assert isinstance(note.sprint_start, datetime)


def test_sprint_end_property():
    note = Note(1)
    now = datetime.now()
    note.sprint_end = now
    assert note.sprint_end == now
    assert isinstance(note.sprint_end, datetime)


def test_previous_version_backups_property():
    note = Note(1)
    backup_note = Note(2)
    note.previous_version_backups = [backup_note]
    assert note.previous_version_backups == [backup_note]
    assert isinstance(note.previous_version_backups, list)
    assert all(isinstance(backup, Note) for backup in note.previous_version_backups)