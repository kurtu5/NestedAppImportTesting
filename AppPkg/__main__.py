#print(f"CALLED __main__.py")
#print(f"\t__name__={__name__}, __package__={__package__}, dir()={list(filter(lambda x: x[0]!='_', dir()))}")
#
#print(f'Before import AppPkg')

import AppPkg

#print(f'After')
#print(f"\t\t__name__={__name__}, __package__={__package__}, dir()={list(filter(lambda x: x[0]!='_', dir()))}")
#print(f"\t\tAND dir(AppPkg)={list(filter(lambda x: x[0]!='_', dir(AppPkg)))}")

if __name__ == "__main__":
    AppPkg.main()
    
