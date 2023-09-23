import tkinter as tk

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "complete": False})

    def mark_complete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["complete"] = True

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]


class TodoListApp:
    def __init__(self, root):
        self.todo_list = TodoList()
        self.root = root
        self.root.title("To-Do List App")

        # Task entry widget
        self.task_entry = tk.Entry(root)
        self.task_entry.pack(pady=10)

        # Add Task button
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        # Listbox to display tasks
        self.tasks_listbox = tk.Listbox(root)
        self.tasks_listbox.pack(pady=10)

        # Mark Complete button
        self.mark_complete_button = tk.Button(root, text="Mark Complete", command=self.mark_complete)
        self.mark_complete_button.pack()

        # Delete Task button
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_list.add_task(task)
            self.update_tasks_listbox()

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.todo_list.tasks:
            status = "✓" if task["complete"] else " "
            self.tasks_listbox.insert(tk.END, f"[{status}] {task['task']}")

    def mark_complete(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            self.todo_list.mark_complete(selected_index[0])
            self.update_tasks_listbox()

    def delete_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            self.todo_list.delete_task(selected_index[0])
            self.update_tasks_listbox()

# Create the main window
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
    
