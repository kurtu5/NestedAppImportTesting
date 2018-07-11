#print(f'CALLED _AppPkg.py')
#print(f"\t__name__={__name__}, __package__={__package__}, dir()={list(filter(lambda x: x[0]!='_', dir()))}")


from AppPkg.App import App
def main():
    print("i am main")
    print(dir(App))
    #App('class instance')
#print(f"\t__name__={__name__}, __package__={__package__}, dir()={list(filter(lambda x: x[0]!='_', dir()))}")

