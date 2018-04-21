import subprocess
import sys
import platform
import argparse

try:
    from pip import main as pipmain
except:
    from pip._internal import main as pipmain

try:
    import jupyter
except ImportError:
    pipmain(['install', 'jupyter'])

parser=argparse.ArgumentParser(
    description='''Simple script to run ipynb notebooks as slides.
            Installs jupyter if not present.''')
parser.add_argument('--file', type=str, default='1.Python101.ipynb', 
    help='Specifies the target file. If left empty runs 1.Python101.ipynb')
args, unknown = parser.parse_known_args()

if len(unknown)>1:
    parser.print_help()
    print('\nYou passed extra arguments. Did you try to pass filename?'
            ' Try the --file argument. Please refer to the help above.')
    sys.exit(1)

elif len(unknown) == 1:
    file_name = unknown[0]

else:
    file_name = args.file

def check_extension(f_name, extension=".ipynb"):
    if f_name.lower().endswith(extension) == True:
        return f_name
    else:
        print("Wrong file format. Please try with another file.")
        sys.exit(1)

command_string = 'jupyter nbconvert {} --to slides --post serve'.format(check_extension(file_name))
os_platform = platform.system()

if os_platform == 'Windows':
    subprocess.call(['C:\\windows\\system32\\cmd.exe',
            '/C', 
            command_string])
                
elif os_platform in ['Linux','Darwin']:
    subprocess.call(command_string, shell=True)

else:
    print('Unrecognised platform')