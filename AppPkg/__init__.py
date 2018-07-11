#pkg='Test package'
#print (f'CALLED __init__.py')
#print(f"\t__name__={__name__}, __package__={__package__}, dir()={list(filter(lambda x: x[0]!='_', dir()))}")


#print(f'\tBefore from AppPkg._AppPkg import main')
from AppPkg._AppPkg import main
#print(f'\tAfter from AppPkg._AppPkg import main')
#print(f"\t\t__name__={__name__}, __package__={__package__}, dir()={list(filter(lambda x: x[0]!='_', dir()))}")

