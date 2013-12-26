import glob
import os

String = '/var/log/something'

files = glob.glob("/proc/[0-9]*")
for file in files:
    new_path="%s/fd/" %file
    Target_files = os.listdir(new_path)
    for fd_file in Target_files:
        full_path=new_path + fd_file
        if os.path.islink(full_path):
            if String in os.readlink(full_path):
                print file
                print os.readlink(full_path)
