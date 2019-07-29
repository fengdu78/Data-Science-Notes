# This script is adapted from Andreas Mueller:
# https://github.com/amueller/scipy-2018-sklearn/blob/master/check_env.ipynb

from __future__ import print_function
from distutils.version import LooseVersion as Version
import sys


try:
    import curses
    curses.setupterm()
    assert curses.tigetnum("colors") > 2
    OK = "\x1b[1;%dm[ OK ]\x1b[0m" % (30 + curses.COLOR_GREEN)
    FAIL = "\x1b[1;%dm[FAIL]\x1b[0m" % (30 + curses.COLOR_RED)
except:
    OK = '[ OK ]'
    FAIL = '[FAIL]'

try:
    import importlib
except ImportError:
    print(FAIL, "Python version 3.4 (or 2.7) is required,"
                " but %s is installed." % sys.version)


def import_version(pkg, min_ver, fail_msg=""):
    mod = None
    try:
        mod = importlib.import_module(pkg)
        if pkg in {'PIL'}:
            ver = mod.VERSION
        else:
            ver = mod.__version__
        if Version(ver) < min_ver:
            print(FAIL, "%s version %s or higher required, but %s installed."
                  % (lib, min_ver, ver))
        else:
            print(OK, '%s version %s' % (pkg, ver))
    except ImportError:
        print(FAIL, '%s not installed. %s' % (pkg, fail_msg))
    return mod


# first check the python version
print('Using python in', sys.prefix)
print(sys.version)
pyversion = Version(sys.version)
if pyversion >= "3":
    if pyversion < "3.5":
        print(FAIL, "Python version 3.5 (or 2.7) is required,"
                    " but %s is installed." % sys.version)
elif pyversion >= "2":
    if pyversion < "2.7":
        print(FAIL, "Python version 2.7 is required,"
                    " but %s is installed." % sys.version)
else:
    print(FAIL, "Unknown Python version: %s" % sys.version)

print()
requirements = {'numpy': "1.9", 'scipy': "0.13.3", 'matplotlib': "2.0",
                'sklearn': "0.20", 'pandas': "0.21", 'notebook': "5"}

# now the dependencies
for lib, required_version in list(requirements.items()):
    import_version(lib, required_version)
