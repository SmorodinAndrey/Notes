import json
import os
from datetime import datetime


class NoteManager:
    def __init__(self):
        pass

    def save_notes(self, notes):
        with open("notes.json", "w") as file:
            json.dump(notes, file)

    def load_notes(self):
        if not os.path.exists("notes.json"):
            return []

        with open("notes.json", "r") as file:
            return json.load(file)

    def list_notes(self, filter_date=None):
        notes = self.load_notes()

        if filter_date:
            filtered_notes = [
                note for note in notes if note["date"] == filter_date]
            return filtered_notes
        else:
            return notes

    def add_note(self, title, message):
        notes = self.load_notes()
        note = {"id": len(notes) + 1, "title": title, "message": message,
                "date": datetime.now().strftime("%d-%m-%Y")}
        notes.append(note)
        self.save_notes(notes)

    def edit_note(self, note_id, new_title, new_message):
        notes = self.load_notes()
        for note in notes:
            if note["id"] == note_id:
                note["title"] = new_title
                note["message"] = new_message
                note["date"] = datetime.now().strftime("%d-%m-%Y")
        self.save_notes(notes)

    def delete_note(self, note_id):
        notes = self.load_notes()
        notes = [note for note in notes if note["id"] != note_id]
        self.save_notes(notes)

    def run(self):
        while True:
            command = input("Введите команду (add/list/edit/delete/exit): ")

            if command == "add":
                title = input("Введите заголовок заметки: ")
                message = input("Введите тело заметки: ")
                self.add_note(title, message)
                print("Заметка успешно сохранена")
            elif command == "list":
                filter_date = input(
                    "Введите дату для фильтрации (ДД-ММ-ГГГГ) или нажмите Enter для вывода всех заметок: ")
                notes = self.list_notes(filter_date)
                for note in notes:
                    print(note)
            elif command == "edit":
                note_id = int(input("Введите id заметки для редактирования: "))
                new_title = input("Введите новый заголовок заметки: ")
                new_message = input("Введите новое тело заметки: ")
                self.edit_note(note_id, new_title, new_message)
                print("Заметка успешно отредактирована")
            elif command == "delete":
                note_id = int(input("Введите id заметки для удаления: "))
                self.delete_note(note_id)
                print("Заметка успешно удалена")
            elif command == "exit":
                break
            else:
                print("Неверная команда, попробуйте еще раз")
