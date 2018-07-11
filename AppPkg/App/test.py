# Bullshit to allow "python blah/blah/file.py"
import sys
sys.path = [''] + sys.path

from AppPkg.App.Derived import Derived

# Test is app can use a derived class
dclass = Derived('I am derived')
print(dclass.__class__)
print(dir(Derived))
        