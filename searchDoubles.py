import os
import glob


class File:
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.duplicates = []

    def add_duplicate(self, file):
        self.duplicates.append(file.path)

    def is_duplicate(self):
        return len(self.duplicates) > 0


path = ['C:/Users/jessi/Pictures/Saved Pictures', 'C:/Users/jessi/Pictures/Saved Pictures/test']

#put all JPG files in a List
jpg_files = []
for p in path:
    jpg_files.extend(glob.glob(os.path.join(p, '*.jpg')))

files = []
for file_path in jpg_files:
    file_name = os.path.basename(file_path)
    files.append(File(file_name, file_path))

# Check for duplicates
for file1 in files:
    for file2 in files:
        if file1 is not file2 and file1.name == file2.name:
            if file1.path != file2.path and file2.path not in file1.duplicates:
                file1.add_duplicate(file2)

# Print duplicates
for file in files:
    if file.is_duplicate():
        print(f'{file.name} has duplicates:')
        for duplicate in file.duplicates:
            print(f"    {duplicate}")