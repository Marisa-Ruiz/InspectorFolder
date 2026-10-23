import hashlib

from interfaces.folder_inspector import FolderInspector

class PdfDeduplicator(FolderInspector):
    def __init__(self, folder_path):
        super().__init__(folder_path)

    def get_pdf_files(self):
        all_files = self.list_files()
        pdf_files = []
        for file in all_files:
            if file.suffix.lower() == ".pdf":
                pdf_files.append(file)
        return pdf_files

    def calculate_hash(self, files_path):
        hasher = hashlib.md5()
        with open(files_path, 'rb') as f:
            hasher.update(f.read())
        return hasher.hexdigest()

    def find_duplicates(self):
        pdf_files = self.get_pdf_files()
        hashes = {}

        for file in pdf_files:
            file_hash = self.calculate_hash(file)

            if file_hash not in hashes:
                hashes[file_hash] = []

            hashes[file_hash].append(file)

        duplicates = {}
        for h, files in hashes.items():
            if len(files) > 1:
                duplicates[h] = files

        return duplicates
