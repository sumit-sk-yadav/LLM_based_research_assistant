import os
from pathlib import Path

list_of_files = [
    'data/',
    'embeddings/',
    'scripts/__init__.py',
    'app/',
    '.gitignore'
]


for path in list_of_files:
    full_path = Path(path)
    
    if path.endswith('/'):
        os.makedirs(path, exist_ok=True)
    else:
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.touch(exist_ok=True)


print('__________________FOLDER STRUCTURE CREATED_____________________')