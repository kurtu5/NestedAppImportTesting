# Bullshit to allow "python blah/blah/file.py"
import sys
sys.path = [''] + sys.path

from Derived import Derived
Derived('hi from testDerived')