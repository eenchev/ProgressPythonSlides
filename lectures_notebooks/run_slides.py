import subprocess
import sys
import platform
import argparse

parser=argparse.ArgumentParser(
    description='''Simple script to run ipynb notebooks as slides ''')
parser.add_argument('--file', type=str, default='1.Python101.ipynb', 
    help='Specifies the target file. If left empty runs 1.Python101.ipynb')
args=parser.parse_args()


command_string = 'jupyter nbconvert {} --to slides --post serve'.format(args.file)
os_platform = platform.system()

if os_platform == 'Windows':
    subprocess.call(['C:\\windows\\system32\\cmd.exe',
                '/C', 
                command_string])
                
elif os_platform == 'Linux':
    subprocess.call(command_string, shell=True)

else:
    print('Unrecognized platform')