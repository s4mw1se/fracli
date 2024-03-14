import json
from note import Note
from rich.prompt import Prompt
from datetime import datetime
from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt


class Controller:
    def __init__(self, console):
        self.console = console
        self.notes: list[Note] = []
    
    def load_notes(self):
        try:
            with open("notes.json", "r") as file:
                data = json.load(file)
                self.notes = [Note(**note) for note in data]
                print("Notes loaded successfully", style="bold green")
                
        except FileNotFoundError:
            self.console.print("No notes found, starting new file", style="bold orange")
            self.notes = []
        except json.JSONDecodeError:
            self.console.print("Error loading notes", style="bold red")
    

    def save_notes(self):
        data = [vars(note) for note in self.notes]
        try:
            with open("notes.json", "w") as file:
                json.dump(data, file)
        except IOError:
            self.console.print("Error saving notes", style="bold red")
    
    def set_note_title(self, title:str, note:Note=None) -> str:
        if note is None:
            title = Prompt.ask("Enter note title", console=self.console, style="bold blue")
            return title
        else:
            self.console.print(f"Current title: {note.title}", style="bold blue")
            new_title = Prompt.ask("Enter new title (or leave blank to keep the current title)", console=self.console)
            if new_title:
                note.title = new_title
                note.edited_at = datetime.now()

    def create_note(self):
        now = datetime.now()

        title = Prompt.ask("Enter note title", console=self.console, style="bold blue")
        body = Prompt.ask("Enter note body", console=self.console, style="bold purple")
        priority = Prompt.ask("Enter priority (high, medium, low, blank for none)", console=self.console, style="bold yellow")
        reminder_input = Prompt.ask("Create reminder? (enter: yes or leave blank for no)", console=self.console, style="bold yellow")
        reminder = None
        if reminder_input:
            reminder_input = Prompt.ask("How many days from now?", console=self.console, style="bold yellow")
            try:
                days = int(reminder_input)
                if days < 1:
                    self.console.print("Invalid input, creating reminder for today", style="bold red")
                    reminder = now.date()
                reminder = now + datetime.timedelta(days=days)
            except ValueError:
                self.console.print("Invalid input, reminder not created", style="bold red")
                

        attachments_input = Prompt.ask("Enter attachments (comma-separated file paths or URLs, leave blank for none)", console=self.console)
        attachments = attachments_input.split(",") if attachments_input else []
        notebook = Prompt.ask("Enter notebook", console=self.console)
        collaborators_input = Prompt.ask("Enter collaborators (comma-separated names or emails, leave blank for none)", console=self.console)
        collaborators = collaborators_input.split(",") if collaborators_input else []
        tags_input = Prompt.ask("Enter tags (comma-separated, leave blank for none)", console=self.console)
        tags = tags_input.split(",") if tags_input else []

        note = Note(title, body, now, now, priority, reminder, attachments, notebook, collaborators, tags)
        self.notes.append(note)
        self.console.print("Note created successfully", style="bold green")

    def view_notes(self, notes):
        if not notes:
            self.console.print("No notes found", style="bold red")
            return

        table = Table(title="Notes")
        table.add_column("Index", style="cyan")
        table.add_column("Title", style="magenta")

        for i, note in enumerate(notes, start=1):
            table.add_row(str(i), note.title)

        self.console.print(table)

        while True:
            input_str = Prompt.ask("Enter note number to view details (or 'b' to go back)", console=self.console)
            if input_str == "b":
                return
            try:
                index = int(input_str) - 1
                if 0 <= index < len(notes):
                    note = notes[index]
                    self.console.print(f"Title: {note.title}", style="bold blue")
                    self.console.print(f"Body: {note.body}", style="bold purple")
                    self.console.print(f"Priority: {note.priority}", style="bold yellow")
                    self.console.print(f"Reminder: {note.reminder.isoformat() if note.reminder else ''}", style="bold yellow")
                    self.console.print(f"Attachments: {note.attachments}", style="bold yellow")
                    self.console.print(f"Notebook: {note.notebook}", style="bold yellow")
                    self.console.print(f"Collaborators: {note.collaborators}", style="bold yellow")
                    self.console.print(f"Tags: {note.tags}", style="bold yellow")
                    self.console.print(f"Created: {note.created_at.isoformat()}", style="bold green")
                    self.console.print(f"Edited: {note.edited_at.isoformat()}", style="bold yellow")
                    break
                else:
                    self.console.print("Invalid note number", style="bold red")
            except ValueError:
                self.console.print("Invalid input", style="bold red")

    def delete_note(self, notes):
        if not notes:
            self.console.print("No notes found", style="bold red")
            return

        while True:
            input_str = Prompt.ask("Enter note number to delete (or 'b' to go back)", console=self.console)
            if input_str == "b":
                return
            try:
                index = int(input_str) - 1
                if 0 <= index < len(notes):
                    del notes[index]
                    self.console.print("Note deleted successfully", style="bold green")
                    return
                else:
                    self.console.print("Invalid note number", style="bold red")
            except ValueError:
                self.console.print("Invalid input", style="bold red")

    def edit_note(self, notes):
        if not notes:
            self.console.print("No notes found", style="bold red")
            return

        while True:
            input_str = Prompt.ask("Enter note number to edit (or 'b' to go back)", console=self.console)
            if input_str == "b":
                return
            try:
                index = int(input_str) - 1
                if 0 <= index < len(notes):
                    note = notes[index]
                    now = datetime.now()

                    self.console.print(f"Current title: {note.title}", style="bold blue")
                    new_title = Prompt.ask("Enter new title (or leave blank to keep the current title)", console=self.console)
                    if new_title:
                        note.title = new_title
                        note.edited_at = now

                    self.console.print(f"Current body: {note.body}", style="bold purple")
                    new_body = Prompt.ask("Enter new body (or leave blank to keep the current body)", console=self.console)
                    if new_body:
                        note.body = new_body
                        note.edited_at = now

                    self.console.print(f"Current priority: {note.priority}", style="bold yellow")
                    new_priority = Prompt.ask("Enter new priority (high, medium, low) (or leave blank to keep the current priority)", console=self.console)
                    if new_priority:
                        note.priority = new_priority
                        note.edited_at = now

                    self.console.print(f"Current reminder: {note.reminder.isoformat() if note.reminder else ''}", style="bold yellow")
                    new_reminder_input = Prompt.ask("Enter new reminder (leave blank for no reminder)", console=self.console)
                    if new_reminder_input:
                        try:
                            new_reminder = datetime.fromisoformat(new_reminder_input)
                            note.reminder = new_reminder
                            note.edited_at = now
                        except ValueError:
                            self.console.print("Invalid reminder format, using current time", style="bold red")
                            note.reminder = now
                            note.edited_at = now

                    self.console.print(f"Current attachments: {note.attachments}", style="bold yellow")
                    new_attachments_input = Prompt.ask("Enter new attachments (comma-separated file paths or URLs, leave blank for no change)", console=self.console)
                    if new_attachments_input:
                        note.attachments = new_attachments_input.split(",")
                        note.edited_at = now

                    self.console.print(f"Current notebook: {note.notebook}", style="bold yellow")
                    new_notebook = Prompt.ask("Enter new notebook (or leave blank to keep the current notebook)", console=self.console)
                    if new_notebook:
                        note.notebook = new_notebook
                        note.edited_at = now

                    self.console.print(f"Current collaborators: {note.collaborators}", style="bold yellow")
                    new_collaborators_input = Prompt.ask("Enter new collaborators (comma-separated names or emails, leave blank for no change)", console=self.console)
                    if new_collaborators_input:
                        note.collaborators = new_collaborators_input.split(",")
                        note.edited_at = now

                    self.console.print(f"Current tags: {note.tags}", style="bold yellow")
                    new_tags_input = Prompt.ask("Enter new tags (comma-separated, leave blank for no change)", console=self.console)
                    if new_tags_input:
                        note.tags = new_tags_input.split(",")
                        note.edited_at = now

                    self.console.print("Note edited successfully", style="bold green")
                    return
                else:
                    self.console.print("Invalid note number", style="bold red")
            except ValueError:
                self.console.print("Invalid input", style="bold red")