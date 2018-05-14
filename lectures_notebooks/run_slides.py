import subprocess
import sys
import platform
import argparse
import pkgutil

parser=argparse.ArgumentParser(
    description='''Simple script to run ipynb notebooks as slides.
            Installs jupyter if not present.''')
parser.add_argument('--file', type=str, default='1.Python101.ipynb', 
    help='Specifies the target file. If left empty runs 1.Python101.ipynb')
args, unknown = parser.parse_known_args()


def run_command(command):
    os_platform = platform.system()
    
    if os_platform == 'Windows':
        return subprocess.call(['C:\\windows\\system32\\cmd.exe',
            '/C', 
            command])
    elif os_platform in ['Linux', 'Darwin']:
        return subprocess.call(command, shell=True)
    else:
        print('Unrecognised platform')
        sys.exit(1)


def load_pip():
    pip_loader = pkgutil.find_loader('pip')
    pip_found = pip_loader is not None

    if pip_found == False:
        run_command('easy_install pip')
        run_command('python {} {}'.format(sys.argv[0], args.file))
        sys.exit(1)

    try:
        from pip import main as pipmain
    except ImportError:
        from pip._internal import main as pipmain
            
    try:
        return pipmain
    except:
        print("Could not import pip.")
        sys.exit(1)

try:
    import jupyter
except ImportError:
    pipmain = load_pip()
    pipmain(['install', 'jupyter'])

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

try:
    run_command('jupyter nbconvert {} --to slides --post serve'.format(check_extension(file_name)))
except KeyboardInterrupt:
    sys.exit("Exiting...")
