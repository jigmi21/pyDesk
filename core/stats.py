import os
files = []
folders = []
def run_stats (path:str, human = False, verbose = False):
    for (root, dirs, files , rootfd) in os.fwalk (path):
        files.append(files)
        folders.append(dirs)
    return root