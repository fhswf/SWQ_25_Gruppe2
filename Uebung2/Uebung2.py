# A1 Schwer Verständliche Codeteile FALR CNQZ CNSK
# Vergabe der Id bei neuen Tasks, wenn ID nicht mitgegeben wird
# Nutzen von backup_tasks
# Global tasks nicht global
# Datenstruktur Task unklar
# Print unübersichtlich
# get_task_lenght Warum Schleife
# calculate_task_average Berechnung ist unklar
# upcoming_tasks Sortierung unklar
# process_tasks nicht fertig entwickelt, Sinn unklar
# calculate_task_average Average von was?

# A2 Mögliche Verbesserungen FALR CNQZ CNSK
# ID Vergabe so gestalten, das es nicht zu dopplungen kommen kann
# Task Datenstruktur definieren
# Echte Datenstrukturen nutzen (BSP. Datum nicht als String)
# get_task_lenght Schleife mit tasks.lenght() ersetzen
# Global tasks global definieren
# process_tasks ist für diese Anwendung unnütz, kann enterfent werden

# A3 Code anpassen FALR CNQZ CNSK
# Code als Klasse für Wiederverwendbarkeit, einfache Erweiterbarkeit und Typsicherheit
# Funktionen als Methoden der Klasse (Funktionen inhaltlich angepasst nach Sinnhaftigkeit)
# Erklärung der Funktionen durch Kommentare
# Beispielhafte Nutzung der Funktionen am Ende des Codes nun mit allen Funktionen
# Backup_tasks als Sicherungskopie der Aufgabenliste wird zwar aktuell nicht genutzt, aber für Erweiterungen vorgehalten


import datetime
from dataclasses import dataclass, field
from typing import Dict, Optional

# Globale Task-Listen als Dictionary, damit Aufgaben eindeutig per ID verwaltet werden können
tasks: Dict[int, 'Task'] = {}
backup_tasks: Dict[int, 'Task'] = {}

# Die Task-Datenstruktur wird als dataclass definiert, um Felder klar zu benennen und Typsicherheit zu gewährleisten


@dataclass
class Task:
    name: str  # Name der Aufgabe
    due_date: datetime.date  # Fälligkeitsdatum als echtes Datum
    priority: int = 3  # Priorität, Standardwert 3
    done: bool = False  # Status, ob Aufgabe erledigt ist
    user: str = 'user1'  # Benutzer, dem die Aufgabe zugeordnet ist
    created_at: datetime.datetime = field(
        default_factory=datetime.datetime.now)  # Erstellungszeitpunkt

    def __str__(self):
        # Übersichtliche Darstellung der Aufgabe für die Ausgabe
        status = 'Erledigt' if self.done else 'Offen'
        return (f"{self.name} (Prio: {self.priority}) - bis {self.due_date.strftime('%d-%m-%Y')} - {status} "
                f"[Erstellt: {self.created_at.strftime('%d-%m-%Y %H:%M')}, User: {self.user}]")


def add_task(name: str, due_date: str, priority: int = 3, task_id: Optional[int] = None, user: str = 'user1') -> int:
    """
    Erstellt eine neue Aufgabe und fügt sie der globalen Aufgabenliste hinzu.
    Input:
        name (str): Name der Aufgabe
        due_date (str): Fälligkeitsdatum im Format 'TT-MM-YYYY'
        priority (int, optional): Priorität der Aufgabe (Standard: 3)
        task_id (int, optional): Optionale ID, sonst automatisch generiert
        user (str, optional): Benutzername (Standard: 'user1')
    Output:
        int: Die vergebene eindeutige Task-ID
    """
    global tasks, backup_tasks
    # Das Fälligkeitsdatum wird als echtes Datum gespeichert, nicht als String
    due_date_obj = datetime.datetime.strptime(due_date, "%d-%m-%Y").date()
    if task_id is None:
        # Eindeutige ID-Vergabe: Unix-Timestamp in Mikrosekunden, um Dopplungen zu vermeiden
        task_id = int(datetime.datetime.now().timestamp() * 1_000_000)
        while task_id in tasks:
            task_id += 1  # Falls es doch eine Kollision gibt, wird die ID erhöht
    # Die Aufgabe wird als Task-Objekt gespeichert, nicht als Liste
    task = Task(name=name, due_date=due_date_obj, priority=priority, user=user)
    tasks[task_id] = task
    backup_tasks[task_id] = task  # backup_tasks dient als Sicherungskopie
    return task_id


