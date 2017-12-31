#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import errno
import sys
from os import getuid, getgid

from time import time
from stat import S_IFDIR, S_IFREG
from fuse import FUSE, Operations, FuseOSError


class ClipboardFS(Operations):

	def __init__(self):
		now = time()
		self.fd = 0
		self.contents = "Hello Kitty\n"
		self.files = dict()
		self.files['/'] = dict(
			st_mode=(S_IFDIR | 0o755),
			st_atime=now,
			st_ctime=now,
			st_mtime=now,
			st_uid=getuid(),
			st_guid=getgid(),
			st_nlink=2)

		self.files['/board'] = dict(
			st_mode=(S_IFREG | 0o755),
			st_atime=now,
			st_ctime=now,
			st_mtime=now,
			st_uid=getuid(),
			st_guid=getgid(),
			st_size=len(self.contents),
			st_nlink=1)

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
		return str.encode(self.contents)

	def readdir(self, path, fh):
		if path == "/":
			return ['.', '..', 'board']
		else:
			raise FuseOSError(errno.ENOENT)

if __name__ == "__main__":
	try:
		mount_path = sys.argv[1]
	except IndexError:
		print("Must specify the path to mount the filesystem on.", file=sys.stderr)
		sys.exit(-1)

	clipboard = ClipboardFS()
	FUSE(clipboard, mount_path, foreground=True)
