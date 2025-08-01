#file organizor

import pathlib
import shutil

def organize_directory(path_str):
    target_path = pathlib.Path(path_str)
    if not target_path.is_dir():
        print(f"❌ Error: '{path_str}' is not a valid directory.")
        return
    CATEGORIES = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".heic", ".webp", ".bmp"],
        "Documents": [".pdf", ".docx", ".doc", ".xlsx", ".pptx", ".txt", ".csv", ".rtf"],
        "Audio": [".mp3", ".wav", ".aac", ".m4a"],
        "Video": [".mp4", ".mov", ".avi", ".mkv"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Scripts": [".py", ".js", ".sh", ".bat", ".html", ".css"],
    }
    print(f"\n🚀 Starting organization of: {target_path.resolve()}\n")
    for file_path in target_path.iterdir():
        if file_path.is_dir() or file_path.name == __file__:
            continue

        file_suffix = file_path.suffix.lower()
        moved = False
        for category, suffixes in CATEGORIES.items():
            if file_suffix in suffixes:
                dest_dir = target_path / category
                dest_dir.mkdir(exist_ok=True)
                shutil.move(str(file_path), str(dest_dir))
                print(f"Moved: '{file_path.name}'  ->  '{category}/'")
                moved = True
                break
        if not moved:
            dest_dir = target_path / "Other"
            dest_dir.mkdir(exist_ok=True)
            shutil.move(str(file_path), str(dest_dir))
            print(f"Moved: '{file_path.name}'  ->  'Other/'")

    print("\n✅ Organization complete!")

if __name__ == "__main__":
    directory_to_organize = input("Enter the full path of the directory you want to organize: ")
    organize_directory(directory_to_organize)