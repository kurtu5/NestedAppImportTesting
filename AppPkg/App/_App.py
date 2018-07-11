name = 'app class'


from .Derived import Derived
class AppClass(object):
    def __init__(self, arg):
        print(f'initializing {__class__}')
        print(f'{arg}')
        self.derived = Derived('derived class')