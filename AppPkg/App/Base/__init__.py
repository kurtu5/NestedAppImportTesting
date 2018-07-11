pkg='Base package'
print (f'Import "{pkg}" as {__package__}')

from AppPkg.App.Base._Base \
    import BaseClass as Base