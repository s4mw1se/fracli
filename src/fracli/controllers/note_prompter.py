
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, Static, Button
from textual.containers import Container
from datetime import datetime

from models.note import Note


class NotePrompter(App):
    """A class to prompt the user for note details and build a Note object."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.note = None
        self.current_property = None
        self.property_queue = [
            "note_id", "title", "note_color", "ticket_id", "ticket_link",
            "priority", "body", "parent_note_id", "status", "collaborators",
            "tags", "attachments", "urls", "child_notes", "reminder",
            "sprint_start", "sprint_end"
        ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Container(
            Input(placeholder="Enter the value"),
            Button("Submit", id="submit", variant="primary"),
            Static(id="error"),
            id="input_container"
        )
        yield Footer()

    def on_mount(self) -> None:
        """Called when the app is mounted."""
        self.new_note()

    def new_note(self) -> None:
        """Create a new note and start prompting for properties."""
        self.note = Note(datetime.now().timestamp())
        self.prompt_next_property()

    def prompt_next_property(self) -> None:
        """Prompt the user for the next property in the queue."""
        if self.property_queue:
            self.current_property = self.property_queue.pop(0)
            self.query_one(Input).placeholder = f"Enter {self.current_property} (leave blank to skip)"
        else:
            self.print_note()
            self.exit()

    def on_input_changed(self, event: Input.Changed) -> None:
        """Called when the input value changes."""
        self.query_one("#error", Static).update("")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Called when the submit button is pressed."""
        if event.button.id == "submit":
            value = self.query_one(Input).value
            if self.current_property in ["note_id", "title"] and not value:
                self.query_one("#error", Static).update(f"{self.current_property} is required!")
                return

            try:
                if value:
                    setattr(self.note, self.current_property, value)
            except ValueError as e:
                self.query_one("#error", Static).update(str(e))
                return

            self.query_one(Input).value = ""
            self.prompt_next_property()

    def print_note(self) -> None:
        """Print the final note object."""
        note_color = self.note.note_color or "default"
        self.query_one("#input_container").remove()
        self.query_one(Container).add(
            Static(self.note, id="note", classes=f"note-{note_color}")
        )

if __name__ == "__main__":
    app = NotePrompter()
    app.run()