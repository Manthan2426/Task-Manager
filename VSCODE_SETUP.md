# Task Manager – VS Code Setup Guide

## Step 1: Install VS Code Extensions

Open VS Code → click the **Extensions icon** on the left sidebar (or press `Ctrl+Shift+X`) → search and install these:

| Extension Name | Publisher | Why you need it |
|---|---|---|
| **Python** | Microsoft | Core extension — syntax highlighting, IntelliSense, debugging for Python |
| **Pylance** | Microsoft | Fast, smart autocomplete and error checking (usually auto-installs with Python extension) |
| **Jinja** (optional) | wholroyd | Syntax highlighting for Flask's HTML templates |
| **SQLite Viewer** (optional) | Florian Klampfer / qwtel | Lets you open and view the `tasks.db` file visually inside VS Code |
| **GitLens** (optional but recommended) | GitKraken | Makes Git operations (commit, push, history) easier to see and manage |
| **Live Server** (optional) | Ritwick Dey | Not required for Flask, but handy for quickly previewing plain HTML files |

**Minimum required:** Just **Python** (Pylance comes bundled automatically). Everything else is a convenience.

---

## Step 2: Install Python (if not already installed)

Check if Python is installed by opening a terminal in VS Code (`` Ctrl+` ``) and running:
```powershell
python --version
```
If it shows a version (e.g., `Python 3.12.x`), you're good. If not, download it from [python.org/downloads](https://www.python.org/downloads/) and **make sure to check "Add Python to PATH"** during install.

---

## Step 3: Open the Project Folder

1. Extract the `task-manager-api.zip` file (right-click → Extract All)
2. In VS Code: **File → Open Folder** → select the extracted `task-manager-api` folder
3. VS Code should show `app.py`, `requirements.txt`, `templates/`, `.gitignore` in the sidebar

---

## Step 4: Create a Virtual Environment (recommended)

In the VS Code terminal (`` Ctrl+` ``), inside the project folder:

```powershell
python -m venv venv
```

Activate it:
```powershell
venv\Scripts\activate
```
(On Mac/Linux: `source venv/bin/activate`)

You'll see `(venv)` appear at the start of your terminal line — that means it's active.

> VS Code may show a popup: *"We noticed a new environment has been created"* → click **Yes, use this environment**.

---

## Step 5: Install Dependencies

```powershell
pip install -r requirements.txt
```

This installs `Flask` and `Flask-SQLAlchemy`.

---

## Step 6: Run the App

```powershell
python app.py
```

You should see output like:
```
 * Running on http://127.0.0.1:5000
```

Open that link in your browser — you'll see the Task Manager UI.

To stop the server: press `Ctrl+C` in the terminal.

---

## Step 7: Verify Everything Works

- Add a task using the form → it should appear in the list below
- Click **Complete** → title gets struck through
- Click **Delete** → task disappears
- A file called `tasks.db` will appear in your folder — that's your SQLite database (created automatically on first run)

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `'python' is not recognized` | Python isn't in PATH — reinstall Python and check "Add to PATH" |
| `Could not open requirements file` | You're not inside the project folder — run `cd path\to\task-manager-api` first |
| `ModuleNotFoundError: No module named flask` | Virtual environment isn't activated, or `pip install -r requirements.txt` wasn't run |
| Port 5000 already in use | Close other running Flask apps, or edit the last line of `app.py` to `app.run(debug=True, port=5001)` |

---

## Author
Manthan Sahu
