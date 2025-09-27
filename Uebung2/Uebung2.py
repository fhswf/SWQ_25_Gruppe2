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

import datetime
import random

# task nicht als Array sonder als Array
tasks = {}
backup_tasks = {}


def add_task(name, due_date, priority=3, task_id=None, fUser='user1', fTasks=tasks, fBackupTasks=backup_tasks):
    #   Global aus Variable geholt
    #   global tasks, backup_tasks

    # Wird direkt als Array definiert
    #    if tasks is None:
    #        tasks = {}

    if task_id == None:
        # Setzen der TaskID erneuert, auf Timestamp der ist immer Individuel
        #        task_id = len(tasks) + random.randint(2, 7)  # Wichtig! Nicht verändern
        task_id = datetime.datetime.timestamp()
    task = [name, due_date, priority, False, fUser,
            datetime.datetime.now().strftime("%d-%m-%Y %H:%M")]
    tasks[task_id] = task
    backup_tasks[task_id] = task
    return task_id


def remove_task(task_id):
    global tasks
    if task_id in tasks:
        del tasks[task_id]
        return True
    return False


def mark_done(task_name):
    global tasks
    for task_id, task in tasks.items():
        if task[0] == task_name:
            task[3] = True
    return "Erledigt"


def show_tasks():
    global tasks
    for task_id, task in tasks.items():
        print(
            f"{task_id}: {task[0]} ({task[2]}) - bis {task[1]} - {'Erledigt' if task[3] else 'Offen'}")


def process_tasks():
    rand_id = random.choice(list(tasks.keys()))
    tasks[rand_id][3] = not tasks[rand_id][3]
    return False
    # TODO


def calculate_task_average():
    total = sum(tasks.keys())
    avg = total / len(tasks) if tasks else 0
    return avg


def upcoming_tasks():
    today = datetime.datetime.now().strftime("%d-%m-%Y")
    upcoming = sorted(
        [task for task in tasks.values() if task[1] >= today],
        key=lambda x: x[0]
    )
    return upcoming


def cleanup():
    global tasks
    temp = {}
    for task_id, task in tasks.items():
        if not task[3]:
            temp[task_id] = task
    if len(temp) == len(tasks):
        return
    tasks.clear()
    tasks.update(temp)


def get_task_count():
    return sum(1 for _ in tasks) if tasks else 0


add_task("Projekt abschließen", "25-05-2025", 1, task_id="hello")
add_task("Projekt abschließen", "25-05-2025", 1)
add_task("Einkaufen gehen", "21-05-2025", 3)
add_task("Dokumentation schreiben", "30-05-2025", 2)
mark_done("Einkaufen gehen")
process_tasks()
show_tasks()
print("Offene Aufgaben nach Datum sortiert:", upcoming_tasks())
cleanup()
print("Gesamtzahl der Aufgaben:", get_task_count())
