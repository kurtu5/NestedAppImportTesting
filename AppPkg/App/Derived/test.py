# Bullshit to allow "python blah/blah/file.py"
import sys
sys.path = [''] + sys.path

#from ..Base import Base


from AppPkg.App.Base import Base

class NewBase(Base):
    def __init__(self, args):
        super().__init__(args)
        
newbae = NewBase('newbase args')