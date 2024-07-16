import os
import shutil
from pathlib import Path

files_dict = {
    "zips": ['zip', 'jar', 'rar', '7z', 'tar', 'gz', 'bz2'],
    "text files": ['pdf', 'txt', 'docx', 'pptx', 'doc', 'ppt', 'xls', 'xlsx', 'odt', 'ods', 'rtf'],
    "installers": ['exe', 'dmg', 'msi', 'pkg'],
    "music": ['osz', 'mp3', 'wav', 'flac', 'aac', 'ogg', 'wma'],
    "images": ['jpg', 'png', 'svg', 'jpeg', 'gif', 'bmp', 'tiff', 'webp'],
    "code": ['py', 'java', 'c', 'h', 'cpp', 'js', 'html', 'css', 'ts', 'rb', 'php', 'sql', 'json', 'xml']
}

#path
downloads_path = 'D:\\Downloads' # directory you want to clean
folders_path = Path(downloads_path) / 'folders'
folders_path.mkdir(exist_ok=True)

# additional directories per my keys in the dict
for category in files_dict.keys():
    category_path = Path(downloads_path) / category
    category_path.mkdir(exist_ok=True)

for file in os.listdir(downloads_path):
    file_path = Path(downloads_path) / file
    if file_path.is_file():
        file_extension = os.path.splitext(file_path)[1].lower().strip('.')
        
        for category, extensions in files_dict.items():
            if file_extension in extensions:
                destination_dir = Path(downloads_path) / category
                shutil.move(file_path, destination_dir)
                
    elif file_path.is_dir() and file_path.name not in files_dict.keys() and file_path.name != "folders":
        shutil.move(file_path, folders_path)
        

    
        
    