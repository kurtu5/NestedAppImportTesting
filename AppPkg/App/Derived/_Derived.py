name = 'derived class'
#import Base
#class DerivedClass(Base.BaseClass):

from AppPkg.App.Base import Base
class Derived(Base):
    def __init__(self, arg):
#        super().__init__(arg)
        print(f'initializing {__class__}')
        print(f'{arg}')