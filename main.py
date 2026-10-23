from services.pdf_deduplicator import PdfDeduplicator

folder_path = input("Introduce la ruta de la carpeta: ")
deduplicator = PdfDeduplicator(folder_path)
duplicates = deduplicator.find_duplicates()
if not duplicates:
    print("No se encontraron archivos PDF duplicados en la carpeta.")
else:
    print(f"\nSe encontraron {len(duplicates)} grupo(s) de archivos duplicados:")
    for hash_val, file_list in duplicates.items():
        print(f"\n--- Grupo de duplicados (Hash: {hash_val}) ---")
        for file in file_list:
            print(f"  . {file}")


