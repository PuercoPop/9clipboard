# More information at /home/puercopop/Projects/linux/Documentation/kbuild/makefiles.txt

obj-m += 9clipboard.o

all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
