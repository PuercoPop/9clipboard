# -*- coding: utf-8 -*-

from collections.abc import Mapping
from os import getuid, getgid
from stat import S_IFREG
from time import time

class RegularFile(Mapping):
    def __init__(self, *args, **kwargs):
        super(type(self)).__init__(*args, **kwargs)

        now = time()
        self.stat = dict(
            st_mode=(S_IFREG | 0o644),
	    st_atime=now,
	    st_ctime=now,
	    st_mtime=now,
	    st_uid=getuid(),
	    st_gid=getgid(),
	    st_size=self.size(),
	    st_nlink=1,
        )

    def __getitem__(self, item):
        if item == 'st_size':
            return self.size()
        else:
            return self.stat.__getitem__(item)

    def __iter__(self,):
        return self.stat.__iter__()

    def __len__(self, item):
        return self.stat.__len__()

if __name__ == "__main__":
    f = RegularFile()
    print(f.keys())
    print(f['st_mode'])
