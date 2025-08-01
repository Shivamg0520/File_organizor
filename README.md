# File_organizor
📂 File Organizer
A command-line Python script to automatically sort files in a directory into clean, categorized folders. Say goodbye to cluttered folders and find your files with ease.

🤔 What It Does
This script scans a directory of your choice and moves files into subfolders based on their extension. For example, all .png and .jpg files will be moved into an Images folder, and all .pdf and .docx files will go into a Documents folder.

Any file type that isn't recognized will be safely placed in an Other folder.

✨ Key Features
Smart Categorization: Sorts files into Images, Documents, Audio, Video, Archives, and Scripts.

Safe to Run: The script only moves files. It will not delete anything. It also ignores any existing folders and the script file itself.

User-Friendly: Just run the script and provide a folder path. No complex setup is needed.

Easy to Customize: You can easily add new file types or create new categories by editing the CATEGORIES dictionary directly in the script.

Cross-Platform: Works on Windows, macOS, and Linux without any changes.

🚀 Getting Started
Save the Script: Make sure the script is saved as a Python file (e.g., organize_directory.py).

Open Terminal: Launch your terminal or command prompt.

Run the Script: Navigate to the directory where you saved the script and run it with the following command:

python organize_directory.py

Provide the Path: When prompted, paste or type the full path to the folder you want to organize and press Enter.

Enter the full path of the directory you want to organize: C:\Users\YourUser\Downloads

Watch the Magic: The script will report its progress as it moves each file and will notify you when the organization is complete.

🔧 How to Customize
You can tailor the script to your needs by editing the CATEGORIES dictionary.

For instance, if you want to add .svg files to the Images category and create a new Fonts category, you would modify the dictionary as follows:

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".heic", ".webp", ".bmp", ".svg"],  # .svg added
    "Documents": [".pdf", ".docx", ".doc", ".xlsx", ".pptx", ".txt", ".csv", ".rtf"],
    "Audio": [".mp3", ".wav", ".aac", ".m4a"],
    "Video": [".mp4", ".mov", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".sh", ".bat", ".html", ".css"],
    "Fonts": [".ttf", ".otf", ".woff"]  # New category for fonts
}

📄 License
This script is freely available for use under the MIT License.
