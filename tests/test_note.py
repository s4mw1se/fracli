""" Test the Note class. """

from datetime import datetime, timedelta
import pytest
from src.models.note import Note

def test_note_creation():
    """Test the creation of a Note object."""
    note = Note(1)
    assert note.note_id == 1
    assert note.status == 1
    assert note.created_at is None


def test_note_color():
    """Test setting and getting the note color."""
    note = Note(1)
    note.note_color = "red"
    assert note.note_color == "red"


def test_title():
    """Test setting and getting the note title."""
    note = Note(1)
    note.title = "Test Note"
    assert note.title == "Test Note"


def test_ticket_id():
    """Test setting and getting the ticket ID."""
    note = Note(1)
    note.ticket_id = "ABC-123"
    assert note.ticket_id == "ABC-123"

    with pytest.raises(ValueError):
        note.ticket_id = 123


def test_ticket_link():
    """Test setting and getting the ticket link."""
    note = Note(1)
    note.ticket_link = "https://example.com"
    assert note.ticket_link == "https://example.com"

    with pytest.raises(ValueError):
        note.ticket_link = "invalid_link"


def test_priority():
    """Test setting and getting the note priority."""
    note = Note(1)
    note.priority = 3
    assert note.priority == 3

    note.priority = 6
    assert note.priority == 0


def test_body():
    """Test setting and getting the note body."""
    note = Note(1)
    note.body = "This is a test note."
    assert note.body == "This is a test note."

    with pytest.raises(ValueError):
        note.body = 123


def test_parent_note_id():
    """Test setting and getting the parent note ID."""
    note = Note(1)
    note.parent_note_id = 0
    assert note.parent_note_id == 0

    with pytest.raises(ValueError):
        note.parent_note_id = -1

    with pytest.raises(ValueError):
        note.parent_note_id = 1

    with pytest.raises(ValueError):
        note.parent_note_id = 2


def test_status():
    """Test setting and getting the note status."""
    note = Note(1)
    note.status = 2
    assert note.status == 2

    with pytest.raises(ValueError):
        note.status = -1

    with pytest.raises(ValueError):
        note.status = 4

    with pytest.raises(ValueError):
        note.status = "invalid"


def test_collaborators():
    """Test setting and getting the note collaborators."""
    note = Note(1)
    note.collaborators = ["user1", "user2"]
    assert note.collaborators == ["user1", "user2"]

    with pytest.raises(ValueError):
        note.collaborators = ["user1", 123]


def test_tags():
    """Test setting and getting the note tags."""
    note = Note(1)
    note.tags = ["tag1", "tag2"]
    assert note.tags == ["tag1", "tag2"]

    with pytest.raises(ValueError):
        note.tags = ["tag1", 123]


def test_attachments():
    """Test setting and getting the note attachments."""
    note = Note(1)
    note.attachments = ["file1.txt", "file2.txt"]
    assert note.attachments == ["file1.txt", "file2.txt"]

    with pytest.raises(ValueError):
        note.attachments = ["file1.txt", 123]


def test_urls():
    """Test setting and getting the note URLs."""
    note = Note(1)
    note.urls = ["https://example.com", "https://example.org"]
    assert note.urls == ["https://example.com", "https://example.org"]

    with pytest.raises(ValueError):
        note.urls = ["https://example.com", 123]


def test_child_notes():
    """Test setting and getting the child notes."""
    note = Note(2)
    note.child_notes = [0, 1]
    assert note.child_notes == [0, 1]

    with pytest.raises(ValueError):
        note.child_notes = [0, 3]

    with pytest.raises(ValueError):
        note.child_notes = [0, "invalid"]


def test_created_at():
    """Test setting and getting the created_at timestamp."""
    note = Note(1)
    now = datetime.now()
    note.created_at = now
    assert note.created_at == now

    with pytest.raises(ValueError):
        note.created_at = "invalid"

    with pytest.raises(ValueError):
        note.created_at = now + timedelta(days=1)

def test_edited_at():
    """Test setting and getting the edited_at timestamp."""
    note = Note(1)
    now = datetime.now()
    note.created_at = now
    note.edited_at = now + timedelta(minutes=10)
    assert note.edited_at == now + timedelta(minutes=10)

    with pytest.raises(ValueError):
        note.edited_at = "invalid"
    
    with pytest.raises(ValueError):
        note.edited_at = now - timedelta(minutes=10)


def test_reminder():
    """Test setting and getting the reminder timestamp."""
    note = Note(1)
    now = datetime.now()
    note.reminder = now + timedelta(hours=1)
    assert note.reminder == now + timedelta(hours=1)

    with pytest.raises(ValueError):
        note.reminder = "invalid"

    with pytest.raises(ValueError):
        note.reminder = now - timedelta(hours=1)


def test_sprint_dates():
    """Test setting and getting the sprint start and end dates."""
    note = Note(1)
    now = datetime.now()
    note.sprint_start = now
    note.sprint_end = now + timedelta(days=7)
    assert note.sprint_start == now
    assert note.sprint_end == now + timedelta(days=7)

    with pytest.raises(ValueError):
        note.sprint_start = "invalid"

    with pytest.raises(ValueError):
        note.sprint_end = "invalid"

    with pytest.raises(ValueError):
        note.sprint_end = now - timedelta(days=1)

    with pytest.raises(ValueError):
        note.sprint_start = now + timedelta(days=8)


def test_previous_version_backups():
    """Test setting and getting the previous version backups."""
    note1 = Note(1)
    note2 = Note(2)
    note3 = Note(3)
    note3.previous_version_backups = [note1, note2]
    assert note3.previous_version_backups == [note1, note2]

    with pytest.raises(ValueError):
        note3.previous_version_backups = [note1, "invalid"]
