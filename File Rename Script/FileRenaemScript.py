import os
for dpath, dnames, fnames in os.walk('E:\MUSIC'):
    for f in fnames:
        os.chdir(dpath)
        os.rename(f, f.replace('',' '))