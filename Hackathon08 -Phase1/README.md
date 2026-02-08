# MyTodoApp CLI - Advanced User Guide

A robust, local-first command-line task manager with priorities, tags, discovery, and notifications.

## 🚀 Advanced Features

### 🛠️ Organization
Categorize tasks with priorities and tags.
```bash
# Set priority (high, medium, low)
python src/todo.py add "Fix server" --priority high

# Add tags
python src/todo.py add "Buy milk" --tags "personal,grocery"
```

### 📋 Discovery
Find exactly what you need with filters, sorting, and search.
```bash
# Filter by status or priority
python src/todo.py list --filter status=pending
python src/todo.py list --filter priority=high

# Sort by due date or priority
python src/todo.py list --sort due_date

# Search keyword in description or tags
python src/todo.py search "server"
```

### ⏰ Time Management
Set due dates and recurring tasks.
```bash
# Add task due tomorrow
python src/todo.py add "Meeting" --due "2026-01-02"

# Add recurring task
python src/todo.py add "Weekly Sync" --due "2026-01-02" --recurrence weekly
```

### 🔔 Notifications
Stay informed with system-level alerts.
```bash
# Start the notification service
python src/todo.py notify-service
```

---

## 💾 Installation & Dev
```bash
pip install python-dateutil
python -m unittest discover tests/unit
python -m unittest discover tests/integration
```
