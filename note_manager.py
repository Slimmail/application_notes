import json
from note import Note
import datetime


class NoteManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.notes = self.load_notes()

    def load_notes(self):
        try:
            with open(self.file_name, "r") as file:
                notes_data = json.load(file)
                notes = [Note(**note_data) for note_data in notes_data]
                return notes
        except FileNotFoundError:
            return []

    def save_notes(self):
        notes_data = [note.to_dict() for note in self.notes]
        with open(self.file_name, "w") as file:
            json.dump(notes_data, file, indent=4)

    def create_note(self, title, body):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_note = Note(len(self.notes) + 1, title, body, timestamp)
        self.notes.append(new_note)
        self.save_notes()
        return new_note

    def read_notes(self, date_filter=None):
        if date_filter:
            filtered_notes = [
                note for note in self.notes if date_filter in note.timestamp]
        else:
            filtered_notes = self.notes

        for note in filtered_notes:
            print(f"ID: {note.id}")
            print(f"Заголовок: {note.title}")
            print(f"Тело: {note.body}")
            print(f"Дата/время создания: {note.timestamp}\n")

    def edit_note(self, note_id, new_title, new_body):
        for note in self.notes:
            if note.id == note_id:
                note.title = new_title
                note.body = new_body
                note.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                return
        print("Заметка с указанным ID не найдена.")

    def delete_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                self.notes.remove(note)
                self.save_notes()
                return
        print("Заметка с указанным ID не найдена.")

    def view_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                print(f"ID: {note.id}")
                print(f"Заголовок: {note.title}")
                print(f"Тело: {note.body}")
                print(f"Дата/время создания: {note.timestamp}")
                return
        print("Заметка с указанным ID не найдена.")

    def view_all_notes(self):
        for note in self.notes:
            print(f"ID: {note.id}")
            print(f"Заголовок: {note.title}")
            print(f"Тело: {note.body}")
            print(f"Дата/время создания: {note.timestamp}")
            print("-------------------------------")
