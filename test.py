# Bullshit to allow "python blah/blah/file.py"
import sys
sys.path = [''] + sys.path
import AppPkg
AppPkg.main()
