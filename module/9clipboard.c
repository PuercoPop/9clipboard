#include "9clipboard.h"

#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/fs.h>

static int device_open(struct inode *, struct file *);
static int device_release(struct inode *, struct file *);
static ssize_t device_read(struct file *, char *, size_t, loff_t *);
static ssize_t device_write(struct file *, const char *, size_t, loff_t *);

struct file_operations fops = {
	.read = device_read,
	.write = device_write,
	.open = device_open,
	.release = device_release
};


static int device_open(struct inode *inode, struct file *file)
{
	return 0;
};

static int device_release(struct inode *inode, struct file *file)
{
	return 0;
};
static ssize_t device_read(struct file *file, char *buffer, size_t length, loff_t *offset)
{
	printk(KERN_INFO "%s\n", __FILE__);
	return 0;
};
static ssize_t device_write(struct file *file, const char *buffer, size_t length, loff_t *offset)
{
	return 0;
};

int
init_clipboard(void)
{
	// see how to avoid mknod here
	major =	register_chrdev(0, DEVICE_NAME, &fops);

	if (major < 0) {
		printk(KERN_ALERT "Failed to register 9clip. Error code %d\n", major);
		return major;
	}
	printk(KERN_INFO "Hello World %d!\n", major);
	return 0;
}

void
exit_clipboard(void)
{
	unregister_chrdev(major, DEVICE_NAME);
	printk(KERN_INFO "Goodbye Cruel World\n");
	return;
}

module_init(init_clipboard);
module_exit(exit_clipboard);


MODULE_LICENSE("GPL");
MODULE_AUTHOR(DRIVER_AUTHOR);
MODULE_DESCRIPTION(DRIVER_DESC);
