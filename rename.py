
from shutil import copyfile
import os
import ntpath


import glob
files =  glob.glob('CW/*.*',)

for file in files:
    print(file)
    if not os.path.isdir(f'{os.getcwd()}/CW_new/'):
        os.mkdir(f'{os.getcwd()}/CW_new/')
    
    copyfile(file, 'CW_new/' + os.path.basename(file).replace('\\','__'))
