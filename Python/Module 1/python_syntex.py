" This file is calling by commandline arguments example:-{python python_syntex.py sumit 40}"

import sys

# print('argv len : ',len(sys.argv))

if len(sys.argv) != 3:
    raise ValueError("Please provide your name and age")
print(f'Your name is {sys.argv[1]} and your age is {sys.argv[2]}')
print(f'len of the sys argv is - {len(sys.argv)}')