def remove_task(task_id: int) -> bool:
    """
    Entfernt eine Aufgabe anhand ihrer ID aus der Aufgabenliste.
    Input:
        task_id (int): Die ID der zu entfernenden Aufgabe
    Output:
        bool: True, wenn die Aufgabe entfernt wurde, sonst False
    """
    global tasks
    # Entfernt eine Aufgabe anhand ihrer ID
    if task_id in tasks:
        del tasks[task_id]
        return True
    return False


def mark_done(task_name: str) -> str:
    """
    Markiert eine Aufgabe mit dem gegebenen Namen als erledigt.
    Input:
        task_name (str): Name der Aufgabe
    Output:
        str: Rückmeldungstext ("Erledigt")
    """
    global tasks
    # Setzt den Status einer Aufgabe auf erledigt, wenn der Name übereinstimmt
    for task in tasks.values():
        if task.name == task_name:
            task.done = True
    return "Erledigt"


def show_tasks():
    """
    Gibt alle Aufgaben mit ihren Details auf der Konsole aus.
    Input: Keine
    Output: Keine (Ausgabe erfolgt per print)
    """
    global tasks
    # Gibt alle Aufgaben übersichtlich aus, wenn es keine gibt, wird eine Meldung ausgegeben
    if not tasks:
        print("Keine Aufgaben vorhanden.")
        return
    print("\nAlle Aufgaben:")
    for task_id, task in tasks.items():
        print(f"ID {task_id}: {task}")


def calculate_task_average() -> float:
    """
    Berechnet die durchschnittliche Priorität aller Aufgaben.
    Input: Keine
    Output:
        float: Durchschnittliche Priorität (0.0 falls keine Aufgaben)
    """
    # Berechnet die durchschnittliche Priorität aller Aufgaben
    if not tasks:
        return 0.0
    total_priority = sum(task.priority for task in tasks.values())
    avg = total_priority / len(tasks)
    return avg

# def process_tasks(): gelöscht, da unnütz


def upcoming_tasks():
    """
    Gibt alle offenen Aufgaben zurück, die ab heute fällig sind, sortiert nach Fälligkeitsdatum.
    Input: Keine
    Output:
        list[Task]: Liste der offenen, anstehenden Aufgaben
    """
    # Gibt alle offenen Aufgaben zurück, die ab heute fällig sind, sortiert nach Fälligkeitsdatum
    today = datetime.date.today()
    upcoming = sorted(
        [task for task in tasks.values() if task.due_date >=
         today and not task.done],
        key=lambda x: x.due_date
    )
    return upcoming


def cleanup():
    """
    Entfernt alle erledigten Aufgaben aus der Aufgabenliste.
    Input: Keine
    Output: Keine (verändert globale tasks)
    """
    global tasks
    # Entfernt alle erledigten Aufgaben aus der Liste
    tasks = {tid: task for tid, task in tasks.items() if not task.done}


def get_task_count() -> int:
    """
    Gibt die Anzahl der offenen Aufgaben zurück.
    Input: Keine
    Output:
        int: Anzahl der offenen Aufgaben
    """
    # Gibt die Anzahl der offenen Aufgaben zurück, nun durch Nutzung von len()
    return len(tasks)


# Beispielhafte Nutzung der Funktionen nun mit allen Funktionen
# Aufgaben werden hinzugefügt, IDs werden automatisch eindeutig vergeben
id1 = add_task("Projekt abschließen", "25-05-2025", 1)
id2 = add_task("Projekt abschließen", "25-12-2025", 1)
id3 = add_task("Einkaufen gehen", "21-05-2025", 3)
id4 = add_task("Dokumentation schreiben", "30-05-2025", 2)
# Eine Aufgabe wird als erledigt markiert
mark_done("Einkaufen gehen")
# Alle Aufgaben werden angezeigt
show_tasks()
print("\nOffene Aufgaben nach Datum sortiert:")
# Offene Aufgaben nach Fälligkeitsdatum sortiert ausgeben
for task in upcoming_tasks():
    print(task)
# Durchschnittliche Priorität aller Aufgaben ausgeben
print(f"\nDurchschnittliche Priorität: {calculate_task_average():.2f}")
# Erledigte Aufgaben werden entfernt
cleanup()
# Anzahl der offenen Aufgaben ausgeben
print(f"\nGesamtzahl der offenen Aufgaben: {get_task_count()}")
