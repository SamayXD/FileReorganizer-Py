import os
import collections
from pprint import pprint


EXT_AUDIO = ['mp3']
EXT_VIDEO = ['mp4', 'mkv']
EXT_IMAGE = ['jpeg', 'png', 'jpg']
EXT_DOC = ['pdf', 'txt', 'docs', 'docx']
EXT_COMP = ['zip', 'rar']
EXT_APP = ['dmg' , 'exe']

pathB = 'YOUR PATH HERE/'
BASE_PATH = os.path.expanduser(pathB)
DEST_DIRS = ['Downloads', 'Music', 'Images', 'Videos', 'Docs', 'Apps', 'others']

for d in DEST_DIRS:
    dir_path = os.path.join(BASE_PATH, d)
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    
DOWNLOADS_PATH = os.path.join(BASE_PATH, 'Downloads')
files_mapping = collections.defaultdict(list)

files_list = os.listdir(DOWNLOADS_PATH)

pprint(files_mapping)
print(files_list)

for file_name in files_list:
    if file_name[0] != '.':
        file_ext = file_name.split('.')[-1]
        files_mapping[file_ext].append(file_name)
    
pprint(files_mapping)


for f_ext, f_list in files_mapping.items():
    if f_ext in EXT_IMAGE:
        for file in f_list:
           os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Images', file))

for f_ext, f_list in files_mapping.items():
    if f_ext in EXT_VIDEO:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Videos', file))

    elif f_ext in EXT_DOC:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Docs', file))

    elif f_ext in EXT_COMP:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'others', file))

    elif f_ext in EXT_APP:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Apps', file))

    elif f_ext in EXT_AUDIO:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Music', file))
    
    else:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'others', file))
