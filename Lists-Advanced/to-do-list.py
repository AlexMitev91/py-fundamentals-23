todo_list = []

while True:
    note = input()
    
    if note == "End":
        break

    importance, todo = note.split('-', 1)
    importance = int(importance)
    
    todo_list.append((importance, todo))
    
todo_list.sort(key=lambda x: x[0])

sorted_notes = [f"{note}" for importance, note in todo_list]

print(sorted_notes)