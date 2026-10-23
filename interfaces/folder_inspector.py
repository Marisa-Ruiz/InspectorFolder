from pathlib import Path

class FolderInspector:
    def __init__(self, folder_path):
        self.folder_path = Path(folder_path)

    def list_files(self):
        files = []
        for item in self.folder_path.iterdir():
            if item.is_file():
                files.append(item)
        return files
