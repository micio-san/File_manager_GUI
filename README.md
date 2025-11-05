# 🗂️ File Organizer with GUI – Key Steps

## 🎯 Goal
Build a desktop application that automatically sorts files in a ##chosen## folder into subfolders based on **file type**, **size**, or **creation date**, with a simple graphical interface.

---

## 🧱 Step-by-Step Plan

### 1. Project Setup
- Create a new project directory (e.g., `file-organizer/`).
- Initialize a virtual environment.
- Create a `requirements.txt` file (e.g., `tkinter`, `PyQt5` if using PyQt).
- Add `.gitignore` and `README.md`.

---

### 2. Folder Structure
file-organizer/
├─ README.md
├─ requirements.txt
├─ src/
│ ├─ main.py # App entry point (starts GUI)
│ ├─ gui.py # GUI window, buttons, and event handlers
│ ├─ worker.py # Handles background file operations
│ ├─ organizer/
│ │ ├─ core.py # Main organizing logic
│ │ ├─ file_utils.py # Scanning and moving files
│ │ ├─ classifiers.py # Sorting logic by type, size, or date
│ │ └─ settings.py # Default thresholds and file mappings
│ └─ utils/
│ ├─ logger.py # Log to file and GUI
│ └─ helpers.py # Helper functions
├─ tests/
  ├─ test_classifiers.py
  └─ test_file_utils.py


### 3. Core File Operations
- **scan_folder(path)** → Retrieve all files with size, type, and date info.
- **classify_by_type(file)** → Return folder name (e.g., `Images`, `Documents`).
- **classify_by_size(file)** → Sort by thresholds: Small / Medium / Large.
- **classify_by_date(file)** → Group by creation date (e.g., `2025-11`).
- **safe_move(src, dest)** → Move files safely; handle duplicates or errors.

---

### 4. GUI Design (Tkinter or PyQt5)
**Main window should include:**
- Folder picker (`Browse...` button)
- Sorting mode selection (`Type`, `Size`, `Date`)
- Options (e.g., include subfolders, dry run)
- “Organize” and “Cancel” buttons
- Progress bar + log area for status updates

**Optional features:**
- Settings popup (to configure size thresholds and extension mappings)
- Summary at the end (files moved, skipped, errors)

---

### 5. Threading & Responsiveness
- Run file organization in a **background thread**.
- Use Tkinter’s `.after()` or a queue to update progress safely.
- Prevent GUI freezing during long operations.

---

### 6. Logging & Reporting
- Keep a log of all actions (`organize.log`).
- Display live status updates in the UI.
- Provide a summary after completion.

---

### 7. Error Handling
- Handle permission issues and invalid paths gracefully.
- Implement duplicate name resolution (e.g., `file (1).txt`).
- Optionally skip hidden/system files.

---

### 8. Extra Features (Optional)
- **Dry run mode:** Preview actions without moving files.
- **Undo last operation:** Save move history in a JSON file.
- **Custom mappings:** Let users define new categories.
- **Packaging:** Use PyInstaller to create a `.exe` or `.app`.

---

### 9. Size & Type Classification Defaults
**Size thresholds:**
| Category | Range         |
|-----------|---------------|
| Small     | < 1 MB        |
| Medium    | 1–100 MB      |
| Large     | > 100 MB      |

**Type mapping:**
| Category | Extensions |
|-----------|-------------|
| Images | .jpg, .png, .gif, .bmp |
| Documents | .pdf, .docx, .txt, .xlsx |
| Audio | .mp3, .wav |
| Video | .mp4, .mkv |
| Archives | .zip, .rar, .tar |
| Others | Everything else |

---

### 10. Development Milestones
1. Implement file scanning and classification logic.
2. Add move functionality with error handling.
3. Build a simple Tkinter GUI.
4. Add progress updates and logging.
5. Enable settings and dry-run features.
6. Polish UI and package application.

---

### ✅ Final Outcome
A simple, user-friendly **File Organizer app** that:
- Automatically categorizes and moves files.
- Lets users choose how to sort (Type / Size / Date).
- Provides feedback and logs.
- Keeps the UI responsive and clean.

---
