# fracli

A command line application for note taking that uses hotkeys to quickly create, edit, and delete notes.

I made this because I wanted a quick way to take notes without a bloated web app or GUI application. All the notes are stored in a single file in JSON format this way they can easily be parsed, extended, and version controlled.

## Use Case

I wrote this because my work in security requires me to keep track of a lot of things. Projects, meetings, vulnerabilties, incidents, news, people, training, development, family, appointments, goals,  My brain does great with a lot of things, its a constant stream of ideas, thoughts, connections, and responsiblites that cant be neglected.

What does not do good with handling a high speed steam of conciousness, is pretty much every main stream note taking application. They all fail somewhat miserably because they create half-baked features for shareholders. Not my half-backed ideas.

Why the hell are their no todo apps that allow me to put a date range for the crap I need to do. I don't know when I am going to clean the gutters, sometime in the next period of whenever I have time.

Why can I draw a picture of a cat, make some awful diagram, or create a list of things to do, but there is no feature for formatting code snippets. Looking at you OneNote.

Why can I make a endless amount of databases, but have to script out a query to make a recuring task? Why is that Notion?

Why do I need a degree in UI/UX to set up a stupid notebook? I just want to take notes, not make a website or project management platform.

Why do I have to pay for a service to keep my notes private? Oh yeah, because they are selling my data to advertisers.

Postit notes go on frame of my monitor for 5 years to remind me of that one thing I needed to do a long time ago and no longer server any relevance. Not cluttering up my desktop.

Why is the most colorful feature we have literally an option for dark mode? We celebrate dark mode releases because finally can see our burnt out souls in higher contrast.

Why cant I intergrate my notes into my workflow? Why do I have to stop what I am doing to take a note? Oh yeah to see the ads.

## Fracli Vision

The fractal cli is designed to keep track of the complex dimensions of our life in a streamlined manor using dictionaries to take advantage of the HashTable data structure. All notes are incremented with an ID used as a key in the dictionary. This allows for quick access to notes, and the ability to sort, filter, and search notes. The notes are stored in a single file in JSON format, so they can be easily parsed, extended, and version controlled.

Any note that are created can have child notes stored at the same level as the parent note but with a reference to the parent note instead of nested dictionaries.

Each note has unique color, and their chidlren a shade of that color. When a note is added the shade is incremented by a value of 1. If the note has a parent, it will inherit the color of the parent note and the shade will be incremented by 1. This allows for quick visual identification of the notes and their relationships.

## Features

* CRUD operations on notes, with hotkeys for quick access.
* Set reminders for notes.
* Set deadlines for notes, and have them appear in a todo list.
* set a date range for notes, and have them appear in a todo list.
* track actions on a tree of notes.
* see you progress
* display notes with a date range
  * see how much effort you have spent on a note or a tree of notes
  * 


## Usage

You run it, and keep it running in a shell window while you work. You can then use hotkeys to create, edit, and delete notes.

c - create a new note
e - edit a note
d - delete a note
x - exit the application


```bash
pip -m venv ./.venv
pip install -e .
```
