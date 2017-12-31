#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from subprocess import Popen, PIPE

XSEL = '/usr/bin/xsel'

class Clipboard():
    def read(self,):
        proc = Popen([XSEL, '-o',],  stdout=PIPE)
        return proc.stdout.read()

    def write(self, contents):
        proc = Popen([XSEL, '-i'], stdin=PIPE)
        proc.communicate(input=contents)
        proc.terminate()
        return True

    def size(self,):
        pass

if __name__ == "__main__":
    clipboard = Clipboard()

    if len(sys.argv) > 1:
        clipboard.write(str.encode(''.join(sys.argv[1:])))
    else:
        print(clipboard.read().decode())

    sys.exit(0)
