# Bullshit to allow "python blah/blah/file.py"
import sys
sys.path = [''] + sys.path

from AppPkg.App import App
