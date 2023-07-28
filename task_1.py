import json
import os
import datetime

NOTES_FILE = "notes.json"


def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            return json.load(file)
    else:
        return []


def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file)


def add_note():
    title = input("Введите заголовок заметки: ")
    msg = input("Введите тело заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "msg": msg,
        "timestamp": timestamp,
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена")


def read_notes():
    for note in notes:
        print(f"{note['id']}. {note['title']}")
        print(note['msg'])
        print(note['timestamp'])
        print()


def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note['id'] == note_id:
            new_title = input("Введите новый заголовок заметки: ")
            new_msg = input("Введите новое тело заметки: ")
            note['title'] = new_title
            note['msg'] = new_msg
            note['timestamp'] = datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована")
            break
    else:
        print("Заметка с таким ID не найдена")


def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена")
            break
    else:
        print("Заметка с таким ID не найдена")


def filter_notes_by_date():
    date_str = input("Введите дату для фильтрации (в формате ГГГГ-ММ-ДД): ")
    try:
        date_filter = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        filtered_notes = [note for note in notes if
                          datetime.datetime.strptime(note['timestamp'],
                                                     "%Y-%m-%d %H:%M:%S").date() == date_filter]
        if filtered_notes:
            print("Список заметок за выбранную дату:")
            for note in filtered_notes:
                print(f"{note['id']}. {note['title']}")
                print(note['msg'])
                print(note['timestamp'])
                print()
        else:
            print("Заметки за выбранную дату не найдены")
    except ValueError:
        print("Ошибка ввода даты")


if __name__ == "__main__":
    notes = load_notes()

    while True:
        print("\n===== Команды =====")
        print("add - добавить новую заметку")
        print("read - прочитать список заметок")
        print("edit - редактировать заметку")
        print("delete - удалить заметку")
        print("filter - фильтровать заметки по дате")
        print("exit - выход из программы")

        command = input("Введите команду: ").lower()

        if command == "add":
            add_note()
        elif command == "read":
            read_notes()
        elif command == "edit":
            edit_note()
        elif command == "delete":
            delete_note()
        elif command == "filter":
            filter_notes_by_date()
        elif command == "exit":
            break
        else:
            print("Неизвестная команда")