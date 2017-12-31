#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import errno
import sys
from os import getuid, getgid

from time import time
from stat import S_IFDIR, S_IFREG
from fuse import FUSE, Operations, FuseOSError

from RegularFile import RegularFile
from clipboard import Clipboard

class ClipboardFile(Clipboard, RegularFile):
        pass

class ClipboardFS(Operations):

	def __init__(self):
		now = time()
		self.fd = 0
		self.contents = b"Hello Kitty\n"
		self.files = dict()
		self.files['/'] = dict(
			st_mode=(S_IFDIR | 0o755),
			st_atime=now,
			st_ctime=now,
			st_mtime=now,
			st_uid=getuid(),
			st_gid=getgid(),
			st_nlink=2)

		self.files['/board'] = ClipboardFile()


	def getattr(self, path, fh=None):
		if path not in self.files.keys():
			raise FuseOSError(errno.ENOENT)

		return self.files[path]

	def destroy(self, path):
		print("Shutting down")

	def opendir(self, path):
		return self.fd

	def open(self, path, flags):
		return 1

	def read(self, path, size, offset, fh):
		if path == '/board':
			return self.files[path].read()

	def readdir(self, path, fh):
		if path == "/":
			return ['.', '..', 'board']
		else:
			raise FuseOSError(errno.ENOENT)

	def write(self, path, data, offset, fh):
		if path == "/board":
			self.contents = data

if __name__ == "__main__":
	try:
		mount_path = sys.argv[1]
	except IndexError:
		print("Must specify the path to mount the filesystem on.", file=sys.stderr)
		sys.exit(-1)

	clipboard = ClipboardFS()
	FUSE(clipboard, mount_path, foreground=True)

