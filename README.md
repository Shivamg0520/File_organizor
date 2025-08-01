# 📂 File Organizer

A command-line Python script to automatically sort files within a directory into organized, category-based folders.

---

## 📖 Overview

This script scans a specified directory and moves each file into a subfolder corresponding to its file type. For example, all `.jpg` and `.png` files are moved into an `Images` folder, and `.pdf` and `.docx` files are moved into a `Documents` folder. This helps declutter folders like your "Downloads" or "Desktop" with a single command.

---

## ✨ Key Features

* **Automated Sorting**: Moves files into folders like `Images`, `Documents`, `Audio`, `Video`, etc.
* **Smart Categorization**: Uses a dictionary of file extensions for easy and accurate sorting.
* **"Other" Category**: Any file type not recognized is safely moved to an `Other` folder, ensuring no file is left behind.
* **Safe Operation**: The script automatically ignores subdirectories and itself to prevent errors.
* **User-Friendly**: Simply run the script and provide a directory path when prompted.
* **Easy to Customize**: Add new file extensions or entire categories just by editing the `CATEGORIES` dictionary in the source code.

---

## 🚀 Getting Started

### Prerequisites

* **Python 3.x** must be installed on your system.

### Instructions

1.  **Save the Script**: Save the code as a Python file (e.g., `organize_files.py`).
2.  **Open Terminal**: Launch your terminal (Command Prompt on Windows, Terminal on macOS/Linux).
3.  **Navigate to the Script's Location (Optional)**: If the script is not in the directory you want to organize, you can still run it by providing the full path.
4.  **Run the Script**: Execute the following command:
    ```bash
    python organize_files.py
    ```
5.  **Provide the Path**: When prompted, type or paste the full path to the directory you want to clean up and press `Enter`.
    ```
    Enter the full path of the directory you want to organize: C:\Users\YourUser\Downloads
    ```
6.  **Watch the Magic**: The script will print the actions as it moves each file. Once finished, a "complete" message will be displayed.

---

## 🔧 Customization

To add new file types or categories, simply edit the `CATEGORIES` dictionary within the script file.

**Example**: To add support for `.svg` images and a new `Code` category for `.java` files:

```python
# Original
"Images": [".jpg", ".jpeg", ".png", ".gif", ".heic", ".webp", ".bmp"],
"Scripts": [".py", ".js", ".sh", ".bat", ".html", ".css"],

# Modified
"Images": [".jpg", ".jpeg", ".png", ".gif", ".heic", ".webp", ".bmp", ".svg"],
"Scripts": [".py", ".js", ".sh", ".bat", ".html", ".css"],
"Code": [".java"] # New Category
```

---

## 📄 License

This script is released under the MIT License. See the `LICENSE` file for more details.
