#!/usr/bin/python3
import os, sys, stat
from stat import *

# This will build the find command based on the command line arguments.
cmd = 'find ' + sys.argv[1] + ' -name *' + sys.argv[2] + '*'
print(cmd)

# Executes the command and will store the result in a variable.
listOfFiles = os.popen(cmd).read()
listOfFiles = listOfFiles.split()
totalSize = 0

# For each file in the output list,
for line in listOfFiles:
    statinfo = os.stat(line)

# If the file is regular, print its file name and size.
if stat.S_ISREG(statinfo.st_mode):
    print(line, statinfo.st_size, 'bytes')
    totalSize += statinfo.st_size
# If file is not regular, just print the file name.
else:
    print(line, '...')
print('Total file size:', totalSize, 'bytes')
