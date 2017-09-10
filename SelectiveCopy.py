#! python3
# SelectiveCopy.py : select specific file type (.pdf) and copy to other folder

import os, re, shutil



def selectcopy(folder, target, type):
    folder = os.path.abspath(folder)
    target = os.path.abspath(target)
    print(target)

    if not os.path.exists(target):
        os.makedirs(target)

    for foldername, subfolder, filenames in os.walk(folder):
        print('.'+str(type))
        for filename in filenames:
            if filename.startswith('Yuanta') and filename.endswith('.'+str(type)):
               shutil.copy(os.path.join(foldername, filename),target)


selectcopy('/Users/paperboy/Downloads', '/Users/paperboy/Desktop/信用卡帳單', 'pdf')



