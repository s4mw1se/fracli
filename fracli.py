
from controller import Controller
from note import Note
from datetime import datetime
from rich import print
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

console = Console()

def main():
    controller = Controller(console)
    
    while True:
        command = Prompt.ask("Enter command (c: create, v: view, d: delete, e: edit, x: exit)", console=console)

        if command == "c":
            controller.create_note()
            controller.save_notes()
        elif command == "v":
            controller.view_notes()
        elif command == "d":
            controller.delete_note()
            controller.save_notes()
        elif command == "e":
            controller.edit_note()
            controller.save_notes()
        elif command == "x":
            return
        else:
            console.print("Invalid command", style="bold red")

if __name__ == "__main__":
    main()