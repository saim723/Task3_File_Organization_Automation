import os
import pathlib
import shutil

file_format = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.txt', '.docx', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Audio': ['.mp3', '.wav', '.flac'],
    'Archives': ['.zip', '.tar', '.rar', '.gz'],
    'Scripts': ['.py', '.js', '.html', '.css'], 
}

file_type = list(file_format.keys())
file_format = list(file_format.values())

print(file_format)
print(file_type)

for file in os.scandir():
    file_name = pathlib.Path(file)
    file_format_type = file_name.suffix.lower()
    src = str(file_name)
    dest = "Other"

    if file_format_type == "":
        print(f"{src} has no file format")

    else:
        for format in file_format:
            if file_format_type in format:
                folder = file_type[file_format.index(format)]
                print(folder)

                if not os.path.isdir(folder):
                    os.mkdir(folder)
                dest = folder
                break  
            

    if not os.path.isdir("Other"):
        os.mkdir("Other")

    print(src, "moved to", dest, "!")
    shutil.move(src, dest)

print("File Organization Started")
input("\nPress Enter To Exit")