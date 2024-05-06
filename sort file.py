import os
import shutil

pyt = os.getcwd()
print(pyt)


with os.scandir(pyt) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            filename, file_extension = os.path.splitext(entry.name)
            hooeta = filename+file_extension
            if not os.path.exists(file_extension):
                if hooeta != os.path.basename(__file__):
                    os.makedirs(file_extension)
                    print(f"Папка для расширения {file_extension} успешно создана.")
            if hooeta != os.path.basename(__file__):
                shutil.move(hooeta, file_extension)


